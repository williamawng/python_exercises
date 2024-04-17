if __name__ == '__main__':
    N = int(input())
    commands = []
    for i in range(N):
        commands.append(str(input()))
    my_list = []
    for c in commands:
        if c.startswith("insert"):
            temp = c.split()
            if int(temp[-1]):
                my_list.insert(int(temp[-2]), int(temp[-1]))
        elif c.startswith("print"):
            print(my_list)
        elif c.startswith("remove"):
            temp = c.split()
            if (int(temp[-1])):
                my_list.remove(int(temp[-1]))
        elif c.startswith("append"):
            temp = c.split()
            if (int(temp[-1])):
                my_list.append(int(temp[-1]))
        elif c.startswith("sort"):
            my_list.sort()
        elif c.startswith("pop"):
            my_list.pop(len(my_list)-1)
        elif c.startswith("reverse"):
            my_list.reverse()