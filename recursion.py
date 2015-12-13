import random
__author__ = 'wilsonincs'



def fib(n):
    if n <= 1:   #made it so if n is less or equals to 1 , the return value is 1
        return 1
    else:
        return fib(n-1) + fib(n-2)


def gcd(a,b):
    return gcd(b,a%b) if b else abs(a)


def compareTo(s1,s2):
    if s1 < s2:
        return random.randint(-100,-1)
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return random.randint(1,100)
    else:
        print "something is wrong"


#Tests

print fib(17)

print gcd(7,10)


s1 = "Redbull rules!"
s2 = "Coffee hits the spot!"
print compareTo(s1,s2)