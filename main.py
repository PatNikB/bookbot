def main():
    with open( './books/frankenstein.txt' ) as f:
        file_contents = f.read()
        print ( count_words(file_contents))
        print ( count_characters( file_contents ) )

def count_words( str_text ):
    words = str_text.split()
    return len( words )

def count_characters( str_text ):
    number_of_characters = {}
    lowered_string = str_text.lower()
    for char in range( 0,len( lowered_string ) ):
        if lowered_string[ char ] in number_of_characters:
            number_of_characters[ lowered_string[char] ] += 1
        else:
            number_of_characters[ lowered_string[char] ] = 1
    return number_of_characters
main()