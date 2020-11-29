import requests
from bs4 import BeautifulSoup

def extract_job(html, link):
    title = html.find("span", {"class":"title"}).string
    company = html.find("span", {"class":"company"}).string
    # location = html.find("span", {"class":"region company"}).string
    link = link.find("a")["href"]
    return {"title":title, "company":company,
            "apply link" : f"https://weworkremotely.com/{link}"}

def extract_jobs(url):
    jobs=[]
    print("Wework Scrapping Start...")
    result = requests.get(f"{url}")
    soup = BeautifulSoup(result.text, "html.parser")
    link = soup.find("article").find("ul").find("li")
    results = soup.find_all("li", {"class":"feature"})
    for result in results:
        job = extract_job(result, link)
        jobs.append(job)
    print("Wework Scrapping Finished...")
    return jobs


def get_wework_jobs(word):
    url=f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs( url)
    return jobs