class Point3D():
    def __init__(self, x=0, y=0, z=0):
        self.pnt = [x, y, z]

    __slots__ = ['pnt', 'table']

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def __setcoordx(self, x):
        if Point3D.__checkValue(x):
            pnt = self.pnt
            pnt[0] = x
            self.pnt = pnt
        else:
            print(f'Value {x} in not number')



    def __getcoordx(self):
        return self.pnt[0]

    def __getattribute__(self, key):
        if key == '_Point3D__getcoordx':
            print(f'Attribute {key} is Privat')
            raise AttributeError
        else:
            return object.__getattribute__(self, key)

    def setcoordx(self, x):
        self.__setcoordx(x)

    def getcoordx(self):
        return self.__getcoordx()

    def __del__(self):
        pass
        print('delete smt')

    def set_coords(self, *args):
        length = len(args)
        pnt = self.pnt
        for i in range(length):
            pnt[i] = args[i]
        self.pnt = pnt


if __name__ == '__main__':
    pt = Point3D(45, 12, 13)
    print(f'point coordinates0 = {pt.pnt}')
    pt.set_coords(9)
    print(f'point coordinates1 = {pt.pnt}')
    Point3D.set_coords(pt, 4, 5)
    pt.setcoordx(34)

    print(f'point coordinates2 = {pt.pnt}')
    print(f'coordinate x = {pt.getcoordx()}')
    print(f'coordinate x = {pt._Point3D__getcoordx()}')
    pt.table = 145