import spacy

def test_custom_model():
    print("Loading trained Custom NER model...")
    try:
        nlp = spacy.load("./custom_ner_model")
    except Exception as e:
        print(f"Failed to load model: {e}")
        return

    test_bios = [
        "Hey guys follow me on insta @cool_dude_99 and text me at +91 9876543210",
        "Nothing much just a normal guy. t.me/random_group. Contact: nine eight seven six five four three two one zero",
        "I am on telegram: @user123 and my number is 1 2 3 4 5 6 7 8 9 0",
        "Follow my photography page instagram.com/nature_shots_2024",
        "Contact me for biz: 888-555-0192 or ig: @biz_page"
    ]

    with open('test_output_clean.txt', 'w', encoding='utf-8') as f:
        f.write("\n" + "="*50 + "\n")
        f.write("TESTING MODEL ON NEW BIOS\n")
        f.write("="*50 + "\n\n")

        for i, bio in enumerate(test_bios, 1):
            doc = nlp(bio)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            
            f.write(f"Test #{i}:\n")
            f.write(f"Bio Text: '{bio}'\n")
            f.write(f"Extracted Entities: {entities}\n")
            f.write("-" * 50 + "\n")
            
    print("Test output saved to test_output_clean.txt")

if __name__ == "__main__":
    test_custom_model()
