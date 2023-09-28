
numbers=[]
if len(numbers)!=0:
    k=(sum(numbers))//len(numbers)
    print('Среднее значение', k)
else:
    print('0')

print(sum(numbers)/len(numbers)) if numbers else print(0)
a=int(input()); b=int(input()); c=int(input())
D=b**2-4*a*c
if D==0 and a!=0 and b!=0:
    print((-b)/2*a)
if a==0 and b==0 and c==0:
    print('X любое число')
if D<0 or c!=0:
    print('Нет корней')
if D>0:
    print((-b+D**(1/2))/2*a)
    print((-b-D**(1/2))/2*a)
jhjh5434