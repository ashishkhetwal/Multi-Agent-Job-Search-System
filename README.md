# AI Job Hunt Assistant — Version 1.0

An AI-powered job application assistant built using Python, Streamlit, CrewAI, and Google Gemini API. The application helps users streamline parts of the job search and application process by analyzing job descriptions and generating personalized application materials.

**Current Release:** Version 1.0

## Features

- **Job Search:** Fetches job postings using the USAJOBS API based on job titles and locations.
- **Job Description Analysis:** Uses specialized AI agents to analyze job descriptions and identify relevant requirements.
- **Resume Tailoring:** Generates resume content tailored to specific job descriptions.
- **Cover Letter Generation:** Creates customized cover letters for selected job opportunities.
- **Professional Messaging:** Generates personalized outreach messages suitable for LinkedIn or email.
- **Multiple Job Selection:** Allows users to select multiple job postings and process them through the agent workflow.
- **Application Tracking:** Records job application information in a CSV file.
- **Cover Letter Export:** Supports exporting individual cover letters.

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **AI Agent Framework:** CrewAI
- **LLM Integration:** Google Gemini API
- **Job Data:** USAJOBS API
- **Data Storage:** CSV

## Project Structure

```text
AI-Job-Hunt-Assistant/
│
├── agents/
│   ├── jd_analyst.py
│   ├── messaging_agent.py
│   └── resume_cl_agent.py
│
├── data/
│   ├── applications_log.csv
│   └── sample_resume.txt
│
├── utils/
│   ├── config.py
│   ├── tracking.py
│   └── __init__.py
│
├── orchestrator.py
├── streamlit_app.py
├── usajobs_api.py
├── testapi.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ashishkhetwal/AI-Job-Hunt-Assistant.git
cd AI-Job-Hunt-Assistant
```

### 2. Install dependencies

Install the required Python packages:

```bash
pip install streamlit crewai langchain-google-genai python-dotenv requests
```

### 3. Configure API keys

Create a `.env` file inside the `utils/` directory:

```env
USAJOBS_API_KEY=your_usajobs_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder values with your own API keys.



### 4. Run the application

```bash
streamlit run streamlit_app.py
```

Open the local URL displayed in your terminal to access the application.

## How It Works

1. Users search for job opportunities using job titles and locations.
2. The application retrieves relevant postings through the USAJOBS API.
3. Users select one or more job postings.
4. CrewAI coordinates specialized AI agents to analyze job descriptions and generate tailored application materials.
5. Generated content is presented through the Streamlit interface.
6. Application information is recorded in a CSV file.

## Roadmap — Future Improvements

The following features are planned for future releases and are not yet implemented.


- **Resume–Job Match Engine:** Analyze resumes against job descriptions to calculate a relevance score, identify missing skills, and suggest targeted improvements.
- **Intelligent Job Recommendation System:** Recommend and rank job opportunities based on a user's skills, experience, preferences, and resume profile.
- **AI Mock Interview System:** Generate role-specific technical and behavioral questions, conduct interactive interview sessions, and evaluate responses with personalized feedback.
- and any more updates
## Current Status

Version 1.0 provides the foundational job search and AI-powered application assistance workflow. Future versions aim to evolve the project into a more comprehensive AI-driven career and job search platform.

- GitHub: [ashishkhetwal](https://github.com/ashishkhetwal)
- LinkedIn: [Ashish Khetwal](https://www.linkedin.com/in/ashish-khetwal-a22671303/)
