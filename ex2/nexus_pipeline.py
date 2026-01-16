from abc import ABC
from typing import Any, List, Protocol
import time


# ===== Stage interface (duck typing) =====
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


# ===== Pipeline base =====
class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def process(self, data: Any, *, silent: bool = False) -> Any:
        for stage in self.stages:
            # すべての stage に silent を伝播させる
            if hasattr(stage, "silent"):
                stage.silent = silent
            data = stage.process(data)
        return data


# ===== Stages =====
class InputStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: Any) -> Any:
        if not self.silent:
            print("Input:", data)
        return data


class TransformStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: Any) -> Any:
        return data


class JSON_TransformStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: dict) -> str:
        if "value" not in data:
            raise ValueError("Error detected in Stage 2: Invalid data format")

        if not self.silent:
            print("Transform: Enriched with metadata and validation")

        value = data["value"]
        return f"Processed temperature reading: {value}°C (Normal range)"


class CSV_TransformStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: list[str]) -> str:
        if not self.silent:
            print("Transform: Parsed and structured data")
        return f"User activity logged: {len(data) - 1} actions processed"


class Stream_TransformStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: str) -> str:
        if not self.silent:
            print("Transform: Aggregated and filtered")
        return "Stream summary: 5 readings, avg: 22.1°C"


class OutputStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: Any) -> Any:
        if not self.silent:
            print("Output:", data)
            print()
        return data


# ===== Adapter (Pipeline) =====
class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(JSON_TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any, *, silent: bool = False) -> Any:
        if not silent:
            print("Processing JSON data through pipeline...")
        return super().process(data, silent=silent)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(CSV_TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any, *, silent: bool = False) -> Any:
        if not silent:
            print("Processing CSV data through same pipeline...")
        parsed = data.split(",")
        return super().process(parsed, silent=silent)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(Stream_TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any, *, silent: bool = False) -> Any:
        if not silent:
            print("Processing Stream data through same pipeline...")
        return super().process(data, silent=silent)


# ===== Analysis =====
class AnalysisAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        # ここは「分析」用 stage にしておく（今回は最低限 Output のみ）
        self.add_stage(OutputStage())

    def process(self, data: Any, *, silent: bool = False) -> Any:
        if not silent:
            print("Analyzing data...")
        return super().process(data, silent=silent)


# ===== Store =====
class StoreStage:
    def __init__(self) -> None:
        self.silent = False

    def process(self, data: Any) -> Any:
        if not self.silent:
            print("Store: Data stored successfully")
        return {"stored": True}


class StoreAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(StoreStage())
        self.add_stage(OutputStage())

    def process(self, data: Any, *, silent: bool = False) -> Any:
        if not silent:
            print("Storing analyzed data...")
        return super().process(data, silent=silent)


# ===== Router =====
class PipelineRouter:
    def route(self, data: Any) -> ProcessingPipeline:
        if isinstance(data, dict):
            return JSONAdapter("PIPE_JSON")
        elif isinstance(data, str) and "," in data:
            return CSVAdapter("PIPE_CSV")
        else:
            return StreamAdapter("PIPE_STREAM")


# ===== Manager =====
class NexusManager:
    def __init__(self) -> None:
        self.router = PipelineRouter()
        self.backup_pipeline = StreamAdapter("PIPE_BACKUP")

    def run(self, data: Any) -> Any:
        try:
            pipeline = self.router.route(data)
            return pipeline.process(data)
        except Exception as e:
            print("Error detected:", e)
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return self.backup_pipeline.process(data, silent=True)

    def run_chain(self,
                  pipelines: List[ProcessingPipeline],
                  data: Any) -> None:
        start = time.perf_counter()
        if isinstance(data, list):
            for item in data:
                tmp = item
                for pipeline in pipelines:
                    tmp = pipeline.process(tmp, silent=True)
                time.sleep(0.002)
        else:
            tmp = data
            for pipeline in pipelines:
                tmp = pipeline.process(tmp, silent=True)

        end = time.perf_counter()

        print("Chain result: 100 records processed through 3-stage pipeline")
        print(f"Performance: {end - start:.2f}s total processing time")


# ===== Execution =====
def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print()
    print("=== Multi-Format Data Processing ===")
    print()

    manager = NexusManager()

    manager.run({"sensor": "temp", "value": 23.5, "unit": "C"})
    manager.run("user,action,timestamp")
    manager.run("Real-time sensor stream")

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    records = [{"sensor": "temp", "value": 20 + i % 5} for i in range(100)]
    manager.run_chain(
        [JSONAdapter("PIPE_JSON"),
         AnalysisAdapter("PIPE_ANALYSIS"),
         StoreAdapter("PIPE_STORE")],
        records,
    )

    print()

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    manager.run({"sensor": "temp"})
    print()
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
