def diamond(n):
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)
    for i in range(n - 2, 0, -2):
        print(' ' * ((n - i) // 2) + '*' * i)

if __name__ == "__main__":
    size = int(input("Enter an odd number for the diamond size: "))
    if size % 2 == 0:
        print("Please enter an odd number.")
    else:
        diamond(size)
