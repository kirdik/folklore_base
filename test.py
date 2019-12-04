a1 = [['zig', 'zag'], ['one', 'two'], ['din', 'don']]
a2 = [['zig', 'zag'], ['super', 'puper'], ['dalay', 'lama']]

for i in a1:
    for a in a2:
        if i == a:
            a2.remove(i)

print(a2)





