# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Function to fetch job postings
# def fetch_jobs(keywords, location, geo_id, job_id, total_jobs):
#     l = []
#     k = []
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
#     base_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keywords}&location={location}&geoId={geo_id}&currentJobId={job_id}&start={{}}'
#     #https://www.linkedin.com/jobs/search/?currentJobId=3917482411&distance=25&f_TPR=r604800&geoId=105080838&keywords=financial%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
    
#     for i in range(0, (total_jobs // 25) + 1):
#         res = requests.get(base_url.format(i * 25), headers=headers)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         all_jobs_on_this_page = soup.find_all("li")
#         for job in all_jobs_on_this_page:
#             job_data = job.find("div", {"class": "base-card"})
#             if job_data:
#                 job_id = job_data.get('data-entity-urn')
#                 if job_id:
#                     l.append(job_id.split(":")[3])

#     # Fetch detailed job info
#     for j in l:
#         target_url = f'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{j}'
#         resp = requests.get(target_url, headers=headers)
#         soup = BeautifulSoup(resp.text, 'html.parser')
        
#         o = {}
#         o["company"] = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt') if soup.find("div", {"class": "top-card-layout__card"}) else None
#         o["job-title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip() if soup.find("div", {"class": "top-card-layout__entity-info"}) else None
#         o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace("Seniority level", "").strip() if soup.find("ul", {"class": "description__job-criteria-list"}) else None
        
#         k.append(o)

#     return pd.DataFrame(k)

# st.title('LinkedIn Job Scraper')

# # User Inputs
# keywords = st.text_input('Keywords', 'Financial Analyst')
# location = st.text_input('Location', 'New York')
# geo_id = st.text_input('Geo ID', '105080838')
# job_id = st.number_input('Current Job ID', min_value=0, value=3917482411, step=1)
# total_jobs = st.number_input('Total Jobs to Fetch', min_value=25, max_value=100, value=25, step=25)

# if st.button('Fetch Jobs'):
#     df = fetch_jobs(keywords, location, geo_id, job_id, total_jobs)
#     if not df.empty:
#         st.dataframe(df)
#     else:
#         st.write("No jobs found.")


# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Function to fetch job postings
# def fetch_jobs(keywords, location, geo_id, job_id, total_jobs):
#     l = []
#     k = []
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
#     base_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keywords}&geoId={geo_id}&f_TPR=r604800&currentJobId={job_id}&start={{}}'
    
#     for i in range(0, (total_jobs // 25) + 1):
#         res = requests.get(base_url.format(i * 25), headers=headers)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         all_jobs_on_this_page = soup.find_all("li")
#         for job in all_jobs_on_this_page:
#             job_data = job.find("div", {"class": "base-card"})
#             if job_data:
#                 job_id = job_data.get('data-entity-urn')
#                 if job_id:
#                     l.append(job_id.split(":")[3])

#     # Fetch detailed job info
#     for j in l:
#         target_url = f'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{j}'
#         resp = requests.get(target_url, headers=headers)
#         soup = BeautifulSoup(resp.text, 'html.parser')
        
#         o = {}
#         o["company"] = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt') if soup.find("div", {"class": "top-card-layout__card"}) else None
#         o["job-title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip() if soup.find("div", {"class": "top-card-layout__entity-info"}) else None
#         o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace("Seniority level", "").strip() if soup.find("ul", {"class": "description__job-criteria-list"}) else None
#         o["description"] = soup.find("div", {"class": "show-more-less-html__markup"}).get_text(strip=True) if soup.find("div", {"class": "show-more-less-html__markup"}) else "No description available"
#         o["salary"] = soup.find("li", {"class": "job-details-jobs-unified-top-card__job-insight job-details-jobs-unified-top-card__job-insight--highlight"}).get_text(strip=True) if soup.find("li", {"class": "job-details-jobs-unified-top-card__job-insight job-details-jobs-unified-top-card__job-insight--highlight"}) else "Salary not specified"
#         o["date_posted"] = soup.find("span", {"class": "posted-time-ago__text"}).get_text(strip=True) if soup.find("span", {"class": "posted-time-ago__text"}) else "Date not available"
#         o["link"] = f'https://www.linkedin.com/jobs/view/{j}'
#         o["skills"] = [skill.get_text(strip=True) for skill in soup.find_all("span", {"class": "skill"})]  # Assuming skills are listed in <span class="skill">
#         o["job_type"] = soup.find("span", {"class": "job-type"}).get_text(strip=True) if soup.find("span", {"class": "job-type"}) else "Job type not specified"

#         k.append(o)
#         print (o)

#     return pd.DataFrame(k)
# #https://www.linkedin.com/jobs/search/?currentJobId=3878756337&distance=25&f_SB2=3&f_TPR=r604800&geoId=105080838&keywords=financial%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
# #https://www.linkedin.com/jobs/search/?currentJobId=3917979649&distance=25&f_SB2=3&f_TPR=r86400&geoId=105080838&keywords=financial%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
# #https://www.linkedin.com/jobs/search/?currentJobId=3891916908&distance=25&f_SB2=3&f_TPR=r2592000&geoId=105080838&keywords=financial%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true

