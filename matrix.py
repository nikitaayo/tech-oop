class Matrix:
    def __init__(self):
        self.size = 0

    def read_from(self, stream):
        self.size = int(stream.readline().rstrip('\n'))

    def write_to(self, stream):
        stream.write(f'\tSize: {self.size}\n')

    def sum(self):
        s = 0
        for item in self.data:
            if isinstance(item, int):
                s += item
            else:
                s += sum(item)
        return s

    @staticmethod
    def create_from(stream, line):
        k = int(line)

        if k == 1:
            matrix = TwoDimArray()
        elif k == 2:
            matrix = Diagonal()
        elif k == 3:
            matrix = Triangle()
        else:
            stream.close()
            raise Exception('Error type')

        matrix.read_from(stream)
        return matrix


class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        for i in range(self.size):
            line = stream.readline().rstrip('\n')
            self.data.append(list(map(lambda x: int(x), line.split())))

    def write_to(self, stream):
        stream.write('\tThis is two-dimensional array\n')
        for row in self.data:
            stream.write(f'\t\t{row}\n')
        stream.write(f'\tSum: {self.sum()}\n')
        super().write_to(stream)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        super().read_from(stream)
        self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

    def write_to(self, stream):
        stream.write('\tThis is diagonal matrix\n')
        stream.write(f'\t\t{self.data}\n')
        stream.write(f'\tSum: {self.sum()}\n')
        super().write_to(stream)


class Triangle(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

    def write_to(self, stream):
        stream.write('\tThis is triangle matrix\n')
        stream.write(f'\t\t{self.data}\n')
        super().write_to(stream)