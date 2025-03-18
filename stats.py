def sort_characters(char_count):
    sorted_list=[
        {"char":char, "count":count}
        for char, count in char_count.items() if char.isalpha()
    ]
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list

def count_character(text):
    char_count={}
    text=text.lower()

    for char in text:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

def get_num_words(text):
    words=text.split()
    return len(words)