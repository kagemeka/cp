def makeArrayConsecutive2(statues):
    a = statues
    return max(a) - min(a) + 1 - len(a)
