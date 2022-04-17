#!/usr/bin/python3

import requests
import sys
import os


def main():
    words = sys.argv[1:]
    if not words:
        print("No words to look up were passed!")
    else:
        get_words(words)


def get_words(words):
    key = "f434f965-79df-430b-a61e-42d61ea80b6b"
    print("looking up...")
    for w in words:
        r = requests.get(
            f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{w}?key={key}"
        )

        if r.status_code == 200:
            for output in r.json():
                word = output["hwi"]["hw"]
                w_class = output["fl"]
                shortdef = output["shortdef"][0]
                syns_list = output["meta"]["syns"]
                synonyms = [item for sublist in syns_list for item in sublist]
                ants_list = output["meta"]["ants"]
                antonyms = [item for sublist in ants_list for item in sublist]

                print("_" * os.get_terminal_size().columns)
                print(f"\n{word} ({w_class}): {shortdef}")
                print("\nsynonyms: ", end="")
                print(*synonyms, sep=", ")
                if antonyms:
                    print("\nantonyms: ", end="")
                    print(*antonyms, sep=", ")
        else:
            print(f"Could not retrieve data for {word}. Status code: {r.status_code}")


if __name__ == "__main__":
    main()
