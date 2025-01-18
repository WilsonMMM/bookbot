def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        word_cnt = get_word_count(file_contents)
        char_cnt = get_char_count(file_contents)

        print(f"--- Begin report of {book} ---")    
        print(f"{word_cnt} words found in the document")
        print("")

        for c in char_cnt:
            print(f"The '{c}' character was found {char_cnt[c]} times")
        print("--- End report ---")

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_map = {};
    sorted_map = {}
    for i in range(0, len(text)):
        chr = text[i].lower();
        if not (chr.isalpha()):
            continue;
        if chr not in char_map:
            char_map[chr] = 0
        char_map[chr]+= 1
    
    for k in sorted(char_map, key=char_map.get, reverse=True    ):
        sorted_map[k] = char_map[k];
    return sorted_map

main();