class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self,x):
        if x > 0:
            self.x = x

