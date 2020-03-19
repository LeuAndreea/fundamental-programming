n = input("n=")
n = int(n)

if (n==0 | n==1):
    print (n,"is not prime.")
elif (n%2 == 0):
    if (n == 2):
        print(n,"is prime.")
    else:
        print(n,"is not prime.")
else:
    div = 3;
    while (div*div <= n):
        if (n % div == 0):
            print(n,"is not prime.")
            break
        div += 2
    if (n%div != 0):
        print(n,"is prime.")
