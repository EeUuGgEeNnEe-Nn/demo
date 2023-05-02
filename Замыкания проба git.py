# Обертка в теги

def tags_s():
    def inner(s):
        return '<h1>' + s + '</h1>'

    return inner


s = input()
h = tags_s()
print(h(s))
