import pandas as pd
import re
import spacy
from spacy.tokens import DocBin
import json

# Extended word digits to include common obfuscations
word_digit = r"(?:zero|one|two|too|three|tree|four|for|five|six|seven|eight|ate|nine)"

PHONE_REGEX = [
    r'\b\d{10}\b',
    r'\b(?:\d[\s\W_]*){10}\b',
    r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    rf'(?i)\b(?:{word_digit}[\s\W_]*){{10}}\b',
    r'(?i)9[\ufe0f\u20e3]?8[\ufe0f\u20e3]?7[\ufe0f\u20e3]?6[\ufe0f\u20e3]?5[\ufe0f\u20e3]?4[\ufe0f\u20e3]?3[\ufe0f\u20e3]?2[\ufe0f\u20e3]?1[\ufe0f\u20e3]?0[\ufe0f\u20e3]?' # emoji digits roughly
]

TG_REGEX = [
    r'(?i)\b(?:t\.me/|telegram\.me/)([a-zA-Z0-9_]{5,32})\b',
    r'(?i)\b(?:telegram|tg)[\s:-]*@?([a-zA-Z0-9_]{5,32})\b'
]

IG_REGEX = [
    r'(?i)\b(?:instagram\.com/)([a-zA-Z0-9_.]+)\b',
    r'(?i)\b(?:ig|isg|istg|insta|instagram|inst|gram)[\s:-]*@?([a-zA-Z0-9_.]+)\b'
]

SNAP_REGEX = [
    r'(?i)\b(?:sc|snap|snp|snapchat|sncpchat)[\s:-]*@?([a-zA-Z0-9_.-]+)\b'
]

DISCORD_REGEX = [
    r'(?i)\b(?:discord|cord|dscrd|dsc)[\s:-]*@?([a-zA-Z0-9_.-]+#\d{4}|[a-zA-Z0-9_.-]+)\b'
]

EMAIL_REGEX = [
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
]

WA_REGEX = [
    r'(?i)\b(?:wa\.me/|whatsapp|wa)[\s:-]*\+?(\d[\d\s-]{7,15})\b'
]

def extract_entities(text):
    if not isinstance(text, str):
        return []
        
    entities = []
    
    label_map = {
        'PHONE': PHONE_REGEX,
        'TELEGRAM': TG_REGEX,
        'INSTAGRAM': IG_REGEX,
        'SNAPCHAT': SNAP_REGEX,
        'DISCORD': DISCORD_REGEX,
        'EMAIL': EMAIL_REGEX,
        'WHATSAPP': WA_REGEX
    }
    
    for label, patterns in label_map.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text):
                start, end = match.start(), match.end()
                while end > start and text[end-1].isspace():
                    end -= 1
                entities.append((start, end, label))
                
    # Handle overlaps
    entities = sorted(entities, key=lambda x: (x[0], -x[1]))
    filtered_entities = []
    last_end = -1
    for start, end, label in entities:
        if start >= last_end:
            filtered_entities.append((start, end, label))
            last_end = end
            
    return filtered_entities

def main():
    bios = []
    print("Loading Data.xlsx...")
    try:
        df = pd.read_excel('Data.xlsx')
        bios.extend([str(b) for b in df['Bio'].dropna()])
    except Exception as e:
        print(f"Error loading excel: {e}")
        
    print("Loading synthetic_data.json...")
    try:
        with open('synthetic_data.json', 'r') as f:
            syn = json.load(f)
            bios.extend([item['Bio'] for item in syn])
    except Exception as e:
        print(f"Error loading synthetic: {e}")

    nlp = spacy.blank("en")
    doc_bin = DocBin()
    
    stats = {}

    for bio in bios:
        if not bio.strip(): continue
            
        entities = extract_entities(bio)
        doc = nlp.make_doc(bio)
        ents = []
        for start, end, label in entities:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is not None:
                ents.append(span)
                stats[label] = stats.get(label, 0) + 1
                
        try:
            doc.ents = ents
            doc_bin.add(doc)
        except Exception:
            pass

    print(f"Extraction stats: {stats}")
    print(f"Saved {len(doc_bin)} documents to train.spacy")
    doc_bin.to_disk("./train.spacy")

if __name__ == "__main__":
    main()
