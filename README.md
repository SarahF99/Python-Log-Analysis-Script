# Python-Log-Analysis-Script
# Log Analysis Script

## Overview
This Python script analyzes log files to extract key information such as:
1. Number of requests made by each IP address.
2. The most frequently accessed endpoint.
3. Detection of suspicious activity, specifically brute-force login attempts.

It outputs the results both in the terminal and as a structured CSV file.

---

## Features

### 1. **Count Requests Per IP Address**
The script extracts all IP addresses from the log file, counts the requests made by each, and displays the results sorted in descending order of request count.

Example Output:
```
Requests per IP:
192.168.1.1          7
203.0.113.5          12
10.0.0.2             6
198.51.100.23        7
192.168.1.100        9
```

### 2. **Most Frequently Accessed Endpoint**
The script identifies the endpoint (e.g., URLs or resource paths) that was accessed the most number of times.

Example Output:
```
Most Frequently Accessed Endpoint:
/home (Accessed 5 times)
```

### 3. **Detect Suspicious Activity**
The script identifies IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts).

Example Output:
```
Suspicious Activity Detected:
203.0.113.5          12
```

---

## CSV Output
The results are saved to `log_analysis_results.csv` with the following structure:

### Requests Per IP:
```csv
IP Address,Request Count
192.168.1.1,7
203.0.113.5,12
10.0.0.2,6
198.51.100.23,7
192.168.1.100,9
```

### Most Accessed Endpoint:
```csv
Most Accessed Endpoint,Access Count
/home,5
```

### Suspicious Activity:
```csv
IP Address,Failed Login Attempts
203.0.113.5,12
```

---

## Usage

### Prerequisites
- Python 3.x
- Sample log file (`sample.log`)

### Steps to Run the Script
1. Save the script as `log_analysis.py`.
2. Ensure the log file `sample.log` is in the same directory.
3. Run the script:
   ```bash
   python log_analysis.py
   ```
4. View the results in the terminal and in the generated CSV file (`log_analysis_results.csv`).

---

## Sample Log File
The script uses the following log format for analysis:
```
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
...
```

Ensure the log file follows this structure for accurate analysis.

---

## Evaluation Criteria
1. **Functionality**: The script processes the log file correctly and fulfills all requirements.
2. **Code Quality**: The script is modular, well-organized, and adheres to Python best practices.
3. **Performance**: The script efficiently handles large log files.
4. **Output**: The output is correctly formatted in both the terminal and the CSV file.

---

## Output Example
### Terminal Output:
```
Requests per IP:
192.168.1.1          7
203.0.113.5          12
10.0.0.2             6
198.51.100.23        7
192.168.1.100        9

Most Frequently Accessed Endpoint:
/home (Accessed 5 times)

Suspicious Activity Detected:
203.0.113.5          12
```

### CSV Output (`log_analysis_results.csv`):
#### Requests Per IP:
```csv
IP Address,Request Count
192.168.1.1,7
203.0.113.5,12
10.0.0.2,6
198.51.100.23,7
192.168.1.100,9
```

#### Most Accessed Endpoint:
```csv
Most Accessed Endpoint,Access Count
/home,5
```

#### Suspicious Activity:
```csv
IP Address,Failed Login Attempts
203.0.113.5,12
```

---

## Notes
- Adjust the `FAILED_LOGIN_THRESHOLD` constant in the script to change the detection sensitivity for suspicious activities.
- The script can be extended to include additional analysis or handle more complex log formats.

---

## License
This project is open-source and available for modification and distribution under the MIT License.