# # Streamlit interface setup
# st.title('LinkedIn Job Scraper')
# keywords = st.text_input('Keywords', 'Financial Analyst')
# location = st.text_input('Location', 'New Jersey, United States')
# geo_location_id = {"New Jersey" :101651951, "New York Metropolitan Area": 90000070, "New York City": 102571732}
# geo_id = st.radio("Select an option", geo_location_id.keys())
# job_id = st.number_input('Current Job ID', min_value=0, value=3917482411, step=1)
# total_jobs = st.number_input('Total Jobs to Fetch', min_value=25, max_value=100, value=25, step=25)

# if st.button('Fetch Jobs'):
#     df = fetch_jobs(keywords, location, geo_id, job_id, total_jobs)
#     if not df.empty:
#         st.dataframe(df)
#         st.markdown("### Detailed Job Listings")
#         for index, row in df.iterrows():
#             st.write(f"#### {row['job-title']} at {row['company']}")
#             st.write(f"**Level:** {row['level']}")
#             st.write(f"**Type:** {row['job_type']}")
#             st.write(f"**Salary:** {row['salary']}")
#             st.write(f"**Date Posted:** {row['date_posted']}")
#             st.write(f"**Description:** {row['description']}")
#             st.write(f"**Skills:** {', '.join(row['skills'])}")
#             st.markdown(f"[Job Link]({row['link']})", unsafe_allow_html=True)
#     else:
#         st.write("No jobs found.")


# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime

# # Function to parse date strings into datetime objects
# def parse_date(date_str):
#     try:
#         # Assuming the date is in a format like "April 15, 2023"
#         return datetime.strptime(date_str, '%B %d, %Y')
#     except ValueError:
#         # Return current datetime if parsing fails
#         return datetime.now()

# # Function to fetch job postings
# def fetch_jobs(keywords, location, geo_id, job_id, total_jobs):
#     l = []
#     k = []
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
#     base_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keywords}&location={location}&geoId={geo_id}&currentJobId={job_id}'
#     #&start={{}}'
    
#     for i in range(0, (total_jobs // 25) + 1):
#         res = requests.get(base_url.format(i * 25), headers=headers)
#         print(base_url)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         all_jobs_on_this_page = soup.find_all("li")
#         for job in all_jobs_on_this_page:
#             job_data = job.find("div", {"class": "base-card"})
#             if job_data:
#                 job_id = job_data.get('data-entity-urn')
#                 if job_id:
#                     l.append(job_id.split(":")[3])

#     # Fetch detailed job info
#     for j in l:
#         target_url = f'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{j}'
#         resp = requests.get(target_url, headers=headers)
#         soup = BeautifulSoup(resp.text, 'html.parser')
        
#         o = {}
#         o["company"] = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt') if soup.find("div", {"class": "top-card-layout__card"}) else None
#         o["job-title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip() if soup.find("div", {"class": "top-card-layout__entity-info"}) else None
#         o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace("Seniority level", "").strip() if soup.find("ul", {"class": "description__job-criteria-list"}) else None
#         o["description"] = soup.find("div", {"class": "show-more-less-html__markup"}).get_text(strip=True) if soup.find("div", {"class": "show-more-less-html__markup"}) else "No description available"
#         o["salary"] = soup.find("span", {"class": "salary"}).get_text(strip=True) if soup.find("span", {"class": "salary"}) else "Salary not specified"
#         o["link"] = f'https://www.linkedin.com/jobs/view/{j}'
#         o["posted date"] = soup.find("dl", {"class": "position-overview"}).find("dd", {"class": "extra-large-semibold"}).find("span", {"class": "job-view-content"})
#         o["skills"] = [skill.get_text(strip=True) for skill in soup.find_all("span", {"class": "skill"})]  # Assuming skills are listed in <span class="skill">
#         o["job_type"] = soup.find("span", {"class": "job-type"}).get_text(strip=True) if soup.find("span", {"class": "job-type"}) else "Job type not specified"

#         k.append(o)

#     df = pd.DataFrame(k)
#     return df.sort_values(by='date_posted', ascending=False)  # Sort by date descending (most recent first)

# # Streamlit interface setup
# st.title('Leemz LI Job Finder')
# keywords = st.text_input('Keywords', 'Analyst')
# location = st.text_input('Location', 'New Jersey, United States')
# #geo_location_id = {"New Jersey" :101651951, "New York Metropolitan Area": 90000070, "New York City": 102571732}
# #geo_id = st.radio("Select an option", geo_location_id.keys())
# geo_id = st.radio("Choose location:", ["101651951", "90000070", "102571732"], captions = ["New Jersey", "New York Metropolitan Area", "New York City"])
# job_id = st.number_input('Current Job ID', min_value=0, value=3415227738, step=1)
# total_jobs = st.number_input('Total Jobs to Fetch', min_value=25, max_value=100, value=25, step=25)

