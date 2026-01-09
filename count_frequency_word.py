def count_word_frequency(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;"()[]{}')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                # word_count[word] = word_count.get(word, 0) + 1
    return word_count
    
file_path = 'sample.txt'
frequency = count_word_frequency(file_path)
print(frequency)