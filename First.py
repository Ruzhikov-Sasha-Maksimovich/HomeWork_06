mylist= "Напишите программу, удаляющую из алфавит абв е"

def del_some_words(mylist):
    mylist = list(filter(lambda x: 'абв' not in x, mylist.split()))
    return " ".join(mylist)

mylist = del_some_words(mylist)
print(mylist)