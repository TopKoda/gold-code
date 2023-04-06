"""
Count substrings in string.  This includes overlapping strings.

Got answer here: https://stackoverflow.com/questions/8899905/count-number-of-occurrences-of-a-substring-in-a-string

Johnny Mac - 06 Apr 2023
"""
def count_substring(string, sub_string):
    l=len(sub_string)
    count=0
    if 1 <= len(string) <= 200:
        for i in range(len(string)-len(sub_string)+1):
            if(string[i:i+len(sub_string)] == sub_string ):      
                count+=1
        return count  
    else:
        print("Please keep string between 1 and 200 characters.")
      
#def main():
#    string = input("Please enter a string btw 1 and 200 chars: ").strip()
#    sub_string = input("Please enter a sub string: ").strip()
#    
#    count = count_substring(string, sub_string)
#    print(count)
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)