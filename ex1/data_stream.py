from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    抽象基底クラス
    必要なクラスを宣言する
    """

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:
        return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return ({})


class SensorStream(DataStream):
    """
    temp, humidity, pressureを分析するクラス
    DataStreamを継承し、メソッドをオーバーライドする
    """
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data_type = "Environmantal Data"
        self.critical_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        メソッドのオーバーライド
        渡されたデータを整形して返す
        """
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")
        print(f"Processing sensor batch: {data_batch}")
        temps = []
        self.reading_num = len(data_batch)
        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            key, value = item.split(":", 1)
            if key == "temp":
                try:
                    temps.append(float(value))
                except ValueError:
                    print("Error")
        if not temps:
            return (f"Sensor analysis: {self.reading_num} readings processed")
        avg_temp = sum(temps) / len(temps)
        return (f"Sensor analysis: {self.reading_num}) readings processed,"
                f" avg temp: {avg_temp}°C")

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:
        alerts = []
        for item in data_batch:
            if isinstance(item, str):
                try:
                    key, value = item.split(":", 1)
                    if key == "temp":
                        if float(value) >= 20:
                            alerts.append(item)
                    if key == "humidity":
                        if float(value) >= 60:
                            alerts.append(item)
                    if key == "pressure":
                        if float(value) >= 1500:
                            alerts.append(item)
                except ValueError:
                    continue
        self.critical_count = len(alerts)
        return (alerts)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return ({
            "type": "Sensor",
            "readings": self.reading_num,
            "critical": self.critical_count
        })


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data_type = "Financial Data"
        self.large_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")
        print(f"Processing sensor batch: {data_batch}")
        total = 0
        self.operations = len(data_batch)
        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            key, value = item.split(":", 1)
            try:
                amount = int(value)
            except ValueError:
                continue
            if key == "sell":
                total += amount
            elif key == "buy":
                total -= amount
        if total > 0:
            pm = "+"
        else:
            pm = ""
        return (f"Transaction analysis: {len(data_batch)} operations,"
                f" net flow: {pm}{total} units")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        large = []
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                key, value = item.split(":", 1)
                try:
                    amount = int(value)
                except ValueError:
                    continue
                if amount >= 1000:
                    large.append(item)
        self.large_count = len(large)
        return large

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return ({
            "type": "Transaction",
            "readings": self.operations,
            "large": self.large_count
        })


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")
        print(f"Processing sensor batch: {data_batch}")
        error_count = 0
        self.events = len(data_batch)
        for item in data_batch:
            if not isinstance(item, str) or item not in ["login", "error"]:
                continue
            if item == "error":
                error_count += 1
        return (f"Event analysis: {len(data_batch)} events,"
                f" {error_count} error detected")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return ({
            "type": "Event",
            "readings": self.events
        })


class StreamProcessor:
    """
    データタイプに応じて動かすクラスを決める
    """
    def run(
        self,
        stream: DataStream,
        batch: List[Any]
    ) -> tuple[str, Dict[str, Union[str, int, float]]]:
        result = stream.process_batch(batch)
        stats = stream.get_stats()
        return result, stats


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    # === Preparing Data ===

    streams = [SensorStream("SENSOR_001"),
               TransactionStream("TRANS_001"),
               EventStream("EVENT_001")]

    batches = [["temp:22.5", "humidity:65", "pressure:1013"],
               ["sell:100", "buy:150", "sell:75"],
               ["login", "error", "login"]]

    processor = StreamProcessor()
    all_stats = []
    for stream, batch in zip(streams, batches):
        stream.filter_data(batch)
        result, stats = processor.run(stream, batch)
        all_stats.append(stats)
        print(result)
        print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print()

    print("Batch 1 Results:")
    critical_sensor = 0
    large_transaction = 0
    for data in all_stats:
        if data["type"] == "Sensor":
            critical_sensor += data["critical"]
            print(f"- Sensor data: {data['readings']} readings processed")
        if data["type"] == "Transaction":
            large_transaction += data["large"]
            print(f"- Transaction data:"
                  f" {data['readings']} operations processed")
        if data["type"] == "Event":
            print(f"- Event data: {data['readings']} events processed")

    print()

    print("Stream filtering active: High-priority data only")
    print(f"Filtered results: {critical_sensor} critical sensor alerts,"
          f" {large_transaction} large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
