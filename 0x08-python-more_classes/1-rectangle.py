#!/usr/bin/python3
class Rectangle:
    """
    Rectangle class with private attributes width and height.
    """
    def __init__(self, width=0, height=0):
         """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
         self.width = width
         self.height = height

    @property
    def __width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width
    
    @__width.setter
    def __width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        - value (int): The width value to set.

        Raises:
        - TypeError: If the width is not an integer.
        - ValueError: If the width is less than 0.
        """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def __height(self):
        """
        Gets the height of the rectangle.

        Parameters:
        - value (int): The height value to set.

        Raises:
        - TypeError: If the height is not an integer.
        - ValueError: If the height is less than 0.
        """
        return self.__height
    
    @__height.setter
    def __height(self, value):
         """
        Sets the height of the rectangle.

        Parameters:
        - value (int): The height value to set.

        Raises:
        - TypeError: If the height is not an integer.
        - ValueError: If the height is less than 0.
        """
         if not isinstance(value, int):
              raise TypeError("height must be an integer")
         
         elif value < 0:
              raise ValueError("height must be >= 0")
         else:
             self.__height = value
