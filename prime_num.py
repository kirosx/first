def prime_or_not(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def what_prime(number):
    a=[]
    i=1
    while len(a)<=number:
        if prime_or_not(i):
            a.append(i)
        i+=1
    print(a[-1])
