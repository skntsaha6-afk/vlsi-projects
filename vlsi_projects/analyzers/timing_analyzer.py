from vlsi_projects.utils.parser_utils import file_reader_lines

def count_violations(slack_values):
    return sum(1 for slack in slack_values if slack < 0)

def find_worst_slack(slack_values):
    if not slack_values:
        return None
    return min(slack_values)

def total_path_count(slack_values):
    return len(slack_values)

def violation_path(slack_values):
    return [slack for slack in slack_values if slack < 0]

def top_worst_path(slack_values,n):
    return sorted(slack_values)[:n]

def extract_timing_slacks(lines):
        slack = []
        for line in lines:
            if "slack" in line.lower():
                parts = line.split()
                for part in parts:  
                    try:
                        float_part = float(part)
                        slack.append(float_part)
                    except ValueError:
                        pass
        return slack




#print(analyze_timing_report("vlsi_projects/data/timing_report.txt"))

def main():
    report_path = "vlsi_projects/data/timing_report.txt"
    slack = extract_timing_slacks(file_reader_lines(report_path))
    print("Timing Analysis Report:")
    print(slack)
    print('Violations:',count_violations(slack))
    print('Worst Slack:', find_worst_slack(slack))
    print('Total Paths:', total_path_count(slack))
    print('Violation Paths:', violation_path(slack))
    print('Top 3 Worst Paths:', top_worst_path(slack, 5))


if __name__ == "__main__":
    main()