# if st.button('Fetch Jobs'):
#     df = fetch_jobs(keywords, location, geo_id, job_id, total_jobs)
#     if not df.empty:
#         st.dataframe(df[['job-title', 'company', 'level', 'job_type', 'date_posted']])
#         st.markdown("### Detailed Job Listings")
#         for index, row in df.iterrows():
#             st.write(f"#### {row['job-title']} at {row['company']}")
#             st.write(f"**Level:** {row['level']}")
#             st.write(f"**Type:** {row['job_type']}")
#             st.write(f"**Salary:** {row['salary']}")
#             st.write(f"**Date Posted:** {row['date_posted'].strftime('%B %d, %Y')}")
#             st.write(f"**Description:** {row['description']}")
#             st.write(f"**Skills:** {', '.join(row['skills'])}")
#             st.markdown(f"[Job Link]({row['link']})", unsafe_allow_html=True)
#     else:
#         st.write("No jobs found.")

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from io import BytesIO

# Function to parse date strings into datetime objects
def parse_date(date_str):
    try:
        # Assuming the date is in a format like "April 15, 2023"
        return datetime.strptime(date_str, '%B %d, %Y')
    except ValueError:
        # Return current datetime if parsing fails
        return datetime.now()

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Jobs')
    processed_data = output.getvalue()
    return processed_data

# Function to fetch job postings
def fetch_jobs(keywords, location, geo_id, job_id, total_jobs):
    l = []
    k = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    base_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keywords}&location={location}&geoId={geo_id}&currentJobId={job_id}&start={{}}'
    
    for i in range(0, (total_jobs // 25) + 1):
        res = requests.get(base_url.format(i * 25), headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        all_jobs_on_this_page = soup.find_all("li")
        for job in all_jobs_on_this_page:
            job_data = job.find("div", {"class": "base-card"})
            if job_data:
                job_id = job_data.get('data-entity-urn')
                if job_id:
                    l.append(job_id.split(":")[3])

    for j in l:
        target_url = f'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{j}'
        resp = requests.get(target_url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        o = {}
        o["company"] = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt') if soup.find("div", {"class": "top-card-layout__card"}) else None
        o["job-title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip() if soup.find("div", {"class": "top-card-layout__entity-info"}) else None
        o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace("Seniority level", "").strip() if soup.find("ul", {"class": "description__job-criteria-list"}) else None
        o["description"] = soup.find("div", {"class": "show-more-less-html__markup"}).get_text(strip=True) if soup.find("div", {"class": "show-more-less-html__markup"}) else "No description available"
        o["salary"] = soup.find("span", {"class": "salary"}).get_text(strip=True) if soup.find("span", {"class": "salary"}) else "Salary not specified"
        o["date_posted"] = soup.find("span", {"class": "posted-time-ago__text"}).get_text(strip=True) if soup.find("span", {"class": "posted-time-ago__text"}) else "Date not available"
        o["link"] = f'https://www.linkedin.com/jobs/view/{j}'
        o["skills"] = ', '.join([skill.get_text(strip=True) for skill in soup.find_all("span", {"class": "skill"})])
        o["job_type"] = soup.find("span", {"class": "job-type"}).get_text(strip=True) if soup.find("span", {"class": "job-type"}) else "Job type not specified"

        k.append(o)

    df = pd.DataFrame(k)
    df['date_posted'] = df['date_posted'].apply(parse_date)
    return df.sort_values(by='date_posted', ascending=False)

# Streamlit interface setup
st.title('Leemz LI Job Finder')
keywords = st.text_input('Keywords', 'Analyst')
location = st.text_input('Location', 'New Jersey, United States')
geo_id = st.radio("Choose location:", ["101651951", "90000070", "102571732"], index=0, format_func=lambda x: {"101651951": "New Jersey", "90000070": "New York Metropolitan Area", "102571732": "New York City"}[x])
job_id = st.number_input('Current Job ID', min_value=0, value=3415227738, step=1)
total_jobs = st.number_input('Total Jobs to Fetch', min_value=25, max_value=100, value=25, step=25)

if st.button('Fetch Jobs'):
    df = fetch_jobs(keywords, location, geo_id, job_id, total_jobs)
    if not df.empty:
        st.dataframe(df)
        excel_data = to_excel(df)
        st.download_button(label='Download Excel', data=excel_data, file_name='job_listings.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        st.markdown("### Detailed Job Listings")
        for index, row in df.iterrows():
            st.write(f"#### {row['job-title']} at {row['company']}")
            st.write(f"**Level:** {row['level']}")
            st.write(f"**Type:** {row['job_type']}")
            st.write(f"**Salary:** {row['salary']}")
            st.write(f"**Date Posted:** {row['date_posted'].strftime('%B %d, %Y')}")
            st.write(f"**Description:** {row['description']}")
            st.write(f"**Skills:** {row['skills']}")
            st.markdown(f"[Job Link]({row['link']})", unsafe_allow_html=True)
    else:
        st.write("No jobs found.")
