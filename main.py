import sys
from stats import get_num_words, count_character, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path= sys.argv[1] # obtener argumentos de la linea de comandos
    book_text=get_book_text(file_path)
    
    num_words=get_num_words(book_text)
    char_count=count_character(book_text)
    sorted_chars=sort_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
  

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")



main()