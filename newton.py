def newton(x, accuracy=0.001):
    """Compute the square root of the number x using Newton's method"""
    G = x/2
    while G ** 2 - x > 0.001:
        G = G - ((G**2 - x) / (2*G))
    return (round(G,3))
