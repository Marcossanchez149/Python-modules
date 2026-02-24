#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stream_type = "Generic"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.stream_type
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = []
            count = len(data_batch)
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    key, val = item.split(":")
                    if key == "temp":
                        temps.append(float(val))
            avg_temp = sum(temps) / len(temps) if temps else 0
            return (f"Sensor analysis: {count} readings processed,"
                    f"avg temp: {avg_temp:.1f}°C")
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "High-priority":
            return [x for x in data_batch if "alert" in x or "critical" in x]
        return data_batch


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net_flow = 0
            count = len(data_batch)

            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    action, amount = item.split(":")
                    value = int(amount)
                    if action == "buy":
                        net_flow += value
                    elif action == "sell":
                        net_flow -= value
            sign = "+" if net_flow >= 0 else ""
            return (f"Transaction analysis: {count} operations,"
                    f"net flow: {sign}{net_flow} units")
        except ValueError:
            return "Error: Invalid transaction format"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "High-priority":
            filtered = []
            for item in data_batch:
                if ":" in item:
                    _, amount = item.split(":")
                    if int(amount) > 200:
                        filtered.append(item)
            return filtered
        return data_batch


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        count = len(data_batch)
        errors = 0
        for item in data_batch:
            if "error" in item:
                errors += 1
        return f"Event analysis: {count} events, {errors} error detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "High-priority":
            return [x for x in data_batch if "error" in x]
        return data_batch


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, data_map: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            if stream.stream_id in data_map:
                print(stream.process_batch(data_map[stream.stream_id]))
                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: {len(data_map[stream.stream_id])} "
                          f"readings processed")
                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: "
                          f"{len(data_map[stream.stream_id])} "
                          f"operations processed")
                elif isinstance(stream, EventStream):
                    print(f"- Event data: "
                          f"{len(data_map[stream.stream_id])} "
                          f"events processed")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_data}")
    print(sensor.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    trans_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_data}")
    print(trans.process_batch(trans_data))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    print(event.process_batch(event_data))
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)
    batch_data = {
        "SENSOR_001": ["temp:20", "temp:21"],
        "TRANS_001": ["buy:10", "sell:5", "buy:20", "sell:2"],
        "EVENT_001": ["login", "click", "logout"]
    }
    print("Batch 1 Results:")
    processor.process_streams(batch_data)
    print("\nStream filtering active: High-priority data only")
    filter_input_sensor = ["temp:20", "critical_alert:Overheat",
                           "critical_alert:Fail"]
    filter_input_trans = ["buy:10", "sell:5000"]
    res_sensor = sensor.filter_data(filter_input_sensor, "High-priority")
    res_trans = trans.filter_data(filter_input_trans, "High-priority")
    print(f"Filtered results: {len(res_sensor)} critical sensor alerts, "
          f"{len(res_trans)} large transaction")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
