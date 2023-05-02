# Обертка в теги

# def tags_s():
#     def inner(s):
#         return '<h1>' + s + '</h1>'
#
#     return inner
#
#
# s = input()
# h = tags_s()
# print(h(s))

#dict_xo = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
# print(dict_xo)
# print(*dict_xo)
dict_xo_pole = {1:'1 |', 2:' 2 |', 3:' 3', 4:'4 |', 5:' 5 |', 6:' 6', 7:'7 |', 8:' 8 |', 9:' 9'}
for v in dict_xo_pole.values():
    if v == ' 3':
        print(v, end='\n')
        print('=========')
    elif v == ' 6':
        print(v, end='\n')
        print('== === ==')
    else:
        print(v, end='')
