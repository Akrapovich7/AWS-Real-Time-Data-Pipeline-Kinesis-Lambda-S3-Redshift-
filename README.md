# AWS-Real-Time-Data-Pipeline-Kinesis-Lambda-S3-Redshift-
Stream live data → process it → store it → analyze it in near real-time.
Architecture Overview
Data Source: fake data generator(sensors)

Kinesis Data Stream: collect real-time data.

AWS Lambda: process each record (cleaning, validation).

S3 Bucket: store raw and processed data.

Redshift: store processed data for querying.
