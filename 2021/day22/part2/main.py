class Dimension:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    
    def __len__(self):
        return self.end - self.begin
    
    def intersect(self, other):
        if self.end <= other.begin or other.end <= self.begin:
            return Dimension(0, 0)
        return Dimension(max(self.begin, other.begin), min(self.end, other.end))

class Cuboid:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.voids = []

    def volume(self):
        return len(self.x) * len(self.y) * len(self.z) - sum(void.volume() for void in self.voids)

    def intersect(self, other):
        return Cuboid(self.x.intersect(other.x), self.y.intersect(other.y), self.z.intersect(other.z))

    def subtract(self, other):
        new_void = self.intersect(other)
        if new_void.volume() == 0:
            return
        for void in self.voids:
            void.subtract(new_void)
        self.voids.append(new_void)

cuboids = []

for line in open('input.txt').readlines():
    on, line = line.split(' ')
    dims = []
    for dim in line.split(','):
        begin, end = map(int, dim.split('=')[1].split('..'))
        dims.append(Dimension(begin, end + 1))
    new_cuboid = Cuboid(*dims)
    for cuboid in cuboids:
        cuboid.subtract(new_cuboid)
    if on == "on":
        cuboids.append(new_cuboid)

print(sum(cuboid.volume() for cuboid in cuboids))
