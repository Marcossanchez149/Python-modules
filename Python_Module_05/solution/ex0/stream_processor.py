#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if (self.validate(data)):
            print("Validation: Numeric data verified")
            size = 0
            sum = 0
            for num in data:
                size += 1
                sum += num
            sol = (f"Processed {size} numeric values,"
                   f"sum={sum}, avg={sum / size}")
            return (self.format_output(sol))
        else:
            return ("Processing data: There is a invalid value")

    def validate(self, data: Any) -> bool:
        is_num = True
        x = 0
        try:
            if (not isinstance(data, list)):
                is_num = False
            for num in data:
                x += int(num)
        except Exception:
            is_num = False
        finally:
            return (is_num)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if (self.validate(data)):
            print("Validation: Text data verified")
            characters = 0
            words = 0
            for c in data:
                characters += 1
            words = len(data.split())
            sol = (f"Processed text: {characters} "
                   f"characters, {words} words")
            return (self.format_output(sol))
        else:
            return ("Processing data: Its not a string")

    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return (True)
        return (False)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if self.validate(data):
            print("Validation: Log entry verified")
            level, msg = data.split(": ", 1)
            if level == "ERROR":
                return f"[ALERT] {level} level detected: {msg}"
            else:
                return f"[INFO] {level} level detected: {msg}"
        return "Error: Invalid log format"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ": " in data


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric_processor = NumericProcessor()
    print("Initializing Numeric Processor...")
    print(f"{numeric_processor.process([1, 2, 3, 4])}")
    textProcessor = TextProcessor()
    print("Initializing Text Processor...")
    print(textProcessor.process("Hello Nexus World"))
    print("Initializing Log Processor...")
    logProcessor = LogProcessor()
    print(logProcessor.process("ERROR: Connection timeout"))

    print("\n \n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    inputs = [
        [10, 20, 30],
        "Hello Polymorphism",
        "info: System ready"
    ]
    for i, (proc, data) in enumerate(zip(processors, inputs)):
        result = proc.process(data)
        print(f"Result {i+1}: {result}")


if __name__ == "__main__":
    main()
