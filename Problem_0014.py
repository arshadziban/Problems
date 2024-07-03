#Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
def test():
    import random
    data_list =['a', 'e', 'i', 'o', 'u']
    random.shuffle(data_list)
    print("".join(data_list))
test()
    