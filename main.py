PATH = 'books/frankenstein.txt'


def get_words_count(text: str):
    words = text.split()
    return len(words)


def get_letter_frequency(text: str):
    words = text.split()
    freq_map = {}
    for word in words:
        for letter in word:
            # skip when letter is not an alphabet
            if not letter.isalpha():
                continue

            letter = letter.lower()
            if letter in freq_map:
                freq_map[letter] += 1
            else:
                freq_map[letter] = 1
    return freq_map


def print_report(book_path: str, book_content: str):
    print(f'--- Begin report of {book_path} ---\n')
    print(f'{get_words_count(book_content)} words found in the document\n')

    freq = get_letter_frequency(book_content)
    sorted_letters = sorted(freq.keys())

    for letter in sorted_letters:
        print(f'The \'{letter}\' character was found {freq[letter]} times')

    print('\n--- End report ---')


if __name__ == '__main__':
    with open(PATH) as f:
        book_content = f.read()
        print_report(PATH, book_content)
