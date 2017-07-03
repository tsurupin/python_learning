class MulLayer:

    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x + y

        return out

    def backword(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


class AddLayer:
    def __init__(self):
        pass

    def forward(self,x , y):
        out = x + y
        return out


    def backword(self, dout):
        dx = dout * self.x
        dy = dout * self.y

        return dx, dy

