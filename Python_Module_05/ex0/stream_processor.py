#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class that defines a common interface for data processors.

    Subclasses must implement the `process` and `validate` methods.
    This class also provides a helper method to standardize output formatting.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the given data and return a formatted string result.

        Args:
            data (Any): The input data to be processed.

        Returns:
            str: A string describing the processing result.
        """

        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate the given input data.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if the data is valid for processing, False otherwise.
        """

        pass

    def format_output(self, result: str) -> str:
        """
        Format the processing result with a standard prefix.

        Args:
            result (str): The raw processing result.

        Returns:
            str: The formatted output string.
        """

        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Concrete implementation of DataProcessor for numeric list data.

    This processor validates that the input is a list of numeric values,
    then calculates the total sum and average of the numbers.
    """

    def process(self, data: Any) -> str:
        """
        Process a list of numeric values by calculating count, sum,
        and average.

        Args:
            data (Any): A list expected to contain numeric values.

        Returns:
            str: A formatted summary of numeric processing results or
                 an error message if validation fails.
        """

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
        """
        Validate that the input is a list containing only numeric values.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if data is a list of numeric values, False otherwise.
        """

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
    """
    Concrete implementation of DataProcessor for text data.

    This processor validates that the input is a string and then
    calculates the number of characters and words.
    """

    def process(self, data: Any) -> str:
        """
        Process a string by counting its characters and words.

        Args:
            data (Any): A string expected for text processing.

        Returns:
            str: A formatted summary of text processing results or
                 an error message if validation fails.
        """

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
        """
        Validate that the input is a string.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if data is a string, False otherwise.
        """

        if (isinstance(data, str)):
            return (True)
        return (False)


class LogProcessor(DataProcessor):
    """
    Concrete implementation of DataProcessor for log entries.

    This processor validates log strings in the format:
        "LEVEL: message"

    It categorizes logs as ALERT (for ERROR level) or INFO.
    """

    def process(self, data: Any) -> str:
        """
        Process a log entry string and classify it based on its level.

        Args:
            data (Any): A log entry string formatted as "LEVEL: message".

        Returns:
            str: A formatted alert or info message, or an error message
                 if validation fails.
        """

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
        """
        Validate that the input is a properly formatted log string.

        Args:
            data (Any): The input data to validate.

        Returns:
            bool: True if data is a string containing ': ', False otherwise.
        """

        return isinstance(data, str) and ": " in data


def main():
    """
    Entry point of the program.

    Demonstrates:
        - Individual processor usage.
        - Polymorphic behavior through a common interface.
        - Processing of numeric, text, and log data types.
    """

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric_processor = NumericProcessor()
    print("Initializing Numeric Processor...")
    print(f"{numeric_processor.process([1, 2, 3, 4])}")
    text_processor = TextProcessor()
    print("Initializing Text Processor...")
    print(text_processor.process("Hello Nexus World"))
    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    print(log_processor.process("ERROR: Connection timeout"))

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
