from functools import partial
from glob import iglob
from re import sub

def get_log_files():
    for log_file_path in iglob('*.log'):
        yield log_file_path

def get_raw_text(file_path):
    with open(file_path, 'r') as log_file:
        return log_file.readlines()
 
def remove_stamps(line_list):
    remover = partial(sub, r"\d{6,8}\.\d{6}", "")
    return map(remover, line_list)
 
def rewrite_new_lines(new_Lines, file_path):
    with open(file_path, 'w+') as new_file:
        new_file.writelines(new_Lines)
 
def main():
    def rewrite_log_file(log):
        rewrite_new_lines(remove_stamps(get_raw_text(log)), log)
    map(rewrite_log_file, get_log_files())
 
if __name__ == '__main__':
    main()