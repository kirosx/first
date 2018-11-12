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
print('Этот скрипт находит n-ое простое число и выводит время, необходимое для его нахождения')
n=int(input('Enter N:'))
t1 = time.process_time()
what_prime(n)
t2 = time.process_time()
print(f'Вычисление {n} простого числа заняло {t2-t1} секунд') 


