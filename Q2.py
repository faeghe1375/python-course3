a=int(input())
b=int(input())
c=int(input())
if (c*c == a*a + b*b) or  (b*b == a*a + c*c) or (a*a == c*c + b*b):
 print("right")
else:
print("no right")