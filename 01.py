"""
Create an isosceles triangle by taking its height.
M.A.B
"""

#! This class creates a triangle
class IsoscelesTriangle:
    """
    isosceles_triangle
    
    input:
        height ---> int
    """
    def __init__(self, height=int) -> None:
        self.height= height
        #? base pattern :
        #? height = base ===>  1 = 1    2 = 3    3 = 5    n = n+n-1
        self.base= self.height*2-1
        
    def show_triangle(self) -> None:
        """
        To print triangle
        """
        temp= self.base//2
        star= 1
        for i in range(self.height):
            print(temp*' ' + star*'*')
            temp-= 1
            star+= 2
 
#--------------------------------------------------------------------------------------------------------------------------------           
#==========================================================test==================================================================
height= int(input('Enter height= '))

triangle= IsoscelesTriangle(height)
triangle.show_triangle()