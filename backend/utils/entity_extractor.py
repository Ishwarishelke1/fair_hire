import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    entities = {
        "name": "",
        "organizations": [],
        "locations": [],
        "emails": [],
        "phones": []
    }

    for ent in doc.ents:

        if ent.label_ == "PERSON" and entities["name"] == "":
            entities["name"] = ent.text

        elif ent.label_ == "ORG":
            entities["organizations"].append(ent.text)

        elif ent.label_ == "GPE":
            entities["locations"].append(ent.text)

    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    phone_pattern = r'\+?\d[\d\s\-]{8,15}'

    entities["emails"] = re.findall(email_pattern, text)

    entities["phones"] = re.findall(phone_pattern, text)

    return entities