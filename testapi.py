from usajobs_api import fetch_usa_jobs

jobs = fetch_usa_jobs("IT Specialist", "Washington, DC")

print("\nFinal Result:")
print("Total jobs:", len(jobs))

if jobs:
    job = jobs[0]["MatchedObjectDescriptor"]

    print("Job Title:", job.get("PositionTitle"))
    print("Organization:", job.get("OrganizationName"))