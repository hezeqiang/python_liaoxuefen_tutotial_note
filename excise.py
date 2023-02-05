l1=[1,1,2]
l2=[1,1]
sum_number=[]
over10=0
while l1 or l2:
    if l1:
        number1=l1.pop()
    else:
        number1=0
    if l2:
        number2=l2.pop()
    else:
        number2=0

    sum=number1+number2
    if over10==1:
        sum=sum+1
    if sum>10:
        over10=1
        sum=sum-10
    else:
        over10=0

    sum_number.append(sum)

print(sum_number)


