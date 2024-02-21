import math
import os

def title_text():
    os.system('cls')
    title = "VOCAB BUILDER"
    version = "0.1.0"
    boxWidth =70
    print("+" + ("-"*(boxWidth-2)) + "+")
    center(title,boxWidth,"|")
    center(version,boxWidth,"|")
    print("+" + ("-"*(boxWidth-2)) + "+")
    print("\n\n")


def center(text, width, border = " "):
    print(border + " "*(math.floor((width-2-len(text))/2)) + text + " "*(math.ceil((width-2-len(text))/2))  + border)


title_text()