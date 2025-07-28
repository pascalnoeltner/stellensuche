from langchain.prompts import PromptTemplate

template = """

Bitte analysiere die folgende Stellenanzeige.

Deine Aufgabe ist es, den Mittelteil der Anzeige in zwei Abschnitte zu unterteilen:

1. Tätigkeiten: Welche Aufgaben, Verantwortlichkeiten, Methoden oder Technologien sind mit der Stelle verbunden?
2. Anforderungen: Welche Qualifikationen, Kenntnisse, Erfahrungen oder persönlichen Eigenschaften werden erwartet?

Entferne:
- Die Einleitung mit Angaben wie Titel, Ort, Arbeitgeber oder Veröffentlichungsdatum.
- Den Schlussteil mit Informationen über das Unternehmen, Bewerbungshinweise, Kontaktinformationen oder rechtliche Hinweise.

Gib nur diese beiden Abschnitte zurück – und zwar in folgendem Format:

### TÄTIGKEITEN:
<Auflistung der Tätigkeiten>

### ANFORDERUNGEN:
<Auflistung der Anforderungen>

Füge keine weiteren Texte, Überschriften oder Kommentare hinzu.

Hier ist die Stellenanzeige:
{jobtext}
"""
