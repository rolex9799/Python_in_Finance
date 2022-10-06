# *Compounding

# *store the inputs

from numpy import number
from pendulum import time


principal = float(input('Enter the pricipal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time in years: '))
number = float(input('Enter the number of timer you want the interest to be compunded: '))


 
#calculate total amount
amount = principal * ((1 + ((rate/100)/number))** (number*time))

#calculate compound interest

ci = amount - principal 

#display result

print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)
