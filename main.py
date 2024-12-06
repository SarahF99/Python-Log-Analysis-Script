import re
import csv
from collections import Counter

# Define constants
LOG_FILE = "sample.log"
OUTPUT_FILE = "log_analysis_results.csv"
FAILED_LOGIN_THRESHOLD = 10

# Function to parse log file
def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

# Function to count requests per IP
def count_requests_per_ip(logs):
    ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
    ip_counts = Counter()
    for log in logs:
        match = ip_pattern.match(log)
        if match:
            ip_counts[match.group(1)] += 1
    return ip_counts

# Function to find the most accessed endpoint
def find_most_accessed_endpoint(logs):
    endpoint_pattern = re.compile(r'"[A-Z]+ (\S+) HTTP')
    endpoint_counts = Counter()
    for log in logs:
        match = endpoint_pattern.search(log)
        if match:
            endpoint_counts[match.group(1)] += 1
    most_accessed = endpoint_counts.most_common(1)
    return most_accessed[0] if most_accessed else (None, 0)

# Function to detect suspicious activity
def detect_suspicious_activity(logs):
    suspicious_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+).*".*" 401.*Invalid credentials')
    failed_login_counts = Counter()
    for log in logs:
        match = suspicious_pattern.search(log)
        if match:
            failed_login_counts[match.group(1)] += 1
    return {ip: count for ip, count in failed_login_counts.items() if count > FAILED_LOGIN_THRESHOLD}

# Function to save results to CSV
def save_results_to_csv(ip_counts, most_accessed, suspicious_activities):
    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write requests per IP
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_counts.items():
            writer.writerow([ip, count])

        # Write most accessed endpoint
        writer.writerow([])  # Empty row for separation
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow(most_accessed)

        # Write suspicious activities
        writer.writerow([])  # Empty row for separation
        writer.writerow(["IP Address", "Failed Login Attempts"])
        for ip, count in suspicious_activities.items():
            writer.writerow([ip, count])

# Main function
def main():
    logs = parse_log(LOG_FILE)

    # Count requests per IP
    ip_counts = count_requests_per_ip(logs)

    # Find most accessed endpoint
    most_accessed = find_most_accessed_endpoint(logs)

    # Detect suspicious activities
    suspicious_activities = detect_suspicious_activity(logs)

    # Display results
    print("Requests per IP:")
    for ip, count in ip_counts.items():
        print(f"{ip: <20}{count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    for ip, count in suspicious_activities.items():
        print(f"{ip: <20}{count}")

    # Save results to CSV
    save_results_to_csv(ip_counts, most_accessed, suspicious_activities)
    print(f"\nResults saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

