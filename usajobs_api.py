import requests
from utils.config import USAJOBS_API_KEY

def fetch_usa_jobs(keyword, location="remote", results_per_page=5):

    url = "https://data.usajobs.gov/api/Search"

    headers = {
        "Host": "data.usajobs.gov",
        "User-Agent": "ashishkhetwal21@gmail.com",
        "Authorization-Key": USAJOBS_API_KEY
    }

    params = {
        "Keyword": keyword,
        "LocationName": location,
        "ResultsPerPage": results_per_page,
        "Page": 1
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()

            jobs = data.get("SearchResult", {}).get(
                "SearchResultItems", []
            )

            print("Jobs Found:", len(jobs))
            return jobs

        else:
            print("API Error:", response.status_code)
            print("Response:", response.text[:1000])
            return []

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return []