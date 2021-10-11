def split_words(line):
    words = line.split(' ')
    return words

def sort(word):
    return sorted(word)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(line):
    word = line.pop(-1)
    print(word)

def sort_line(line):
    words = split_words(line)
    return sort(words)

def print_last_first(line):
    words = split_words(line)
    print_first_word(words)
    print_last_word(words)

def print_last_first_sorted(line):
    words = sort_line(line)
    print_first_word(words)
    print_last_word(words)
























