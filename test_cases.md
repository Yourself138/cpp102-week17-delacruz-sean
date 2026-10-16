# Test Cases – Simulated Device Monitoring and Alert System
 
Tested by: Sean Dela Cruz        Date: October 15, 2026
 
| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Five readings displayed correctly | Pass |
| TC02 | Choose 2, enter 33 | "Reading added successfully" | Reading added successfully | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Invalid input. Enter a whole number only. | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Invalid input. Enter a whole number only. | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Invalid input. Enter a whole number only. | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | Classified as WARNING | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | Classified as WARNING | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Summary matched expected values precisely | Pass |
| TC09 | Enter 9 | Error message; menu shown again | Error displayed, menu reloaded | Pass |
| TC010 | Choose 5 | Exit message; program ends | Program terminated | Pass |
 
## Bugs Found and Fixed
- Initially, boundary checking for 35 °C was missing an inclusive equals sign (`<=`), which misclassified 35 °C as CRITICAL. This was resolved by updating the condition in `classify_reading()` to use `reading <= 35`, ensuring both 30 and 35 fall correctly under WARNING.
