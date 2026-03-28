import spacy
from spacy.training.example import Example
from spacy.tokens import DocBin
import random

def train_ner():
    print("Initializing blank 'en' model...")
    nlp = spacy.blank("en")
    
    print("Loading training data from 'train.spacy'...")
    try:
        doc_bin = DocBin().from_disk("train.spacy")
    except Exception as e:
        print(f"Error loading train.spacy: {e}")
        return

    docs = list(doc_bin.get_docs(nlp.vocab))
    train_data = []
    
    # Set up the pipeline and add labels
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")
        
    labels_found = set()
    for doc in docs:
        ents_tuple = []
        for ent in doc.ents:
            ner.add_label(ent.label_)
            labels_found.add(ent.label_)
            ents_tuple.append((ent.start_char, ent.end_char, ent.label_))
            
        train_data.append(Example.from_dict(nlp.make_doc(doc.text), {"entities": ents_tuple}))
        
    print(f"Loaded {len(train_data)} training examples.")
    print(f"Discovered labels: {labels_found}")
    
    if len(train_data) == 0 or not labels_found:
        print("No valid entities found in data. Exiting training.")
        return

    # Train the NER model
    print("Beginning training...")
    try:
        optimizer = nlp.begin_training()
    except Exception as e:
        print(f"Failed to begin training: {e}")
        return
        
    epochs = 30
    for itn in range(epochs):
        random.shuffle(train_data)
        losses = {}
        for batch in spacy.util.minibatch(train_data, size=8):
            try:
                nlp.update(
                    batch,
                    drop=0.2,
                    sgd=optimizer,
                    losses=losses,
                )
            except Exception as e:
                pass
        print(f"Epoch {itn+1:>2}/{epochs} - Loss: {losses.get('ner', 0.0):.4f}")
        
    # Save model
    output_dir = "./custom_ner_model"
    print(f"Training complete. Saving model to '{output_dir}'")
    nlp.to_disk(output_dir)

if __name__ == "__main__":
    train_ner()
