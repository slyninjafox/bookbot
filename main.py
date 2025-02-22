def main():
    ltr_freq = {}
    num_words = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        num_words += len(file_contents.split())
        for c in file_contents:
            ltr_freq[c] = ltr_freq.get(c,0)+1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for ltr in ltr_freq:
        if ltr.isalpha():
            print(f"The '{ltr}' character was found {ltr_freq[ltr]} times")
    print("--- End report ---")
 
main()