sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
    print("Length:", len(longest_word))
else:
    print("No words entered")
