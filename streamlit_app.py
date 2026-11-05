
import streamlit as st
from usajobs_api import fetch_usa_jobs
from orchestrator import run_pipeline

st.set_page_config(page_title="AI Job Hunt Assistant", layout="centered")

st.title("Find your perfect job!")
st.markdown(
    "Use AI agents to analyze jobs, tailor your resume, "
    "and write outreach messages — all from one interface."
)

st.divider()
st.subheader("Find your next opportunity!")

keyword = st.text_input("Job Keyword", "Software Engineer")
location = st.text_input("Location", "Washington, DC")
resume_text = st.text_area("Paste your resume", height=200)
user_bio = st.text_area(
    "Short Bio (for outreach tone)",
    "I am a computer science graduate interested in software engineering."
)

# Fetch jobs
if st.button("Run Job Hunt Assistant"):

    if not resume_text.strip():
        st.warning("Please paste your resume before searching.")

    else:
        with st.spinner("Fetching job postings..."):
            job_posts = fetch_usa_jobs(
                keyword,
                location,
                results_per_page=5
            )

        if not job_posts:
            st.error("No job postings found.")

        else:
            st.session_state["job_posts"] = job_posts
            st.session_state["resume_text"] = resume_text
            st.session_state["user_bio"] = user_bio

# Display fetched jobs
if "job_posts" in st.session_state:

    st.divider()
    st.subheader("Available Job Postings")

    for i, job in enumerate(st.session_state["job_posts"]):

        details = job["MatchedObjectDescriptor"]

        title = details.get("PositionTitle", "Unknown Position")
        agency = details.get("OrganizationName", "Unknown Agency")

        st.checkbox(
            f"{title} — {agency}",
            key=f"selected_job_{i}"
        )

    # Apply to selected jobs
    if st.button("Apply to Selected Job"):

        selected_jobs = []

        for i, job in enumerate(st.session_state["job_posts"]):
            if st.session_state.get(f"selected_job_{i}", False):
                selected_jobs.append(job)

        if not selected_jobs:
            st.warning("Please select at least one job.")

        else:
            for job in selected_jobs:

                details = job["MatchedObjectDescriptor"]
                title = details.get("PositionTitle", "Unknown Position")

                st.divider()
                st.subheader(title)

                with st.spinner(f"Analyzing {title}..."):

                    result = run_pipeline(
                        job,
                        st.session_state["resume_text"],
                        st.session_state["user_bio"]
                    )

                st.markdown("### Agent Results")
                st.markdown(str(result))
