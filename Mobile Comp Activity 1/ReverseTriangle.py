def reverse_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

if __name__ == "__main__":
    size = int(input("Enter the size of the reverse triangle: "))
    reverse_triangle(size)
