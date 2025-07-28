from web_scraping import get_jobs_api
from web_scraping import web_scrape
from prompts import template
from llm_models import get_llm

job = input("Job: ")
stadt = input("Stadt: ")
umkreis = int(input("Umkreis: "))

refnrs = get_jobs_api(job, stadt, umkreis)
refnr = int(input("Nummer: "))

text = web_scrape(refnrs[refnr])

llm = get_llm()
response = llm.invoke(template + text)
print(response.content)
