# Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу
# int або float Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
# тільки обʼєкти класу Point Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу
# Point). Реалізуйте перевірку даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника. Для
# обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)


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

        return f'Line ({begin_point_coord}, {end_point_coord}). Length is {self.get_length()}'

    def get_length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5


class Triangle:
    point_a = None
    point_b = None
    point_c = None

    def __init__(self, point_a, point_b, point_c):
        # повтор такоїж функції з класу Line.
        # DRY не виконано. Інкапсуляція - виконана.
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

        self.point_a = check_point_type_handle(point_a)
        self.point_b = check_point_type_handle(point_b)
        self.point_c = check_point_type_handle(point_c)

    def __str__(self):
        return f'Triangle {self.point_a}, {self.point_b}, {self.point_c}. Area is {self.get_area()}'

    def get_all_length(self):
        def one_length_handle(point_start, point_end):
            k1 = point_start.x_coord - point_end.x_coord
            k2 = point_start.y_coord - point_end.y_coord

            return (k1 ** 2 + k2 ** 2) ** 0.5

        return {
            'side_ab': one_length_handle(self.point_a, self.point_b),
            'side_bc': one_length_handle(self.point_b, self.point_c),
            'side_ca': one_length_handle(self.point_c, self.point_a),
        }

    def get_area(self):
        side_ab, side_bc, side_ca = self.get_all_length().values()

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
