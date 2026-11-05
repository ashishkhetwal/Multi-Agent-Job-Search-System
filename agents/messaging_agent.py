from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import GEMINI_API_KEY
llm = ChatGoogleGenerativeAI(model = 'gemini-3.8-flash',
google_api_key = GEMINI_API_KEY)
def get_messaging_agent():
    return Agent(
        role = "Messaging Agent",
        verbose = True,
        llm = llm,
        goal=(
            "Write personalized, concise, and professional outreach messages "
            "that help job seekers connect with recruiters, hiring managers, "
            "and industry professionals to explore job and networking opportunities."
        ),
        backstory = (
             "You are an experienced professional networking and career communication "
    "specialist. You understand LinkedIn outreach, recruiter communication, "
    "cold messaging, and professional relationship building. You know how to "
    "craft engaging messages that highlight a candidate's relevant skills, "
    "experience, and interests while maintaining a natural and respectful tone. "
    "You avoid generic templates, exaggerated claims, and overly promotional language."
        )
    )
def create_messaging_task(agent, job_summary, user_bio, agency_name, resume_text):
    return Task(
        description=(
        f"Candidate's Resume:\n{resume_text}\n\n"
            f"Job Description:\n{job_summary}\n\n"

            "Write a brief, professional, and personalized outreach "
            "message expressing the candidate's interest in this job. "
            "Highlight relevant skills and experience from the resume. "
            "Keep the message concise, natural, and engaging. "
            "Do not invent qulifications or experience."
        ),
        expected_output=(
            "A personalized, professional outreach message of fewer than "
            "150 words, suitable for sending through LinkedIn or email. "
             "The message should express interest in the job and highlight "
            "relevant candidate qualifications."
        ),
        agent = agent

    )