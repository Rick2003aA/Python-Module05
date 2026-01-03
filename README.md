## Ex0

- **概要**
    
    同じメソッド名で、全く異なるデータ型を安全かつ柔軟に処理できる設計を理解・実装する。
    
    1. ポリモーフィズムの理解
        
        process()という同じメソッド名でも
        
        - Numeric Processor → 数値として処理
        - Text Processor → 文字列として処理
        - Log Processor → ログとして処理
        
        **→オブジェクトが勝手に正しい処理を選ぶ。**
        
        - 具体的な流れ
            
            Data Processor クラスで共通インターフェースを定義し、
            
            実際の処理は各サブクラスの process() が担当する
            
            ```jsx
                    DataProcessor (ABC)
                          ↑
               ┌──────────┼──────────┐
               │          │          │
            Numeric   TextProcessor  LogProcessor
            Processor
            ```
            
        
- **要件**
    - **Base Class**: Data Processor→共通の処理インターフェースを定義する抽象基本クラス
    - **Specialized Classes**: Numeric Processor(), Text Processor(), Log Processor()
    - Required Methods:
        - process(self, data: Any) -> str
        - validate(self, data: Any) -> bool
        - format_output(self, result: str) -> str
    - ポリモーフィズムの挙動: 同じメソッドが呼ばれても、型ごとに違う挙動を行う
    - 必要な実装：
        - ABC と @abstract method を使用して Data Processor 抽象基底クラスを作成する
        - process() と validate() を抽象メソッドとしてマークする
        - オーバーライド可能な format_output() のデフォルト実装を提供する
        - サブクラスで抽象メソッドをオーバーライドして、特殊な動作を提供する
        - 同じインターフェースを介して異なるデータ型を処理することで、ポリモーフィックな使用方法を示す
        - 無効なデータに対する適切なエラー処理を組み込む
    
    Example:
    
    ```jsx
    $> python3 stream_processor.py
    === CODE NEXUS - DATA PROCESSOR FOUNDATION ===
    Initializing Numeric Processor...
    Processing data: [1, 2, 3, 4, 5]
    Validation: Numeric data verified
    Output: Processed 5 numeric values, sum=15, avg=3.0
    Initializing Text Processor...
    Processing data: "Hello Nexus World"
    Validation: Text data verified
    Output: Processed text: 17 characters, 3 words
    Initializing Log Processor...
    Processing data: "ERROR: Connection timeout"
    Validation: Log entry verified
    Output: [ALERT] ERROR level detected: Connection timeout
    === Polymorphic Processing Demo ===
    Processing multiple data types through same interface...
    Result 1: Processed 3 numeric values, sum=6, avg=2.0
    Result 2: Processed text: 12 characters, 2 words
    Result 3: [INFO] INFO level detected: System ready
    Foundation systems online. Nexus ready for advanced streams.
    ```
    

## ex1

- **概要**
    
    Data Stream を抽象基底クラスにして共通インターフェースを定義する
    
    Sensor Stream / Transaction Stream / Event Stream がそれをオーバーライド
    
    Stream Processor はData Stream型として扱うだけで全部動かせる
    
- **要件**
    
    **Specialized Streams: Data Streamをオーバーライド**
    
    - Sensor Stream(stream_id) :
    - Transaction Stream(stream_id)
    - Event Stream(stream_id)
    
    **Required Methods: Data Streamに含めるメソッド**
    
    - process_batch(self, data_batch: List[Any]) -> str (abstractmethod)
    - filter_data(self, data_batch: List[Any], criteria: Optional[str]
    = None) -> List[Any] (デフォルト実装あり)
    - get_stats()（デフォルト実装あり）
    
    **Stream Processor :** 与えられたものによって挙動を変える
    
    - Data Stream型を受け取る
    - 同じ呼び方で処理
    - Streamごとの違いをポリモーフィズムで吸収する

**Example:**

```jsx
$> python3 data_stream.py
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected
=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...
Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed
Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction
All streams processed successfully. Nexus throughput optimal.
```

## ex2

- **概要**
    
    データ処理パイプラインの構築
    
    処理を複数のステージに分け、複雑なデータ変換を処理する
    
- **要件**

```jsx
$> python3 nexus_pipeline.py
=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===
Initializing Nexus Manager...
Pipeline capacity: 1000 streams/second
Creating Data Processing Pipeline...
Stage 1: Input validation and parsing
Stage 2: Data transformation and enrichment
Stage 3: Output formatting and delivery
=== Multi-Format Data Processing ===
Processing JSON data through pipeline...
Input: {"sensor": "temp", "value": 23.5, "unit": "C"}
Transform: Enriched with metadata and validation
Output: Processed temperature reading: 23.5°C (Normal range)
Processing CSV data through same pipeline...
Input: "user,action,timestamp"
Transform: Parsed and structured data
Output: User activity logged: 1 actions processed
Processing Stream data through same pipeline...
Input: Real-time sensor stream
Transform: Aggregated and filtered
Output: Stream summary: 5 readings, avg: 22.1°C
=== Pipeline Chaining Demo ===
Pipeline A -> Pipeline B -> Pipeline C
Data flow: Raw -> Processed -> Analyzed -> Stored
Chain result: 100 records processed through 3-stage pipeline
Performance: 95% efficiency, 0.2s total processing time
=== Error Recovery Test ===
Simulating pipeline failure...
Error detected in Stage 2: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed
Nexus Integration complete. All systems operational.
```
