from flask import Flask, render_template, request


app = Flask("Super Scrapper")

# @ -> 데코레이터 아래의 "함수"를 실행하도록 유도해줌.
@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    # print(request.args.get('word'))
    word = request.args.get('word')
    word = word.lower()
    return render_template("report.html", searchingBy=word, potato="eat")

app.run(host="localhost")