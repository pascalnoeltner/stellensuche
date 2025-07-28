from langchain.prompts import PromptTemplate

ASSISTANT_SELECTION_INSTRUCTIONS = """

Schneide aus einer Stellenbeschreibung die Einleitung heraus,
welche Angaben zur Stelle enthält heraus und schneide ebenso 
den Schlussteil heraus, der Angaben zum Arbeitgeber enthält.
Behalte nur den Mittelteil, in dem geschildert wird, um was
es geht, wie es gemacht wird, und wer dafür geeignet ist.

Beispiel:

AUSSCHNEIDEN Einleitung:

Detailansicht des Stellenangebots
Zurück zur Startseite
Stellendetails zu: Software Engineer* für Datenprojekte
Zurück zum Ergebnislisteneintrag
Software Engineer* für Datenprojekte
Kopfbereich
Angebotsart:
Arbeit
Software Engineer* für Datenprojekte
Arbeitgeber:
inovex GmbH
Zur BewerbungVormerkenLink kopierenPDF/Druckansicht
Arbeitsort
Karlsruhe, Baden
Anstellungsart
Vollzeit
Beginn
ab sofort
Berufsbezeichnung
Data Engineer
Veröffentlichungsdatum:
Vor 30+ Tagen veröffentlicht
Änderungsdatum:
Vor 8 Tagen bearbeitet
Stellenbeschreibung

BEHALTEN Mittelteil:

Was du bei uns bewegen kannst
Gemeinsam mit deinem agilen, cross-funktionalen Projektteam hilfst du unseren Kunden aus unterschiedlichen Branchen, ihre Daten nutzbar zu machen. Dein Job beginnt nicht erst mit der Entwicklung von Datenprojekten: Du stimmst dich eng mit unseren Kunden ab und berätst sie in Bezug auf die technische Machbarkeit und die konkrete Umsetzung ihrer digitalen Innovationen.Als Software Engineer* für Datenprojekte gestaltest du das Fundament der datengetriebene Anwendungen und entwickelst robuste und wartbare Architekturen. Du sorgst für ein effizientes, sicheres Zusammenspiel der Systeme und Services im Einklang mit den Anforderungen des Kunden.Schon bei der Konzeption und Entwicklung von Datenplattformen, Datenverarbeitungsprozesse oder Daten-Services planst du den späteren hochverfügbaren und -skalierbaren Betrieb der Softwarebestandteile in der Cloud, on premise oder hybrid mit.Mithilfe automatisierter Testing-Verfahren (Unit Testing, CI/CD, Ende-zu-Ende-Tests uvm.) sorgst du für eine kontinuierliche Qualitätskontrolle und -optimierung. Auch die Sicherheit der entwickelten Datensysteme behältst du dabei natürlich immer im Blick.

In unseren Projekten verwenden wir häufig folgende Technologien:
Python, SQL, JavaRelationale und NoSQL-DatenbankenFlask, Spring, FastAPIDatabricks, Spark, Kafka, Airflow, dbt, BigQuery oder Snowflake AWS, GCP, AzureDocker, Kubernetes
Intern wie extern kannst du dich bei uns auf vielfältige Art einbringen: Deinen anfangs gewählten Schwerpunkt kannst du jederzeit verlagern.

Wer gut zu uns passen würde
Du hast ein abgeschlossenes Studium im MINT-Bereich oder in einem vergleichbaren Studiengang und idealerweise auch schon erste Erfahrung mit einer oder mehreren der oben genannten Technologien gesammelt.Du begeisterst dich dafür, datengetriebene Anwendungen lauffähig in den Praxisbetrieb unserer Kunden zu implementieren und scheust nicht davor dich mit Datenverarbeitung, komplexen Algorithmen oder AI-Modellen auseinanderzusetzen. Du hast ein Engineering Mindset und möchtest lernen, wie man das Beste aus datengetriebenen Anwendungen herausholt, um sie möglichst automatisiert, wartbar und robust auf die Straße zu bringen.Du hast den Anspruch, dich in neue Technologien einzuarbeiten und sie in Bezug auf den Projekteinsatz zu prüfen. Dein Wissen teilst du gern mit deinen Kolleg:innen.Du kannst gut priorisieren und hast ein Gespür für die richtige Balance zwischen Pragmatismus und Perfektionismus.Du hast ausgezeichnete kommunikative Fähigkeiten und bringst sehr gute Deutsch- und Englischkenntnisse in Wort und Schrift mit.

AUSSCHNEIDEN Schlussteil:

Arbeitsorte
Karte anzeigen
76131 Karlsruhe, Baden
Unternehmensdarstellung: inovex GmbH

inovex GmbH

Homepage
Alle offenen Stellen anzeigen
Vollständige Unternehmensdarstellung anzeigen
Informationen zur Bewerbung
Sicherheitsabfrage

Wir schützen die Kontaktdaten des Arbeitgebers vor unerlaubten Zugriffen. Bitte geben Sie die dargestellten Zeichen in das Textfeld ein, um die Kontaktdaten des Arbeitgebers anzuzeigen.

Anderes Bild laden
Audioversion abspielen

Hinweis: Die dargestellten Zeichen enthalten keine Umlaute (ä, ö, ü oder ß), Sonderzeichen oder Leerzeichen.

Dargestellte Zeichen
Absenden
Fußbereich
Stelle betreut durch Arbeitgeber
Referenz-Nr.: 16752-r5445-S
Verstoß melden
Zurück zum Ergebnislisteneintrag


WENDE DIESE REGELN FÜR DIE FOLGENDE STELLENANZEIGE AN:
"""


