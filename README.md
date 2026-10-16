# Simulated Device Monitoring and Alert System
 
**Student Name:** Sean D. Dela Cruz
**Student Number:** 2600718
**Section:** 1CPE-A
 
## Project Description
This program monitors simulated device temperature readings for a computer engineering laboratory. It classifies each reading as NORMAL, WARNING, or CRITICAL based on strict temperature thresholds and computes comprehensive numerical statistics and overall device status.
 
## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings
 
## Requirements
- Python 3 (no external packages)
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)
 
## Sample Output
```
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter your choice: 3

READING CLASSIFICATION
----------------------
28 °C -> NORMAL
31 °C -> WARNING
35 °C -> WARNING
37 °C -> CRITICAL
29 °C -> NORMAL
```
 
## Test Cases
I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md.
 
## Known Limitations
- Data modifications only exist during the runtime session; readings reset upon restarting the script.
 
## Reflection
Building this integrative project allowed me to combine modular programming, parameter passing, input validation, and manual numerical processing into a unified program. The most challenging aspect was making sure boundary checks for the WARNING category (30 and 35 inclusive) operated accurately. Debugging using isolated functions made troubleshooting straightforward.