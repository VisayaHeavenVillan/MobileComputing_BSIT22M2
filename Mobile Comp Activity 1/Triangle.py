def triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

if __name__ == "__main__":
    size = int(input("Enter the size of the triangle: "))
    triangle(size)
