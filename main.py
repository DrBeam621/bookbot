def sort_on(dict):
    return dict["num"]

def main():

    character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    # initialize count_dict
    count_dict = {}

    for char in character_list :
        count_dict[char] = 0

    # print(count_dict)

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        for book_word in words :
            lowered_word = book_word.lower()
            for book_char in lowered_word :
                if book_char in character_list :
                    count_dict[book_char] += 1

    # print(count_dict)
    # print(len(words))

    # convert a count dict into a list of dictionary with value names
    alphabet_count_list = []

    for character in character_list :

        dict_item = {}
        dict_item["character"] = character
        dict_item["num"] = count_dict[character]

        alphabet_count_list.append(dict_item)

    # print(alphabet_count_list)

    alphabet_count_list.sort(reverse=True, key=sort_on)
    # print(alphabet_count_list)

    for dict_item in alphabet_count_list :
        print(f"The '{dict_item['character']}' character was found {dict_item['num']} times")

main()