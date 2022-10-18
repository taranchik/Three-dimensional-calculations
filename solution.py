class threedim(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def threedimdistance(i, j):
    deltaxsquared = (i.x - j.x) ** 2
    deltaysquared = (i.y - j.y) ** 2
    deltazsquared = (i.z - j.z) ** 2
    return (deltaxsquared + deltaysquared + deltazsquared) ** 0.5


def threedimmean(threedimlist):
    xvalues = []
    yvalues = []
    zvalues = []
    for point in threedimlist:
        xvalues.append(point.x)
        yvalues.append(point.y)
        zvalues.append(point.z)
    xmean = sum(xvalues)/float(len(xvalues))
    ymean = sum(yvalues)/float(len(yvalues))
    zmean = sum(zvalues)/float(len(zvalues))
    return threedim(xmean, ymean, zmean)


def threedimSD(threedimlist):
    squareddistances = []
    listmean = threedimmean(threedimlist)
    for point in threedimlist:
        squareddistances.append(threedimdistance(point, listmean) ** 2)
    return (sum(squareddistances)/float(len(squareddistances)) ** 0.5)


lineone = threedim(1, 1, 1)
linetwo = threedim(1, 1, 0.5)
linethree = threedim(0, 0, 0)
linefour = threedim(0.5, 0.5, 0.5)


threedimdistance(lineone, linetwo)


listoflines = [lineone, linetwo, linethree, linefour]
threedimmean(listoflines)
threedimSD(listoflines)
