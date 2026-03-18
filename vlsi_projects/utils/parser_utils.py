def file_reader(file_path):
    with open(file_path,"r") as f:
        return f.read()

def file_writer(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def file_appender(file_path, content):
    with open(file_path,'a') as f:
        f.write(content)

def file_reader_lines(file_path):
    with open(file_path,"r") as f:
        return f.readlines()
#print(file_reader("vlsi_projects/data/timing_report.txt"))