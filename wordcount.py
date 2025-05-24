try:
    filename = input("Enter the name of the text file: ")
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print("Total number of words in the file:", word_count)

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")
