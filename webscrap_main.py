import requests
from bs4 import BeautifulSoup

# all_jobs = []

# def scrape_page(url):
# response = requests.get(url)
# soup = BeautifulSoup(
#     response.content, 
#     "html.parser",
#     )
# jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

# for job in jobs:
#     title = job.find("span", class_="title")
#     company, position, region =  job.find_all("span", class_="company")
#     job_url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
#     job_data= {
#         "title": title.text,
#         "company": company.text,
#         "position": position.text,
#         "region": region.text,
#         "url" : f"https://weworkremotely.com{job_url}"
#     }
#     all_jobs.append(job_data)

# print(all_jobs)

class scrape:

    def __init__(url):
    
    
