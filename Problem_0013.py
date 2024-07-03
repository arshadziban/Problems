#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def test_data():
    data = input("Please enter your data:").split(',')
    if len (data) == len(set(data)):
        print("unique")
    else:
        print("Not Unique")
test_data()






    