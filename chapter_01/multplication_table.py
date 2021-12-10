"""
Multiplication table printer
"""

def multi_table(variable):
    for i in range(1,11):
        print("{} x {} = {}".format(variable, i, variable*i))
    
def main():
    number = input("Enter a number: ")
    multi_table(int(number))
    
if __name__== "__main__":
    main()