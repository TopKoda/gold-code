"""
Super simple print full name function challenge.
Johnny Mac - 03 Apr 2023
"""

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    output = "Hello " + str(first) + " " + str(last) + "! You just delved into python."
    print(output)

def main():
  firstname = input("Please input your first name: ")
  lastname = input("Please input your last name: ")
  print_full_name(firstname, lastname)

if __name__ == '__main__':
    main()