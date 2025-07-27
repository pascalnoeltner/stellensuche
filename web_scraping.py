import requests

from playwright.sync_api import sync_playwright


def get_jobs_api(job, stadt, umkreis):

    url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"
    params = {
        "was": job,
        "wo": stadt,
        "umkreis": umkreis
    }
    headers = {
        "X-API-Key": "jobboerse-jobsuche"
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.ok:
        data = response.json()
        stellen = data.get("stellenangebote", [])

        for i, stelle in enumerate(stellen, 1):
            titel = stelle.get("titel", "Kein Titel")
            arbeitgeber = stelle.get("arbeitgeber", "Unbekannt")
            ort = stelle.get("arbeitsort", {}).get("ort", "Unbekannt")
            plz = stelle.get("arbeitsort", {}).get("plz", "00000")
            strasse = stelle.get("arbeitsort", {}).get("strasse", "")
            refnr = stelle.get("refnr", "")
            datum = stelle.get("aktuelleVeroeffentlichungsdatum", "")
        
            print(f"{i}. {titel}")
            print(f"   Arbeitgeber: {arbeitgeber}")
            print(f"   Ort: {plz} {ort}, {strasse}")
            print(f"   Referenznummer: {refnr}")
            print(f"   Veröffentlicht am: {datum}")
            print("-" * 50)

    else:
        print(f"Fehler: {response.status_code}")
    
def web_scrape(ref_nr="16752-r5445-S"):

    URL = f"https://www.arbeitsagentur.de/jobsuche/jobdetail/{ref_nr}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
    
        print(f"🔍 Lade Jobseite: {URL}")
        page.goto(URL, wait_until="networkidle")

        # Optional: Warte auf sichtbare Hauptbox (z. B. Titel)
        page.wait_for_selector("h1")

        # Drucke gesamten sichtbaren Text der Seite
        text = page.inner_text("body")
        print("\n=== Inhalt der Seite ===\n")
        print(text)

        browser.close()
