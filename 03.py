"""
Find prime numbers before 1000.
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

for i in range(1,1000):
    if prime_number(i):
        print(i)
    else:
        pass