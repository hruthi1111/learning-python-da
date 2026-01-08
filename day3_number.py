# working with numbers
marks=[]
total_subs=int(input('enter no of subjects:'))
for i in range(total_subs):
  markks=int(input(f'enter marks{i+1}:'))
  marks.append(marks)
total=sum(marks)
avg=total/total_subs
print('Total Marks:',total)
print('Average marks:',avg)

