import sys
script, input_encoding, error = sys.argv

file_path = '../resources/data/'

def main(encoding, errors):
    with open(file_path + 'languages.txt', encoding='utf-8') as languages:
        lines = languages.readlines()
        for line in lines:
            print_line(line, encoding, errors)
        
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding=encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding=encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)

main(input_encoding, error)