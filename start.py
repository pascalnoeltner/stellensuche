from web_scraping import get_jobs_api

job = input("Job: ")
stadt = input("Stadt: ")
umkreis = int(input("Umkreis: "))

get_jobs_api(job, stadt, umkreis)

# web_scrape()
