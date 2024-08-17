def main():
    book_path = "./books/frankenstein.txt"
    with open( book_path ) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        # print ( count_characters( file_contents ) )
        dict_chars = count_characters( file_contents )
        report = generate_char_report( dict_chars )
        print_report( report, word_count, book_path )

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


def generate_char_report( dict_char ):
    report = []
    # print ( dict_char )
    for char,num in dict_char.items():
        if ( char.isalpha() ):
            report.append( { "char": char, "num" : num } )
    report.sort(reverse=True, key=sort_by_num)
    return report

def print_report( list_report, word_count, book_path ):
    print ( f"--- Report of {book_path} ---" )
    print ( f"{word_count} words found in the document" )
    print ()
    for item in list_report:
        print ( f"The '{ item["char"] }' character was found {item["num"]} times" )
    print ("--- End of report ---")

def sort_by_num( dict ):
    return dict["num"]

main()