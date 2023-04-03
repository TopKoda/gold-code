"""
Simple split and join function

Johnny Mac - 03 Apr 2023
"""
def split_and_join(line):
    split_line = line.split(" ")
    join_line = "-".join(split_line)
    return join_line
    
def main():
    line = input("Please enter a sentence: ")
    result = split_and_join(line)
    print(result)
    
if __name__ == '__main__':
    main()