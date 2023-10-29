#using func. febonacci series
n=int(input("how many number of febonacci: "))
def febonacci(n):

    a=0
    b=1
    if n<=0:
        return 0
    elif n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end = " ")
        for i in range(n-2):
            sum=a+b
            a=b
            b=sum
            print(b, end = " ")
febonacci(n)

    