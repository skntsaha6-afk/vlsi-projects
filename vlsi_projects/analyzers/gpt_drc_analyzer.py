from python_practice.vlsi_projects.utils.parser_utils import file_reader_lines
from python_practice.vlsi_projects.analyzers.drc_analyzer_OOP import DRCAnalyzer

from dotenv import load_dotenv
load_dotenv(override=True)
import os,sys
from openai import OpenAI

class DRCGPTAnalyzer():
    
    def __init__(self, report : dict) :
        self.report = report
        self.client = OpenAI()

    def response(self):
        """Convert the DRC report to a prompt for the GPT model"""
        gpt_reponse = self.client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = [
            {"role": "system", "content": "You are a Senior EDA Tools and Hardware Engineer." + " Analyze the DRC and suggest fixes"},
            {"role": "user", "content": f"Analyze the DRC report and suggest fixes : \n{self.report}"}
        ]
    )
        return gpt_reponse.choices[0].message.content
    

if __name__ == "__main__":
    lines = file_reader_lines("vlsi_projects/data/drc_report.txt")
    drc_analyzer = DRCAnalyzer(lines)
    report = drc_analyzer.summary_report()
    print("DRC Analysis Report")
    print("-"*20)
    print("\nGPT Analysis and Suggestions:")
    print(report)
    #print(DRCGPTAnalyzer()
    gpt_analyzer = DRCGPTAnalyzer(report)
    print(gpt_analyzer.response())