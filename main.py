def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_content = f.read()
        num_words = countWords(file_content)
        char_dict = countCharacters(file_content)
        char_list = toList(char_dict)        
        print(f"--- Begin report of {file} ---")
        print(f"{num_words} words found in the document")
        for c in char_list:
            if c["name"].isalpha():
                print(f"The {c["name"]} character was found {c["num"]} times")
        print("--- End report ---")
def countWords(string):
    return len(string.split())

def countCharacters(string):
    characters = {}
    for c in string.lower():
        if not c in characters:
            characters[c] = 0
        characters[c] += 1
    return characters

def on_sort(dict):
    return dict["num"]

def toList(dict):
    list = []
    for item in dict:
        list.append({"name": item, "num": dict[item]})
    list.sort(reverse=True, key=on_sort)
    return list


main()