def calculategcd(x, y):
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i               
    return gcd 
def lcm(x,y):
    return (x//calculategcd(x, y))* y
a =int(input("enter first number:"))
b= int(input("enter second number:"))
print ("The gcd of given numbers is : ",calculategcd(a,b)) 
print("The lcm of given numbers is : ",lcm(a,b))
