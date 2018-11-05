n =int(input("enter number of values "))
x=[]
for i in range(0,n):
 a=int(input("enter value %d " %(i+1)))
 x.append(a)
print(x)

b=0
for i in range(0,n):
 a = x[i]
 b= b+a
 c=b/n

e=0
for i in range (0,n):
 d = (c-x[i])*(c-x[i])
 e=e+d

variance1= (e/n)
print("population variance is %d" %(variance1))
variance2 = (e/(n-1))
print("sample variance is %d" %(variance2))

sd1= (e/n)**0.5
print("population standard deviation is %d" %(sd1))
sd2 = (e/(n-1))**0.5
print("sample standard deviation is %d" %(sd2))