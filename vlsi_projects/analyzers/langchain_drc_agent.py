"""
Week 6 — LangChain Agent with 3 EDA Tools
Agent autonomously reads DRC report, classifies severity, suggests fixes
"""


from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from python_practice.vlsi_projects.analyzers.drc_analyzer_OOP import DRCAnalyzer
from python_practice.vlsi_projects.utils.parser_utils import file_reader_lines
from dotenv import load_dotenv

load_dotenv(override=True)


llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
        max_completion_tokens=1000
)

# ■■ TOOL 1 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@tool
def read_drc_report(filepath: str) -> dict:
    
    '''Reads a DRC report file and extracts all violations.
        Returns a dict with total_violations and violations_by_rule.
        Use this first before analyzing violations.
    '''

    lines = file_reader_lines(filepath)
    drc_analyzer = DRCAnalyzer(lines)

    return drc_analyzer.summary_report()

# ■■ TOOL 2 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@tool
def classify_violation_severity(rule_name: str, count: int) ->str:
    '''Classifies the severity of a DRC violation based on rule name and count.
    Returns: Critical, High, Medium, or Low.
    Use this after reading the DRC report to prioritize fixes.'''
    critical_rules = ['SHORT', 'OPEN', 'ESD', 'ANTENNA']
    high_rules = ['METAL1_SPACING', 'METAL2_SPACING', 'VIA_ENCLOSURE']

    if any(r in rule_name.upper() for r in critical_rules):
        return 'Critical'
    
    elif any(r in rule_name.upper() for r in high_rules) or count > 10:
        return 'High'
    elif count > 5:
        return 'Medium'
    return 'Low'

# ■■ TOOL 3 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@tool
def suggest_fix_for_rule(rule_name: str, severity: str)->str:
    '''Suggests a specific fix for a DRC violation rule.
        Use this after classifying severity to get actionable fix recommendations.
        Returns a specific engineering action to resolve the violation.'''


    fixes = {
            'METAL1_SPACING': 'Increase spacing between Metal1 wires to minimum rule value.',
            'METAL2_SPACING': 'Reroute Metal2 traces or increase spacing to DRC minimum.',
            'VIA_OVERLAP': 'Adjust via placement to ensure full overlap with metal layers.',
            'METAL1_WIDTH': 'Widen Metal1 wire to meet minimum width requirement.',
            }
    default = f'Review {rule_name} in DRC manual. Adjust layout to meet rule constraints.'
    return fixes.get(rule_name, default)      


tools = [read_drc_report, classify_violation_severity, suggest_fix_for_rule]

# Build agent graph (LangChain 1.2.x)
system_prompt = """You are a Senior EDA Debug Engineer at Intel with 10 years experience.
Analyze DRC reports step by step using the available tools and return concise fixes."""

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
)


def run():
    state = agent.invoke({
        "messages": [
            HumanMessage(content="""Analyze the DRC report at vlsi_projects/data/drc_report.txt.
For each violation: classify severity and suggest a fix.""")
        ]
    })
    messages = state.get("messages", [])
    final_msg = next((m for m in reversed(messages) if isinstance(m, AIMessage)), None)
    print('\nFINAL ANSWER:')
    print(final_msg.content if final_msg else state)

if __name__ == '__main__':
    run()
