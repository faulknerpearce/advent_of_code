def read_file_return_string(file):
    with open(file) as data:
        text_raw = data.read()
        text = text_raw.replace('\n', '')
    return text

def is_symbol(char):
    if char == '*' or char =='#' or char == '$' or char == '+':
        return True
    else:
        return False


