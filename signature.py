#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import random


# Credit to tetrapus
# (https://github.com/tetrapus/Karkat/blob/master/text.py#L14-L28)
def lineify(data, max_size=400):
    """
    Split text up into IRC-safe lines.
    """
    lines = []
    for i in data.split("\n"):
        line = [[]]
        words = i.split(" ")
        for word in words:
            if len(" ".join(line[-1])) < max_size:
                line[-1].append(word)
            else:
                line.append([word])
        lines.extend(" ".join(x) for x in line)
    return lines

home = os.path.expanduser("~")
lyrics_folder = os.path.sep + ".lyrics"
songs = os.listdir(home + lyrics_folder)
artist = "The White Stripes"

song_filename = random.choice(filter(lambda fn: artist in fn, songs))
song = song_filename.split("- ")[1].split(".txt")[0]

path = home + lyrics_folder + os.path.sep + song_filename

with open(path, 'r') as f:
    song_lyrics = f.read()

par_separator = "\n\n"

paragraphs = song_lyrics.split(par_separator)

song_quote = random.choice(paragraphs)

signature = """
----------------------------------------
Declan Kelly (Knight Hawk3)
Head of IT at The Disorganisation
declan@KnightHawk3.com
KnightHawk3.com

Here is a random song quote:

""" + song_quote

signature = lineify(signature, max_size=50)

print '\n'.join(signature)
