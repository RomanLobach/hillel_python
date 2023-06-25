# Доопрацюйте класс Triangle зі свого попереднього дз.
#
# Реалізуйте перевірку даних на те що вершини є Point за допомогою property.
# Реалізуйте ітератор по вершинам трикутника


class WrongCoordinateType(Exception):
    """Exception raised for errors in the input point coordinates.
    This class is not necessary, just an experiment.

    Attributes:
        coordinate -- input coordinate which caused the error
        message -- explanation of the error
    """
    coordinate = None

    def __init__(self, coordinate, message="Coordinate type is not <int> or <float>."):
        self.salary = coordinate
        self.message = message
        super().__init__(self.message)


class WrongPointType(Exception):
    """Exception raised for errors in the input line and triangle points.
    This class is not necessary, just an experiment.

    Attributes:
        point -- input coordinate which caused the error
        message -- explanation of the error
    """
    point = None

    def __init__(self, point, message="Argument is not a child of class Point."):
        self.salary = point
        self.message = message
        super().__init__(self.message)


class Point:
    x_coord = None
    y_coord = None

    def __init__(self, x, y):
        def check_coord_type_handle(coord):
            """Input/Output function, that checking type of coordinate.
            If type of coordinate is <int> or <float> it returns coordinate.
            Else it will raise an WrongCoordinateType error.

            Attributes:
                coord ( any ) -- input checking coordinate
            Returns:
                coord ( int | float ) -- checked output coordinate
            """
            if isinstance(coord, int) or isinstance(coord, float):
                return coord
            else:
                raise WrongCoordinateType(coord)

        self.x_coord = check_coord_type_handle(x)
        self.y_coord = check_coord_type_handle(y)

    def __str__(self):
        return f'Point ({self.x_coord},{self.y_coord})'


class Line:
    begin_point = None
    end_point = None

    def __init__(self, begin, end):
        def check_point_type_handle(point):
            """Input/Output function, that checking the instance point.
            If instance of point is Point it returns point.
            Else it will raise an WrongPointType error.

            Attributes:
                point ( any ) -- input checking coordinate
            Returns:
                coord ( <class '__main__.Point'> ) -- checked output coordinate
            """

            if isinstance(point, Point):
                return point
            else:
                raise WrongPointType(point)

        self.begin_point = check_point_type_handle(begin)
        self.end_point = check_point_type_handle(end)

    def __str__(self):
        begin_point_coord = f'({self.begin_point.x_coord}, {self.begin_point.y_coord})'
        end_point_coord = f'({self.end_point.x_coord}, {self.end_point.y_coord})'

        return f'Line ({begin_point_coord}, {end_point_coord}). Length is {self.length}'

    @property
    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5


class Triangle:
    limit = 2
    current = -1

    def __init__(self, point_a, point_b, point_c):
        self.points = (point_a, point_b, point_c)

    def __str__(self):
        return f'Triangle {self.points[0]}, {self.points[1]}, {self.points[2]}. Area is {self.area}'

    def __iter__(self):
        self.current = self.__class__.current

        return self

    def __next__(self):
        self.current += 1
        if self.current > self.limit:
            raise StopIteration

        return self.points[self.current]

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points_tuple):

        for checking_point in points_tuple:
            if not isinstance(checking_point, Point):
                raise WrongPointType(checking_point)

        self._points = points_tuple

    @property
    def area(self):
        side_ab = Line(self.points[0], self.points[1]).length
        side_bc = Line(self.points[1], self.points[2]).length
        side_ca = Line(self.points[2], self.points[0]).length

        half_perimetr = 0.5 * (side_ab + side_bc + side_ca)

        area = (half_perimetr * (half_perimetr - side_ab) * (half_perimetr - side_bc) * (
                half_perimetr - side_ca)) ** 0.5

        return area


p1 = Point(0, 0)
p2 = Point(0, 4)
p3 = Point(3, 0)
p4 = Point(-1, -1)
p5 = Point(-4, -1)
p6 = Point(-1, -5)

l1 = Line(p1, p2)
l2 = Line(p2, p3)
l3 = Line(p3, p1)

t1 = Triangle(p1, p2, p3)
t2 = Triangle(p4, p5, p6)
t3 = Triangle(p1, p4, p3)
t4 = Triangle(p4, p2, p6)

print('points of t1')
for point in t1:
    print(point)

print('points of t2')
for point in t2:
    print(point)

print('points of t3')
for point in t3:
    print(point)

print('points of t4')
for point in t4:
    print(point)

print('p1 ', p1)
print('p2 ', p2)
print('p3 ', p3)
print('l1 ', l1)
print('l2 ', l2)
print('l3 ', l3)
print('t1 ', t1)
print('t2 ', t2)
print('t3 ', t3)
print('t4 ', t4)
