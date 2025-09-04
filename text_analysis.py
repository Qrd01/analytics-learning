from collections import Counter
import re

def normalize(text: str):
    text = text.lower()
    # remove punctuation
    text = re.sub(r"[.,!?;:()\[\]{}\-\n]", " ", text)
    # collapse spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

def word_freq(text: str):
    words = normalize(text).split(" ")
    counter = Counter(w for w in words if w)
    return counter

if __name__ == "__main__":
    sample_text = (
        "Yandex is a great place to learn analytics and grow as a professional. "
        "I want to study Python, SQL, and data visualization further."
    )
    freq = word_freq(sample_text)
    print("Word frequency:")
    for w, c in freq.most_common():
        print(f"{w}: {c}")
