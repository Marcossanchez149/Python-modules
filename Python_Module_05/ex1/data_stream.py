#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.

    A DataStream defines the core interface for processing batches
    of incoming data and optionally filtering them based on criteria.
    Subclasses must implement the `process_batch` method.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize the data stream.

        Args:
            stream_id (str): Unique identifier of the stream.
        """

        self.stream_id = stream_id
        self.stream_type = "Generic"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data elements.

        Args:
            data_batch (List[Any]): Collection of raw data entries.

        Returns:
            str: A summary or result of the processed batch.
        """

        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter a batch of data based on optional criteria.

        Default implementation returns the batch unchanged.

        Args:
            data_batch (List[Any]): The input data batch.
            criteria (Optional[str]): Filtering rule identifier.

        Returns:
            List[Any]: Filtered data batch.
        """

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieve metadata about the stream.

        Returns:
            Dict[str, Union[str, int, float]]: Dictionary containing
            stream identifier and stream type.
        """

        return {
            "id": self.stream_id,
            "type": self.stream_type
        }


class SensorStream(DataStream):
    """
    Data stream specialized in processing environmental sensor data.

    Expected input format:
        "key:value"
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a SensorStream instance.

        Args:
            stream_id (str): Unique sensor stream identifier.
        """

        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process environmental readings and compute average temperature.

        Args:
            data_batch (List[Any]): Sensor readings formatted as strings.

        Returns:
            str: Summary including number of readings and average temperature.
        """

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
        """
        Filter sensor readings based on priority criteria.

        Args:
            data_batch (List[Any]): Sensor data entries.
            criteria (Optional[str]): If set to "High-priority",
                only critical or alert entries are returned.

        Returns:
            List[Any]: Filtered sensor readings.
        """

        if criteria == "High-priority":
            return [x for x in data_batch if "alert" in x or "critical" in x]
        return data_batch


class TransactionStream(DataStream):
    """
    Data stream specialized in financial transaction processing.

    Expected input format:
        "action:amount"
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a TransactionStream instance.

        Args:
            stream_id (str): Unique transaction stream identifier.
        """

        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process financial transactions and compute net flow.

        Args:
            data_batch (List[Any]): Transaction records.

        Returns:
            str: Summary including operation count and net flow.
        """

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
            sign = "+" if net_flow >= 0 else "-"
            return (f"Transaction analysis: {count} operations,"
                    f"net flow: {sign}{net_flow} units")
        except ValueError:
            return "Error: Invalid transaction format"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter transactions based on priority criteria.

        Args:
            data_batch (List[Any]): Transaction records.
            criteria (Optional[str]): If set to "High-priority",
                returns transactions with amount greater than 200.

        Returns:
            List[Any]: Filtered transaction records.
        """

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
    """
    Data stream specialized in system event monitoring.

    Counts total events and detects occurrences of error-related events.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize an EventStream instance.

        Args:
            stream_id (str): Unique event stream identifier.
        """

        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process system events and count error occurrences.

        Args:
            data_batch (List[Any]): Event entries.

        Returns:
            str: Summary including total events and detected errors.
        """

        count = len(data_batch)
        errors = 0
        for item in data_batch:
            if "error" in item:
                errors += 1
        return f"Event analysis: {count} events, {errors} error detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter events based on priority criteria.

        Args:
            data_batch (List[Any]): Event entries.
            criteria (Optional[str]): If set to "High-priority",
                returns only error-related events.

        Returns:
            List[Any]: Filtered event list.
        """

        if criteria == "High-priority":
            return [x for x in data_batch if "error" in x]
        return data_batch


class StreamProcessor:
    """
    Manager class responsible for coordinating multiple DataStream instances.

    Enables polymorphic processing of heterogeneous data streams
    through a unified interface.
    """

    def __init__(self):
        """Initialize an empty stream registry."""

        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """
        Register a new data stream.

        Args:
            stream (DataStream): Stream instance to be managed.
        """

        self.streams.append(stream)

    def process_streams(self, data_map: Dict[str, List[Any]]) -> None:
        """
        Process multiple streams using a dictionary of batch data.

        Args:
            data_map (Dict[str, List[Any]]): Mapping between stream IDs
                and corresponding data batches.
        """

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
    """
    Program entry point.

    Demonstrates:
        - Initialization of different stream types.
        - Batch processing per stream.
        - Polymorphic stream coordination via StreamProcessor.
        - Filtering high-priority data.
    """

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
