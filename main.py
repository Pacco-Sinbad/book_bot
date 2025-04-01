from stats import word_count
import sys


def main():

    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]

    
    
    def char_count(x):
        dict = {}
        characters = list(x.lower())
        set_of_characters = set(characters)
        for character in set_of_characters:
            dict[f"{character}"] =  characters.count(character)
        return dict

    def report_alpha(x):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        listed_alphabet = list(alphabet)
        dict = char_count(x)
        alpha_dict = {}
        for letter in listed_alphabet:
            alpha_dict[f"{letter}"] = dict[f"{letter}"]
        list_of_alpha = [{"character": k, "num": v} for k, v in alpha_dict.items()]
        sorted_list_of_alpha = sorted(list_of_alpha, reverse=True, key=lambda d: d["num"])
        report = []
        for y in sorted_list_of_alpha:
            report.append(f'''{y["character"]}: {y["num"]}\n''')
        annoying_list_of_useless_garbage = "".join(report)
        return annoying_list_of_useless_garbage
        
        

    with open(path_to_book) as f:
        file_contents = f.read()
        words = word_count(file_contents)
        character_counter = char_count(file_contents)
        alphabetical = report_alpha(file_contents)
      

        print(f"""--- Begin report of {f.name} ---
        {words} words found in the document

{alphabetical}
        --- End report ---
        """) 
        

if __name__ == "__main__":
    main()