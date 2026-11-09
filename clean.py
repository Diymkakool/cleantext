import unicodedata
import sys

def save_file(path: str, content: str):
    try:
        with open(path, 'w', encoding='utf-8') as out:
            out.write(content)
    except Exception as e:
        print(f"Failure to save: {e}")

cleaned_chars = []
cleanedtext = None
inputpath = sys.argv[1]
outpath = sys.argv[2]
file = open(inputpath)
text = file.read()
for char in text:
    if char in (' ', '\n', '\r', '\t'):
        cleaned_chars.append(char)
        continue
        
    category = unicodedata.category(char)
    
    if category in ('Cc', 'Cf', 'Cn', 'Co', 'Cs'):
        continue
        
    cleaned_chars.append(char)
    cleanedtext = "".join(cleaned_chars)
        
save_file(outpath, cleanedtext)