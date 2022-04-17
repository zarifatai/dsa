#!/usr/bin/python3

import requests
import sys


def main():
    args = sys.argv
    if len(args) > 2:
        print("Graag alleen de stad meegeven")
    elif len(args) == 1:
        get_weather("Amersfoort")
    else:
        get_weather(args[1])


def get_weather(city):
    key = "f168df7b41"
    print(f"Weerdata ophalen...\n")

    r = requests.get(
        f"https://weerlive.nl/api/json-data-10min.php?key={key}&locatie={city.capitalize()}"
    )

    if r.status_code == 200:
        output = r.json()["liveweer"][0]
        print("Plaats:", output["plaats"])
        print("Huidige temperatuur (C):", output["temp"])
        print("Min temperatuur (C):", output["d0tmin"])
        print("Max temperatuur (C):", output["d0tmax"])
        print("Dagverwachting:", output["verw"].lower())
        print("Zonsopgang:", output["sup"])
        print("Zonsondergang:", output["sunder"], "\n")

        print("Morgen:")
        print(
            "Min temperatuur (C):",
            output["d1tmin"],
        )
        print("Max temperatuur (C):", output["d1tmax"], "\n")

        print("Overmorgen:")
        print("Min temperatuur (C):", output["d2tmin"])
        print("Max temperatuur (C):", output["d2tmax"])
    else:
        print(
            f"Could not retrieve data for {city.capitalize()}. Status code {r.status_code}"
        )


if __name__ == "__main__":
    main()
