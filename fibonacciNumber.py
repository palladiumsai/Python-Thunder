n = int(input("Number of terms: "))
term1, term2 = 0, 1
if n<=0:
  printf("Please enter a value more than 0!")
elif n==1:
  print("The ", n,"th fibonacci number is: ", term1, sep='')
else:
   count=0
   while count < nterms:
       nth_term = term1 + term2
       term1 = term2
       term2 = nth_term
       count += 1
  print("The ", n,"th fibonacci number is: ", nth_term, sep='')
