def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    else:
        return (on + wait) - cap

x = enough(10, 4, 5)
print(x)
