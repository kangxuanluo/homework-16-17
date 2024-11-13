homework 16
def f(a,b,c):
    if a == 0:
        if b==0:
            print("error")
        else:
            print("x=",-b/c)
    else:
        if b**2-4*a*c<0:
            print("error")
        elif b**2-4*a*c==0:
            print("x=",(-b+(b**2-4*a*c)**0.5)/(2*a))
        elif b**2-4*a*c>0:
            print("x1=",(-b+(b**2-4*a*c)**0.5)/(2*a))
            print("x2=",(-b-(b**2-4*a*c)**0.5)/(2*a))

a=int(input("a:"))
b= int(input("b:"))
c=int(input("c:"))
f(a,b,c)
quit()



homework 17
x=int(input("give me a 4-digit number that is even and does not end with a 0"))
if  x%2!=0:
    print(x,"IS BAD BECAUSE IT IS NOT EVEN ")
elif x%10==0:
    print(x," IS BAD BECAUSE IT ENDS WITH 0 ")
elif x<1000:
    print(x," IS BAD BECAUSE IT IS NOT 4 DIGITS ")
elif x>9999:
    print(x," IS BAD BECAUSE IT IS NOT 4 DIGITS")
else:
    print("thank you")
quit()
