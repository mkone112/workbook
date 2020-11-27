#?позволяет убедиться что геттеры вызываются косвенно для обеспечения переопределения методам подклассов вызываемых через св-во
#возможно это пример шаблонного метода
    import math
    ...
    class Square:
        """A square.
        :property area: a writable area
        :property perimeter:read-only perimeter
        
        To use:
        sq = Square(3)
        sq.area             # 9
        sq.perimeter        # 12
        sq.area = 16
        sq.side             # 4
        sq.perimeter        # 16
        """
        
        def __init__(self, side):
            self.side = side
        
        def __get_area(self):
            """Calculates the 'area' property."""
            return self.side ** 2
        
        def ___get_area(self):
            """Indirect accessor for 'area' property."""
            return self.__get_area()
        
        def __set_area(self, area):
            """Sets the 'area' property."""
            self.side = math.sqrt(area)
        
        def ___set_area(self, area):
            """Indirect setter for 'area' property."""
            self.__set_area(area)
        
        area = property(___get_area, ___set_area,
                        doc="""Gets or sets the area of the square.""")
        
        @property
        def perimeter(self):
            return self.side * 4