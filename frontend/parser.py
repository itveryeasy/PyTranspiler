import re

def parse_code(source_code):
    tokens = re.findall(r'\w+|\S', source_code)
    print(f"Tokens: {tokens}")
    return {"tokens": tokens}