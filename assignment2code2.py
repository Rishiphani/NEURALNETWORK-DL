def count_words(line):
    word_count = {}
    words = line.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def main():
    input_file_path = "input.txt"
    output_file_path = "output.txt"

    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    with open(output_file_path, 'w') as output_file:
        for line in lines:
           
            print(line.strip())
            output_file.write(line)

           
            word_count = count_words(line)

        
            print("Word_Count:")
            output_file.write("Word_Count:\n")

            for word, count in word_count.items():
                print(f"{word}: {count}")
                output_file.write(f"{word}: {count}\n")

            print("\n")
            output_file.write("\n")

if __name__ == "__main__":
    main()
