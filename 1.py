a=int(input())
b=int(input())
even_numbers=[i for i in range(a,b+1) if i%2==0]
print(*even_numbers)