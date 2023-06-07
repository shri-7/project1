class numoperation():
    def __init__(self,num):
        self.num=num
    def is_valid(self):
        if self.num > 0:
            print("input number is valid : ",self.num)
        else:
            print("entered number is negetive or zero")
            exit()
    def oddeven(self):
        if self.num%2==0:
            print(self.num,"is even")
        else:
            print(self.num,"is odd")
    def sqrt(self):
        print("the square root of ",self.num ,"is :",self.num**2)
        return
    def cbrt(self):
        print("the cube root of ",self.num ,"is :",self.num**3)
        return
    def fact(self):    
        n=1
        fact=1
        if self.num <1:
            return 1
        else:
            while self.num>=n:
                fact=fact*n
                n=n+1
            print("factrial of ",self.num,"is :", fact)
        return
    def fib(self): 
        num1, num2 = 0, 1
        if self.num <= 0:
            print("Please enter a positive integer.")
            return
        print("fibonacci series of",self.num,"is :")
        for i in range(0,self.num):
            print(num1, end=" ")
            num1, num2 = num2, num1 + num2
        print()
    def funcl(self):
        fn=numoperation(self.num)
        fn.is_valid()
        fn.oddeven()
        fn.sqrt()
        fn.cbrt()
        fn.fact()
        fn.fib()
        return
n=int(input("enter the number of you want do mathemathecal operation:"))
op=numoperation(n)
while True:
    print("choices 1.checknum 2.evenodd  3.sqrt 4.cuberoot\n 5.factoirial 6.fibonacci 7.all operations 8.exit")
    ch=int(input("enter your choice :"))
    if ch==1:
        op.is_valid()
    elif ch==2:
        op.oddeven()
    elif ch==3:
        op.sqrt()
    elif ch==4:
        op.cbrt()
    elif ch==5:
        op.fact()
    elif ch==6:
        op.fib()
    elif ch==7:
        op.funcl()
    else:
        break