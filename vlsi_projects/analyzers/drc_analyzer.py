from vlsi_projects.utils.parser_utils import file_reader_lines

def count_by_rule(rules: list[str]):
    counts = {}
    for rule in rules:
        counts[rule] = counts.get(rule,0)+1
    return counts

def most_common_violation(counts):
    return max(counts,key=counts.get)

def extract_violations(lines: list[str]):
    if not lines:
        return []
    rules = []
    for line in lines:
        if "VIOLATION" in line:
            rule = line.split()[1]
            rules.append(rule)
    return rules

def main():    
    lines = file_reader_lines("vlsi_projects/data/drc_report.txt")
    rules = extract_violations(lines)
    counts = count_by_rule(rules)
    print("DRC Analysis Report")
    print("-"*20)
    print("Violation by Rule:")
    print(f"Total Violation : {len(rules)}")
    print("\nViolation by Rule:")
    for k,v in counts.items():
        print(f"{k} : {v}")
    print(f"Most common violation : {max(counts,key=counts.get)}")

if __name__ == "__main__":
    main()