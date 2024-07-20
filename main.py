
def main():
    bookpath = "books/frankenstein.txt";
    file_contents = getbook(bookpath);
    wordcount = wordreturner(file_contents);
    dict_count = counter(file_contents);
    order_dicto = convert_dicto(dict_count);
    order_dicto.sort(reverse=True, key=sort_dict);
    print("REPORT START!!! ABOUT???? = FRANKENSTEIN \n");
    print(f"Amount of words???? = {wordcount}\n");
    print_list(order_dicto);
    print("THE END.");

def wordreturner(string):
    words = string.split();
    return len(words);

def getbook(path):
    with open(path) as f:
        return f.read();

def counter(string):
    dicto = {};
    no_caps = string.lower();
    for char in no_caps:
        if char in dicto:
            dicto[char] += 1;
        else:
            dicto[char] = 1;
    return dicto;

def convert_dicto(dicto):
    listo = [];
    for char in dicto:
        if char.isalpha() == True:
            listo.append({char:dicto[char]});
    return listo;

def sort_dict(dicto):
    for char in dicto:
        return dicto[char];

def print_list(list):
    for dict in list:
        for char in dict:
            print(f"{char} was found {dict[char]} times");
    print("\n");



if __name__ == "__main__":
    main();