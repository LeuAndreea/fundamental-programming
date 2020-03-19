n =  input("n=")
n = int(n)

if n % 2 != 0:
    i = n- 1
else:
    i = n
s = 0
while (i != 0):
    s += i
    i -= 2
print ("The sum of even numbers up to ",n, "is ",s)
