# t, count =3
# e, count =1
# s, count =2
# r, count =1
# i, count =1
# n, count =1
# g, count =1
def print_dups(Str):
    char_list = list(Str)
    char_list.sort()
    i = 0

    while i < len(char_list):
        count = 1
        while i < len(char_list)-1 and char_list[i] == char_list[i+1]:
            count += 1
            i += 1
        
        if count > 1:
            print(char_list[i], ", count = ", count)
        i += 1

Str = 'test string'
print_dups(Str)