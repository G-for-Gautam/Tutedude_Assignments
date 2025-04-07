list1=[i for i in range(1, 11)]
print('original list: ',list1)

list_part= list1[:5]
print('extracted first five elements: ',list_part)

list_part.reverse()
print('reversed extracted element: ',list_part)
