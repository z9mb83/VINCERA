import spacy
import pandas as pd

def predict_on_samples():
    print("Loading model from './custom_ner_model'...")
    try:
        nlp = spacy.load("./custom_ner_model")
    except Exception as e:
        print(f"Failed to load model: {e}")
        return

    print("Loading Data.xlsx for testing...")
    df = pd.read_excel("Data.xlsx")
    
    # Drop rows with no bio and sample a few
    df_clean = df.dropna(subset=['Bio'])
    if len(df_clean) > 10:
        samples = df_clean.sample(n=10, random_state=42)
    else:
        samples = df_clean
        
    with open('predictions_clean.txt', 'w', encoding='utf-8') as f:
        f.write("\n" + "="*50 + "\n")
        f.write(f"Predictions on {len(samples)} Random Samples from Dataset\n")
        f.write("="*50 + "\n\n")
        
        for idx, row in samples.iterrows():
            bio = str(row['Bio'])
            
            # Run inference using the trained model
            doc = nlp(bio)
            
            # Extract the discovered entities
            entities_found = [(ent.text, ent.label_) for ent in doc.ents]
            
            f.write(f"Row {idx+2}:\n")  # Excel 1-based indexing roughly
            f.write(f"Bio: {bio}\n")
            f.write(f"Extracted: {entities_found}\n")
            f.write("-" * 50 + "\n")
            
    print("Predictions saved to predictions_clean.txt")

if __name__ == "__main__":
    predict_on_samples()
