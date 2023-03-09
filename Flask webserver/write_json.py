import json

def write(data):
    file1 = open('data_list.txt', "a")  # append mode
    file1.write(data + "\n")
    file1.close()
