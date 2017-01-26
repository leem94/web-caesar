def alphabet_position(letters):
    # type: (object) -> object
    letters = letters.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    for letter in letters: this for loop is to return num of multiple characters
    alpha_num = alpha.find(letters)
    return alpha_num


def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    char_position = alphabet_position(char)
    final_num = (char_position + rot) % 26  #if x % y and x is less than y, it will just return the value of x
    new_char = alpha[final_num]

    if char.isupper() == True:   #check if char was uppercase
        new_char = new_char.upper()  #if so, return new_char as uppercase too

    if char.isalpha() != True:   #return non-alphabet char
        return char

    return new_char

def encrypt(text,rot):
    encryp_word = ''
    for char in text:
        encryp_word += rotate_character(char,rot)
    return encryp_word