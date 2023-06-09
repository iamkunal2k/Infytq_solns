#lex_auth_01269446319507046499

def remove_duplicates(value):
    #start writing your code here
    list1 = []
    for i in value:
        if i in list1:
             pass
        else:
             list1.append(i)
             
    result = "".join(list1)
    return result
        
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))