import json
file_path = 'D:\Python_Lab_Cycles\Lab_cycle_2\QN3\iris.json'

# def list_read(file_path):
#     list_file = open(file_path,'r')
#     list_done = list_file.readlines()
#     print(list_done)

def read(file_path):
    listx=[]
    print("Reading json files contents as list of dict ")
    with open(file_path) as f:
        data = json.load(f)
    print(data)

read(file_path)
# list_read(file_path)