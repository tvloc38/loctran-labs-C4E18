import random

life = 3
while True:
    x = random.randint(1,10)
    y = random.randint(1,10)

    op = random.choice(["+" , "-" , "*" , "/" ])
    result = -99999 

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        if (y != 0):
            result = x / y
    error = random.randint(-1,1)
    # error = random.choice([-1, 0, 1])

    print("{0} {1} {2} = {3}".format(x,op,y,result+error))
    user = input("Y/N: ").lower()
    if error == 0:
        if user == "y":
            print("Yes")
            print("*" * 20)
        elif user == "n":
            life -= 1
            print("Life: {0}".format(life))
            print("*" * 20)
            if life == 0:
                break
        else:
            break
    else:
        if user == "y":
            life -= 1
            print("Life: {0}".format(life))
            if life == 0:
                break
            print("*" * 5)
        elif user == "n":
            print("Yes")
            print("*" * 5)
        else:
            break
    


