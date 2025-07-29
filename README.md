# 🧾 SSH Log Parser (Python)

A simple Python script to parse and filter SSH log entries from a tab-separated log file. It displays clear, formatted output with options to filter logs by result status such as `SUCCESS`, `FAILURE`, or `UNDETERMINED`.

## 📌 Features

- Reads logs from a `.txt.log` file
- Converts timestamps to human-readable format
- Filters entries based on result:
  - ✅ SUCCESS
  - ❌ FAILURE
  - ❓ UNDETERMINED
- Displays tabular data with details:
  - Time
  - Source & Destination IP/Port
  - Connection result
  - Direction
  - Client and Server version
