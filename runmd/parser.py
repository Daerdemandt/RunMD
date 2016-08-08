import re

def has_code(line):
    return re.search('`[^`]+`', line)

def extract_code(line):
    return re.search('`[^`]+`', line).group(0)[1:-1]

def parse_text(text):
    result = []
    for line in text:
        if has_code(line):
            result.append(extract_code(line))
    
    return result

def check_file(filename):
    # checks if file is compliant
    return True

def read_file(filename):
    #TODO: handle non-existent files
    with open(filename) as input_file:
        #TODO: limit file size to something reasonable like 50Mb
        return input_file.readlines()

