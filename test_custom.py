import spacy

bio = "⁸continents one world 6 dimensions e8gh5 spaces f0ur faces"

print("Loading model...")
nlp = spacy.load("./custom_ner_model")
print(f"Testing on: {bio}")
doc = nlp(bio)
entities = [(ent.text, ent.label_) for ent in doc.ents]

with open("custom_test_output.txt", "w", encoding="utf-8") as f:
    f.write(str(entities))
print("Done writing to custom_test_output.txt")
