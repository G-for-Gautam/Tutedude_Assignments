try:
    student_data={'abhishek':34,'rohan':56,'gautam':88,'divya':78,'dhairya':79}
    name=input('Enter student name : ')
    print(name ,'has scored',student_data[name],'marks')
except KeyError:
    print('ERROR: student not found')
