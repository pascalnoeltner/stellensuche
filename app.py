from flask import Flask, render_template, request, redirect, url_for, session
from web_scraping import get_jobs_api, web_scrape
from prompts import template
from llm_models import get_llm

app = Flask(__name__)
app.secret_key = "dein_geheimer_key"  # Für Sessions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job = request.form.get("job")
        stadt = request.form.get("stadt")
        umkreis = int(request.form.get("umkreis"))

        refnrs = get_jobs_api(job, stadt, umkreis)
        session["refnrs"] = list(refnrs.keys())  # Speichere RefNr-Liste in der Session

        return render_template("results.html", refnrs=enumerate(refnrs))
    return render_template("index.html")

@app.route("/show/<int:refnr>")
def show(refnr):
    refnrs = session.get("refnrs")
    if refnrs is None or refnr >= len(refnrs):
        return "Ungültige Referenznummer", 400

    text = web_scrape(refnr)
    llm = get_llm()
    response = llm.invoke(template + text)

    return render_template("output.html", text=text, response=response.content)

if __name__ == "__main__":
    app.run(debug=True)

