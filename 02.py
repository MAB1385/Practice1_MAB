"""
Detector of prime number.
M.A.B
"""


def prime_number(number=int) -> bool:
    """
    To check is prime number.
    """
    temp= 0
    for i in range(1,number+1):
        if number%i == 0:
            temp+= 1
    if temp == 2:
        return True
    return False

#--------------------------------------------------------------------------------------------------------------------------------           
#==========================================================test==================================================================
number= int(input('Enter number= '))

if prime_number(number):
    print('prime')
else:
    print('no prime')