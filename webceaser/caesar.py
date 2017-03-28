
# Step1: Assign value to each character using dictionary

import string

def alphabet_position(letter):

    alphabet= string.ascii_lowercase

    alphabet_position_dic={}
    starting_value=0
    for i in alphabet:
        alphabet_position_dic[i]=starting_value
        starting_value= starting_value+1
    return(alphabet_position_dic[letter.lower()])# returns the value for the alphabet


def character_rotate(char,rot):

        if char.isalpha():
            if rot >= 26:
                rot= rot%26

            alphabet_strt_pos= alphabet_position(char)
            alphabet_new_pos=alphabet_strt_pos+int(rot)

            if alphabet_new_pos > 25:
                alphabet_new_pos= alphabet_new_pos-26

            if char.islower():

                alphabet= string.ascii_lowercase
                alphabet_position_dic={}
                starting_value=0

                for i in alphabet:
                    alphabet_position_dic[i]=starting_value
                    starting_value= starting_value+1


                for k,v in alphabet_position_dic.items():
                    if alphabet_position_dic[k]==alphabet_new_pos:
                        return k
            if char.isupper():

                alphabet= string.ascii_uppercase
                alphabet_position_dic={}
                starting_value=0

                for i in alphabet:
                    alphabet_position_dic[i]=starting_value
                    starting_value= starting_value+1


                for k,v in alphabet_position_dic.items():
                    if alphabet_position_dic[k]==alphabet_new_pos:
                        return k
        return  char


def encrypt(text,rot):
    new_code=""
    for char in text:

        if char.isalpha():
            if rot >= 26:
                rot= rot%26

            alphabet_strt_pos= alphabet_position(char)
            alphabet_new_pos=alphabet_strt_pos+int(rot)

            if alphabet_new_pos > 25:
                alphabet_new_pos= alphabet_new_pos-26

            if char.islower():

                alphabet= string.ascii_lowercase
                alphabet_position_dic={}
                starting_value=0

                for i in alphabet:
                    alphabet_position_dic[i]=starting_value
                    starting_value= starting_value+1


                for k,v in alphabet_position_dic.items():
                    if alphabet_position_dic[k]==alphabet_new_pos:
                        new_code= new_code+k
            elif char.isupper():

                alphabet= string.ascii_uppercase
                alphabet_position_dic={}
                starting_value=0

                for i in alphabet:
                    alphabet_position_dic[i]=starting_value
                    starting_value= starting_value+1


                for k,v in alphabet_position_dic.items():
                    if alphabet_position_dic[k]==alphabet_new_pos:
                        new_code= new_code+k
        else :
            new_code= new_code+char
    return new_code
