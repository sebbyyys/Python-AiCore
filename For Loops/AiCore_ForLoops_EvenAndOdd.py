even_sum = 0
odd_sum = 0


for i in range(1,101):
    if i % 2:
        i += 1
    else:
        even_sum += 1
print(even_sum)     
        
        
        
for i in range(1,101):
    if i % 2:
        odd_sum += 1
    else:
        i += 1
print(odd_sum)