There are some core concepts with which data engineers should be familiar. These concepts underpin many of the workloads that data engineers must implement and support.

# Operational and analytical data

![](https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-operational-analytical-data.png)

`Operational data` is usually `transactional data` that is `generated` and `stored by applications`, often in a `relational` or `non-relational database`. Analytical data is data that has been `optimized for analysis and reporting`, often in a `data warehouse`.

One of `the core responsibilities` of a `data engineer` is to `design, implement, and manage solutions` that `integrate operational and analytical data sources or extract operational data from multiple systems`, `transform` it into `appropriate structures for analytics`, and `load it into` an `analytical data store` (usually referred to as ETL solutions).

# Streaming data
![](https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-stream-data.png)

Streaming data refers to perpetual sources of data that generate data values in real-time, often relating to specific events. Common sources of streaming data include `internet-of-things (IoT) devices` and `social media feeds`.

Data engineers often need to implement `solutions that capture real-time stream of data` and `ingest them into analytical data systems`, often `combining the real-time data` with other application data that is `processed in batches`

# Data pipelines
![](https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-data-pipeline.png)

Data pipelines are used to `orchestrate activities` that `transfer and transform data`. `Pipelines` are the primary way in which data engineers implement `repeatable extract, transform, and load (ETL)` `solutions that can be triggered based on a schedule or in response to events`

# Data lakes
![](https://learn.microsoft.com/en-us/training/wwl-data-ai/introduction-to-data-engineering-azure/media/4-data-lake.png)

A data lake is a `storage repository that holds large amounts of data in native, raw formats`. Data lake stores are `optimized` for `scaling to massive volumes` (`terabytes or petabytes`) of data. The data typically comes from multiple `heterogeneous sources`, and may be `structured, semi-structured, or unstructured`.

The idea with a data lake is to store everything in its original, untransformed state. This approach differs from a traditional data warehouse, which transforms and processes the data at the time of ingestion.

