def diamond(n):
    if (n % 2) == 0 or n < 0:
        return None
    else:
        for i in range(1, n, 2):
            print(" "*(n//2-i//2), "*"*i)
        for i in range(n, 0, -2):
            print(" "*(n//2-i//2), "*"*i)
