def computepay(h,r):
  if h<=40:
    pay=h*r
    return pay
  if h>40:
    pay=((h-40)*(r*1.5)+(40*r))
    return pay 


h = input("Enter Hours:")
r = input ("Enter Rate:")
h=float(h)
r=float(r)

p = computepay(h,r)
print (p)
