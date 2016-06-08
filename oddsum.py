odd=int(input(""))
if odd>0:
  sum=0
    for i in range(1,odd+1):
     if i%2!=0:
       sum+=i
   print(sum)
else:
   print("Invalid number")
