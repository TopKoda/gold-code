"""
Little loop demo.

Johnny Mac - 05 Apr 2023
"""
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20:
        i = 0
        while i < n:
            print(i * i)
            i +=1
    else:
        print("Number must be between 1 and 20.")