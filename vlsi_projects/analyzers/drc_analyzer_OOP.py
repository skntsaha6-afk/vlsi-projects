"""This code will analyze DRCs : OOP based"""
from collections import Counter
from vlsi_projects.utils.parser_utils import file_reader_lines

class DRCAnalyzer():

    def __init__(self, lines: list[str]):
        """Initialize the drc_analyzer function"""
        self.lines = lines
        self.rules = []
    
    def extract_violations(self):
        """Extract the violation rules from the DRC report lines."""
        self.rules = []

        if not self.lines:
            return []
        
        for line in self.lines:
            if 'VIOLATION' in line:
                rule = line.split()
                if len(rule) > 1:
                    parts = rule[1]                
                    self.rules.append(parts)
        return self.rules
    
    def count_by_rule(self):
        """Count the number of violations for each rule."""
        _count = Counter(self.rules)
        return _count
    
    def most_common_violation(self):
        """Find the most common violation."""
        most_common_check = Counter(self.rules)

        return most_common_check.most_common(1) if len(most_common_check) > 0 else None

    def summary_report(self):
        """Generate a summary report of the DRC analysis."""
        if not self.rules:
            self.extract_violations()
            
        counts = self.count_by_rule()
        most_common = self.most_common_violation()

        # Return a dict for GPT access and stremlit can use it to display the report.
        return {
            "total_violations": len(self.rules),
            "violations_by_rule": dict(counts),
            "most_common_violation": most_common[0][0] if most_common else None,
            "most_common_violation_count": most_common[0][1] if most_common else None
        }
        
if __name__ == "__main__":
    lines = file_reader_lines("vlsi_projects/data/drc_report.txt")
    drc_analyzer = DRCAnalyzer(lines)
    summary = drc_analyzer.summary_report()
    print("DRC Analysis Report")
    print("-"*20)
    print("Violation by Rule:")
    print(f"Total Violation : {summary['total_violations']}")
    print("\nViolation by Rule:")
    for k ,v in summary['violations_by_rule'].items():
        print(f"{k} : {v}")
    if summary['most_common_violation']:
        print(f"Most common violation : {summary['most_common_violation']} with {summary['most_common_violation_count']} occurrences")


