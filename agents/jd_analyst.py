from crewai import Agent
from crewai import Task
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import GEMINI_API_KEY
llm = ChatGoogleGenerativeAI(model = "gemini-3.8-flash",
google_api_key = GEMINI_API_KEY)
def get_jd_analyst_agent():
    return Agent(
        role = "Job Description Analyst",
        goal = "Analyse job description and provide concise summaries of responsibilities, required skills, qualifications and experience.",
        backstory = "You are an experienced recruitment analyst who specialises in understanding job descriptions and identifying the most important requirements for candidates.",
        llm = llm,
        verbose = True
    )
def create_jd_analysis_task(agent, job_description):
    return Task(
        description = f"""Analyse the following job description: {job_description}
         Extract the following information:
        1. Job title
        2. Company name
        3. Required technical skills
        4. Required qualifications
        5. Required experience
        6. Key responsibilities
        7. Preferred skills
        8. Important keywords

        Provide a concise and accurate analysis.
        Do not invent information that is not present in the job description.
        """,
        expected_output =""" A structured Markdown report containing:

        # Job Description Analysis

        ## Job Title
        ## Company
        ## Required Technical Skills
        ## Qualifications
        ## Experience
        ## Key Responsibilities
        ## Preferred Skills
        ## Important Keywords
        """,
        agent = agent,
        output_file = "/data/report.md"
    )
    