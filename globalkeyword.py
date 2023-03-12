#globale variable
c = 2

def add():
    global c
    c = c + 2
    print(c)
add()