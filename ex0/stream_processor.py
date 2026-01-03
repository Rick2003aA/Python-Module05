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
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return (False)
        for item in data:
            if not isinstance(item, (int, float)):
                return (False)
        print("Validation: Numeric data verified")
        return (True)

    def _compute(self, data: Any) -> str:
        count = len(data)
        total = sum(data)
        avg = total / count

        return (f"Processed {count} numeric values, sum={total}, avg={avg}")

    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")

        if not self.validate(data):
            return ("Invalid numeric data")

        result = self._compute(data)

        return (self.format_output(result))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or not data.strip():
            return (False)
        print("Validation: Text data verified")
        return (True)

    def _compute(self, data: Any) -> str:
        text_len = len(data)
        splitted = data.split(" ")
        word_count = len(splitted)
        return (f"Processed text {text_len} characters, {word_count} words")

    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        print(f'Processing data: "{data}"')
        if not self.validate(data):
            return ("Invalid text data")

        result = self._compute(data)

        return (self.format_output(result))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return (False)

        if ":" not in data:
            return (False)

        level, message = data.split(":", 1)
        if level not in ("ERROR", "INFO"):
            return (False)

        if not message.strip():
            return (False)
        print("Validation: Log entry verified")
        return (True)

    def _analyze(self, data: str) -> str:
        level, message = data.split(":", 1)
        message = message.strip()

        if level == "ERROR":
            return (f"[ALERT] ERROR level detected: {message}")
        else:
            return (f"[INFO] INFO level detected: {message}")

    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        print(f'Processing data: "{data}"')
        if not self.validate(data):
            return ("Invalid log data")

        result = self._analyze(data)
        return (self.format_output(result))


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    num_p = NumericProcessor()
    txt_p = TextProcessor()
    log_p = LogProcessor()
    print(num_p.process([1, 2, 3, 4, 5]))
    print()
    print(txt_p.process("Hello Nexus World"))
    print()
    print(log_p.process("ERROR: Connection timeout"))
    print()
    print("=== polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    only_result_num = num_p._compute([1, 2, 3])
    only_result_txt = txt_p._compute('Hello Nexus World')
    only_result_log = log_p._analyze("INFO: System ready")
    print(f"Result 1: {only_result_num}")
    print(f"Result 2: {only_result_txt}")
    print(f"Result 3: {only_result_log}")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
