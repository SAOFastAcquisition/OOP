class Point3D():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        print('smt')

    if True:
        def __del__(self):
            pass
            print('delete smt')

    def setCoords(self, x = 2, y = 3):
        self.x = x
        self.y = y
        print('set_Coord', self.__dict__)


if __name__ == '__main__':
    pt = Point3D()
    print(pt.x, pt.y)
    # pt.set_coord()
    Point3D.setCoords(pt, 4, 5)

    print(pt.__dict__)
