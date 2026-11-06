from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=GEMINI_API_KEY
)


def get_resume_cl_agent():
    return Agent(
        role='Resume and Cover Letter Writer',
        goal=(
            'Create tailored, professional resumes and compelling cover letters '
            'that align a candidate’s qualifications, skills, and experience '
            'with the requirements of a specific job description.'
        ),
        backstory=(
            'You are an experienced career consultant and professional resume '
            'writer with expertise in recruitment, applicant tracking systems (ATS), '
            'and job application optimization. You understand how recruiters '
            'evaluate candidates and how to highlight relevant skills, projects, '
            'achievements, and experience. You write clear, concise, and impactful '
            'resumes and cover letters without inventing or exaggerating '
            'the candidate’s qualifications.'
        ),
        llm=llm,
        verbose=True
    )


def create_resume_cl_task(agent, job_summary, resume_text):
    return Task(
        description=(
            f"Candidate's Resume:\n{resume_text}\n\n"
            f"Government Job Description:\n{job_summary}\n\n"
            "Perform the following tasks:\n"
            "1. Tailor the candidate's resume to highlight relevant "
            "qualifications, skills, and experience that match the job requirements.\n"
            "2. Generate a personalized, professional cover letter explaining "
            "why the candidate is suitable for this government position.\n\n"
            "Ensure both documents are clear, professional, and ATS-friendly. "
            "Do not fabricate qualifications, skills, or experience. "
            "Use only the information provided."
        ),
        expected_output="""Generate exactly two sections using these markers:

<<RESUME_SUMMARY>>
A tailored 3-5 sentence resume summary.

<<COVER_LETTER>>
A personalized, professional cover letter.

Preserve both markers exactly. Do not omit them.""",
        agent=agent,
        output_file="/data/resume_agent_output.txt"
    )