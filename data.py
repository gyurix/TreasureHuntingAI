class Map:
    def __init__(self, lines):
        line = lines[0].split(' '), lines[1].split(' ')
        self.maxx, self.maxy, self.x, self.y = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        self.rewards = set([tuple(d) for d in lines[2].split(' ')])


class Program:
    def __init__(self, pr):
        self.pos = 0
        self.ex_lines = 0
        self.pr = [int(n, 2) for n in pr.split(' ')]

    def has_next(self):
        return self.ex_lines < 500 and self.pos < 64

    def next(self):
        self.ex_lines += 1
        d = self.pr[self.pos]
        bit0 = d & 128 == 128
        bit1 = d & 64 == 64
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
        out = []
        while self.has_next():
            d = self.next()
            if d != -1:
                out.append(d)
        return out

    def __str__(self):
        return str(self.pr)
