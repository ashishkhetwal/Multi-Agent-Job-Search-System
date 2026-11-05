
from crewai import Crew, Process
from agents.jd_analyst import get_jd_analyst_agent, create_jd_analysis_task
from utils.tracking import log_application, save_cover_letter_file
from agents.resume_cl_agent import get_resume_cl_agent, create_resume_cl_task
from agents.messaging_agent import get_messaging_agent, create_messaging_task


def extract_between_markers(text, start_marker, end_marker):
    try:
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker)
        return text[start:end].strip()
    except ValueError:
        return ""


def run_pipeline(job, resume_content, user_bio):

    job_details = job['MatchedObjectDescriptor']
    job_summary = job_details['UserArea']['Details']['JobSummary']

    if 'OrganizationName' in job_details:
        agency_name = job_details['OrganizationName']
    else:
        agency_name = 'Unknown Agency'

    if 'PositionTitle' in job_details:
        job_title = job_details['PositionTitle']
    else:
        job_title = 'Unknown Position'

    # Initialize agents
    messaging_agent = get_messaging_agent()
    jd_analyst = get_jd_analyst_agent()
    resume_writer = get_resume_cl_agent()

    # Create tasks
    messaging_task = create_messaging_task(
        messaging_agent, job_summary, user_bio, agency_name, resume_content
    )

    jd_task = create_jd_analysis_task(jd_analyst, job_summary)

    resume_task = create_resume_cl_task(
        resume_writer, job_summary, resume_content
    )

    crew = Crew(
        agents=[jd_analyst, resume_writer, messaging_agent],
        tasks=[jd_task, resume_task, messaging_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    # Extract resume agent output
    resume_output = str(resume_task.output)

    # Extract resume summary
    resume_summary = extract_between_markers(
        resume_output, "<<RESUME_SUMMARY>>", "<<COVER_LETTER>>"
    )

    # Extract cover letter (everything after its marker)
    cover_letter = resume_output.split("<<COVER_LETTER>>", 1)[-1].strip()

    # Log application details
    log_application(job_title, agency_name, resume_summary)

    # Save cover letter
    save_cover_letter_file(job_title, cover_letter)

    return result
