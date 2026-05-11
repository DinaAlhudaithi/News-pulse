# News Pulse Big Data Challenge

This project implements a simplified real-time News Pulse big-data pipeline using Python and PySpark.

## Features
- Reads news headline data from a CSV file
- Simulates news ingestion using batch-style processing
- Counts headlines by news source
- Extracts trending keywords from headlines
- Groups headlines by time window
- Displays results using Spark tables

## Technologies Used
- Python
- PySpark
- Spark SQL

## Files
- news_pulse.py: Main PySpark script
- mock_news.csv: Sample news headline dataset
- requirements.txt: Required Python package
- README.md: Project explanation

## How to Run

```bash
pip install pyspark
python news_pulse.py
