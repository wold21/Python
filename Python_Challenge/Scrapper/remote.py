import requests
from bs4 import BeautifulSoup

def extract_job(html, link):
    # title = html.find("span", {"class":"title"}).string
    # company = html.find("span", {"class":"company"}).string
    # location = html.find("span", {"class":"region company"}).string
    # link = link.find("a")["href"]
    # return {"title":title, "company":company, "location":location,
    #         "apply link" : f"https://weworkremotely.com/{link}"}
    pass

def extract_jobs(url):
    jobs=[]
    print("Remote Scrapping Start...")
    result = requests.get(f"{url}", allow_redirects=False)
    print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tbody").find("tr")
    for result in results:
        job = extract_job(result, link)
        jobs.append(job)
    print("Remote Scrapping Finished...")
    return jobs


def get_remote_jobs(word):
    url=f"https://remoteok.io/remote-{word}-jobs"
    jobs = extract_jobs( url)
    return jobs