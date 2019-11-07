from random import randint


ans = randint(1, 100+1)
print(ans)
guess = int(input("Hi, guess the num(1~100)"))
if ans == guess:
    print('correct')
else:
    print('fail')
