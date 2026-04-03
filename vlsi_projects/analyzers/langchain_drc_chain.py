from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from python_practice.vlsi_projects.analyzers.drc_analyzer_OOP import DRCAnalyzer
from python_practice.vlsi_projects.utils.parser_utils import file_reader_lines
from dotenv import load_dotenv
import sys,os,json


load_dotenv(override=True)

#print(os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0, #always 0 fr EDA Analysis
        max_completion_tokens=1000
)


prompt = ChatPromptTemplate.from_messages([

    ('system', '''You are a Senior VLSI Engineer at Intel.
    You have 10 years of DRC debug experience.
    Analyze DRC violations and return raw JSON only.
    No markdown. No code blocks. Raw JSON only.
    Format:
    {{
    "violations": [
    {{"rule": str, "severity": "Critical|High|Medium|Low",
    "count": int, "root_cause": str, "fix": str}}
    ],
    "priority_fix": str,
    "fix_sequence": [str],
    "estimated_fix_time": str
    }}'''),

    ('user', 'Analyze this DRC report and suggest fixes:\n{drc_report}')
])

parser = JsonOutputParser()

#The chain
chain = prompt | llm | parser

#building class for langChainAnalyzer

class langchainDRCAnalyzer():

    """DRC Analyzer using LangChain chain."""

    def analyzer(self, report: dict) -> dict:
        """Run the DRC chain on a report dict."""

        return chain.invoke({'drc_report': str(report)})
    

if __name__ == '__main__':
    lines = file_reader_lines("vlsi_projects/data/drc_report.txt")
    drc_analyzer = DRCAnalyzer(lines)
    summary = drc_analyzer.summary_report()

    lc = langchainDRCAnalyzer()
    result = lc.analyzer(summary)

    print('LangChain Chain Result:')
    print(result)
    print()
    print(f'Priority Fix: {result["priority_fix"]}')
    print(f'Violations found: {len(result["violations"])}')