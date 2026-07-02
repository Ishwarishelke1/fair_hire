import nltk
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from data.skills import SKILLS_DB

stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    tokens = word_tokenize(text)

    filtered_tokens = []

    for word in tokens:

        if word not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens

def extract_skills(tokens):

    found_skills = []

    for skill in SKILLS_DB:

        if skill.lower() in " ".join(tokens):

            found_skills.append(skill)

    return list(set(found_skills))