m = float(input('Enter number of payments per period: '))
t = float(input('Enter number of years: '))
ytm = float(input('Enter the yield to maturity in decimals term: '))
fv = float(input('Enter the face value of bond: '))
c = float(input('Enter the coupon rate in decimals: '))


bondPrice = ((fv*c/m*(1-(1+ytm/m)**(-m*t)))/(ytm/m)) + fv*(1+(ytm/m))**(-m*t)


print('The price of the bond is: %.2f' %bondPrice)
