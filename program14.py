def prime_numbers(n):
    for num in range(2,n+1):
       for i in range(2,num):
           if num%i==0:
            break
       else:
           yield num

n=int(input("Enter n:"))

for prime in prime_numbers(n):
    print(prime,end=" ")
