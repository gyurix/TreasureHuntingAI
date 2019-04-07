from random import randint


class Map:
    def __init__(self, lines):
        line = (lines[0].split(' ')) + (lines[1].split(' '))
        self.maxx, self.maxy, self.x, self.y = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        self.rewards = set()
        for d in lines[2].split(' '):
            d2 = d.split(';')
            self.rewards.add((int(d2[0]), int(d2[1])))

    def collect(self, dirs):
        out = 0
        x, y = self.x, self.y
        rewards = set(self.rewards)
        for d in dirs:
            d = d & 3
            oldX = x
            oldY = y
            was = len(rewards)
            if d == 0:  # UP
                if y != 0:
                    y -= 1
            elif d == 1:  # DOWN
                if y != self.maxy - 1:
                    y += 1
            elif d == 2:  # LEFT
                if x != 0:
                    x -= 1
            elif d == 3:  # RIGHT
                if x != self.maxy - 1:
                    x += 1
            if oldX != x or oldY != y:
                rewards.discard((x, y))
                out += was - len(rewards)
        return out


class Program:
    def __init__(self, pr=None):
        self.pos = 0
        self.ex_lines = 0
        if pr is None:
            self.pr = [randint(0, 255) for n in range(64)]
        elif type(pr) == str:
            self.pr = [int(n, 2) for n in pr.split(' ')]
        else:
            self.original = pr
            self.pr = pr.pr[:]

    def has_next(self):
        return self.ex_lines < 500 and self.pos < 64

    def next(self):
        self.ex_lines += 1
        d = self.pr[self.pos]
        bit0 = d & 128
        bit1 = d & 64
        adr = d & 63
        out = -1
        if bit0:
            if bit1:
                out = self.pr[adr]
            else:
                self.pos = adr - 1
        else:
            self.pr[adr] = (self.pr[adr] + (255 if bit1 else 1)) & 255
        self.pos += 1
        return out

    def execute(self):
        self.pos = 0
        self.ex_lines = 0
        result = []
        while self.has_next():
            d = self.next()
            if d != -1:
                result.append(d)
        self.result = result

    def clone(self):
        return Program(self)

    def __str__(self):
        return str(self.pr)

    def __repr__(self):
        return str(self.pr)
