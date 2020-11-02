def longest_word(filename):
    with open('zen-of-python.txt', "r") as reader:
        words = reader.read().split()

    max_length = len(max(words, key=len))
    return [word for word in words if len(word) == max_length]

print(longest_word('zen-of-python.txt'))

count = len(open('zen-of-python.txt').readlines())

print(count)









