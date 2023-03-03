import os 

file = input('Entera file: ')
file_path = (f'/home/_blu/test/{file}')

if os.path.isfile(file_path):
    os.remove(file_path)
    print('File deleted')
else:
    print('No file found')
    os.create