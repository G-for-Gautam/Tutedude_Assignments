
take1=input('enter something to write: ')
file=open('output.txt','w')
file.write(take1)
file.close()
print('file written...')

take2=input('enter something to append: ')
file=open('output.txt','a')
file.write(take2)
file.close()
print('file appended...')

file=open('output.txt','r')
readed_data=file.read()
print('final file output...')
print(readed_data)
file.close()
