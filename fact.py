def factorial(n):
    if n<2:
      return n
    else:
      return n*(factorial(n-1))
ans=factorial(5)
print(ans)
