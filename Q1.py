a=int(input("income: "))
if a<1000 :
 d=a
elif 1000< a <= 2500:
 b=a*.1
 d=a-b
elif 2500< a <= 4000:
 b=a*.15 
 d=a-b
elif 4000< a <= 6000:
 b=a*.2
 d=a-b
elif 8000< a:
 b=a*.3
 d=a-b
print(f"net incom={d}")