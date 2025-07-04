# jobcycle_agent/langgraph_config.py

from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from agentic_workflow import collect_profile, extract_skills, match_jobs

# Define the state schema
class JobState(TypedDict):
    profile_data: str
    skills: List[str]
    job_matches: List[str]

# Define the flow graph
def build_job_graph():
    builder = StateGraph(JobState)

    builder.add_node("collect_profile", collect_profile)
    builder.add_node("extract_skills", extract_skills)
    builder.add_node("match_jobs", match_jobs)
    builder.set_entry_point("collect_profile")

    builder.add_edge("collect_profile", "extract_skills")
    builder.add_edge("extract_skills", "match_jobs")
    builder.add_edge("match_jobs", END)

    return builder.compile()
