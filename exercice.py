#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0


def remove_third_char(string: str) -> str:
    new_string = ""
    for i in range(len(string)):
        if(i != 2):
            new_string += string[i]
    return new_string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    for c in string:
        if(c == old_char):
            new_string += new_char
        else:
            new_string += c
    return new_string


def get_number_of_char(string: str, char: str) -> int:
    return string.count(char)


def get_number_of_words(sentence: str, word: str) -> int:
    word_found = 0
    for i in range(len(sentence)):
        if(word[0] == sentence[i]):
            for j in range(1, len(word)):
                if(sentence[j] != word[j]):
                    j = len(sentence) - i
            word_found += 1

    return word_found


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
