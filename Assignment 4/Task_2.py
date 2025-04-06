try:
    file=open('sample.txt','r')
    readed_data=file.read()
    print('reading file data...')
    print(readed_data)
    file.close()
except FileNotFoundError:
    print('ERROR: The filename sample.txt not found !')
