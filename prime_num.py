import time
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
    print(f'Число {a[-1]}')
t1 = time.process_time()
what_prime(100000)
t2 = time.process_time()
print(f'Вычисление 100000х простого числа заняло {t2-t1}') 


