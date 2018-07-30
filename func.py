import os

# Create a new folder for every new website/project
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating a new project: "+directory)
        os.makedirs(directory)

# Creating queue and crawled files in the project directory
def create_data_files(project_name, home_page_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    
    if not os.path.isfile(queue):
        write_file(queue, home_page_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
   with open(path, 'w') as f:
    f.write(data)
    f.close()

#adding links
def append_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

#deleting links
def delete_file_content(path):
    with open(path,'w'):
        pass

#reading a file and coverting them to sets
def file_to_set(file_name):
    results =  set()
    with open(file_name,'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results

# set to file, each item to new line

def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file,link)
