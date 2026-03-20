from python_practice.vlsi_projects.utils.parser_utils import file_reader_lines
from python_practice.vlsi_projects.analyzers.drc_analyzer_OOP import DRCAnalyzer

from dotenv import load_dotenv
load_dotenv(override=True)
import os,sys,json
from openai import OpenAI


class DRCGPTAnalyzer():
    
    def __init__(self, report : dict):
        self.report = report
        self.client = OpenAI()

    def response(self):
        """Convert the DRC report to a prompt for the GPT model"""
        gpt_reponse = self.client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = [
            {"role": "system", "content": 
                        """ 
                        You are a Senior EDA Tools and Hardware Engineer.
                        Analyze the DRC and suggest fixes. 
                        
                        Always respond in JSON format.
                        No Markdown.  
                        No Code Blocks. 
                        Raw JSON only. 
                        
                    {
                        "violations": [
                        {
                        "rule": "rule name",
                        "severity": "High|Medium|Low",
                        "count": number,
                        "fix": "specific action to take"
                        }
                        ],
                        "priority_fix": "most urgent rule to fix first",
                        "estimated_fix_time": "time estimate"
                        }
                        Do not add any text outside the JSON.
                        """
                        
            },
            {"role": "user", "content": 
                        f"""
                            Analyze the DRC report and suggest fixes. 
                            Focus only on Metal Violations.                          
                            LOG: \n{self.report}
                        """
            }
        ]
    )
        content = gpt_reponse.choices[0].message.content
        with open("prompt_response.txt","w") as f:
            f.write(content)
        return content
    
    def validate_response(self,content):
        try : 
            parsed = json.loads(content)
            print("GPT JSON Validated Successfully!") 
            return parsed               
        except json.JSONDecodeError:
            print("Warning : GPT did not return valid JSON")
            return content


if __name__ == "__main__":
    lines = file_reader_lines("vlsi_projects/data/drc_report.txt")
    drc_analyzer = DRCAnalyzer(lines)
    report = drc_analyzer.summary_report()
    print("DRC Analysis Report")
    print("-"*20)
    print("\nGPT Analysis and Suggestions:")
    #print(report)
    #print(DRCGPTAnalyzer()
    gpt_analyzer = DRCGPTAnalyzer(report)
    gpt_reponse = gpt_analyzer.response()
    print(gpt_reponse)
    print(gpt_analyzer.validate_response(gpt_reponse))