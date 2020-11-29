from flask import Flask, render_template, request, redirect, send_file
from Scrapper.so import get_so_jobs
from Scrapper.indeed import get_indeed_jobs
from Scrapper.wework import get_wework_jobs
from save import save_to_file
import csv


app = Flask(__name__)

db = {}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word=word.lower()
        existingJobs=db.get(word)
        if existingJobs:
            jobs=existingJobs
        else:
            jobs = get_so_jobs(word) + get_indeed_jobs(word) + get_wework_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", 
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word=word.lower()
        jobs=db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

if __name__ == "__main__":
    app.run(host="192.168.171.228", debug=True)
