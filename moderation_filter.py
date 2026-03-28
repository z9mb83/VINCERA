import spacy

# Load the model once globally for faster inference after boot
print("Loading Moderation Filter Model...")
try:
    nlp = spacy.load("./custom_ner_model")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

def moderate_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    if entities:
        print("\n[MODERATION ALERT] Action Denied!")
        print("Your content contains prohibited contact information which goes against our safety guidelines.")
        
        detected_types = set([label for text, label in entities])
        print(f"Detected Categories: {', '.join(detected_types)}")
        
        print("\n--- Details (For Admin) ---")
        for ent_text, ent_label in entities:
             print(f"- Found [{ent_label}]: '{ent_text}'")
        print("---------------------------\n")
    else:
        print("\n[MODERATION APPROVED] Content is clean.\n")

if __name__ == "__main__":
    print("=== Dating App Moderation Filter ===")
    print("Type a bio or prompt to test the filter. Type 'exit' or 'quit' to close.\n")
    
    while True:
        try:
            user_input = input("Enter text > ")
            if user_input.strip().lower() in ['exit', 'quit']:
                break
            moderate_text(user_input)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break
