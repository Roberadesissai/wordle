# opening the file in read mode

my_file = open("C:/Users/CodeME/Desktop/VISUAL/WORDLE/wordle.txt", 'r')

# reading the file
data = my_file.read()

word_list = data.split("\n")

if __name__ == "__main__":
    print(word_list)
    my_file.close()
