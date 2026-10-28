# Log Analyzer

A Python-based log analysis tool for detecting repeated failed login attempts and identifying potentially suspicious IP addresses.

## Description

This project is a simple cybersecurity log analyzer built with Python.

The tool reads a log file, finds failed login attempts, extracts the source IP addresses, counts the number of failed attempts for each IP, and generates a security report.

If an IP address reaches 3 or more failed login attempts, the tool generates a security alert.

This project was developed as a practical cybersecurity learning project to practice file handling, string parsing, lists, sets, tuples, functions, loops, and conditional logic.

## Features

- Reads login logs from a file
- Detects failed login attempts
- Extracts IP addresses
- Counts failed attempts per IP
- Generates a failed login report
- Detects potentially suspicious IP addresses
- Generates alerts for repeated failed login attempts

## Example Log

```text
Failed login from 192.168.1.10
Successful login from 192.168.1.20
Failed login from 192.168.1.10
Failed login from 10.0.0.5
Failed login from 192.168.1.10
Successful login from 10.0.0.5
Failed login from 10.0.0.5
```

## Example Output

```text
===== Failed Login Report =====
ip:10.0.0.5
Failed Attempts:2
ip:192.168.1.10
Failed Attempts:3
ALERT: Suspicious IP detected
```

## How It Works

```text
Log File
   ↓
Read Lines
   ↓
Find Failed Login
   ↓
Extract IP Address
   ↓
Count Failed Attempts
   ↓
Generate Report
   ↓
Detect Suspicious IP
   ↓
Generate Alert
```

## Technologies Used

- Python 3
- File Handling
- String Parsing
- Lists
- Sets
- Tuples
- Functions
- Loops
- Conditional Statements
- Linux / WSL
- Git
- GitHub

## Project Purpose

The purpose of this project is to practice:

1. Reading files with Python
2. Processing log data
3. Extracting information from strings
4. Counting repeated events
5. Using functions for reusable logic
6. Detecting suspicious activity
7. Building a basic security alert mechanism

## Security Note

This project is intended for educational purposes and authorized security analysis only.

Use it with log files that you own or have permission to analyze.

## Future Improvements

- Add timestamps to logs
- Detect multiple types of suspicious activity
- Add configurable alert thresholds
- Support larger log files
- Add CSV/JSON reporting
- Add severity levels
- Improve log parsing
- Add command-line arguments
- Add automated monitoring


