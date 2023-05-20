def factorial(n):
   assert isinstance(n, int), "n should be an int"
   assert n >= 0            , "n should not be negative"
   fat = 1
   for i in range(2, n+1):
      fat = fat * i
   return fat