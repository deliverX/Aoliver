grades = (88,99,33,22,11,44,55,66,77)
def drop_first_last(grades):
    first,*middle,last = grades
    return sum(middle)/len(middle)

sorted_list = sorted(list(grades),reverse=True)
print (sorted_list)
result = drop_first_last(sorted_list)
print (result)
