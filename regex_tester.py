import re

def make_all_single_lines(in_string):
    pattern = "\\\W*(?:\r\n|\n|\r)"
    repl = ""
    out_string = re.sub(pattern, repl, in_string)
    return out_string

def get_import_lines(in_string):
    pattern = "(?<=import\W).+"
    return re.findall(pattern, in_string)

def get_import_items(in_list):
    all_items = []
    pattern = "\w+"
    for i_string in in_list:
        all_items.extend([i_match for i_match in re.findall(pattern, i_string)])
    return list(set(all_items)).sort()

def extract_python_lib(in_string):
    return get_import_items(get_import_lines(make_all_single_lines(in_string)))
