

def move(n, source, target, auxillary):
    if n > 0:
        move(n - 1, source, auxillary, target)
        print("Move disk from ", source, " to ", target)
        move(n-1, auxillary, target, source)


move(3, "left", "middle", "right")
