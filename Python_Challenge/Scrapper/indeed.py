import requests
from bs4 import BeautifulSoup

def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("h2",{"class":"title"}).find('a')["title"]
    company = html.find("span", {"class":"company"})
    company_a = company.find('a')
    if company_a is not None:
        company = str(company_a.string)
    else:
        company = str(company.string)
    company = company.strip()
    # location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {"title": title, "company":company,
            "link": f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page, url):
    jobs=[]
    for page in range(last_page):
        print(f"Scrapping Indeed {page+1}")
        result = requests.get(f"{url}&start={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        rerults = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for result in rerults:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_indeed_jobs(word):
    url = f"https://www.indeed.com/jobs?q=python&limit={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs