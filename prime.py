range = input('Range of prime numbers to be generated?')
try:
    range = int(range)
except:
    print('Please input a positive number as range!')
    quit()
count = 2
min = 2

primes = list()
while count<=range:
    not_prime_property = 0
    divisor =  count-1
    while divisor>1:
        x = count%divisor
        if x == 0:
            not_prime_property = not_prime_property+1
        divisor = divisor-1
    if not_prime_property==0:
        primes.append(count)
    count = count +1
print(primes)
# just Testing repository push
