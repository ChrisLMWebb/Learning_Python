#simple program to calculate the coefficients of a binomial

#Row n
n = int(input('Input the exponent, n, of the binomial you wish to calculate.\n'))

while n < 0 or n == 0:
    if n < 0:
        print('Factorials do not exist for negative numbers.')
    if n == 0:
        print('The factorial of 0 is 1.')
    n = int(input('Try again:'))

#calculate n factorial
nfact = 1
for i in range(1, n + 1):
    nfact = nfact*i

#Column r
r = int(input('Input the column, r, of the coefficient you want.\n'))
while r < 0 or r > n:
    print ('Sorry, r must be 0, 1, 2, 3, ..., n')
    r = int(input('Try again:'))

#calculate r factorial
rfact = 1
for j in range(1, r + 1):
    rfact = rfact*j

#calculate (n-r) factorial
nmr = n - r
nmrfact = 1
for h in range(1, nmr + 1):
    nmrfact = nmrfact*h

#put it all together
denom = rfact*nmrfact
nCr = int(nfact/denom)
print('nCr =', nCr)
