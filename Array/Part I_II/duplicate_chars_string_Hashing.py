# t, count =3
# e, count =1
# s, count =2
# r, count =1
# i, count =1
# n, count =1
# g, count =1
def print_dups(Str):
    count = {}

    for i in range(len(Str)):
        if (Str[i] in count):
            count[Str[i]] += 1
        else:
            count[Str[i]] = 1
    
    for item1, item2 in count.items():
        if(item2>0 and item1 !=" "):
            print(item1 + ", count =" + str(item2))

Str = 'test string'
print_dups(Str)