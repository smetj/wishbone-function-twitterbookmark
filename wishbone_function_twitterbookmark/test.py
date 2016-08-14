#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#
#  Copyright 2016 Jelle Smet <development@smetj.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import validators
import nltk

data = "Pull doesn't scale - or does it? I wrote an article about this particularly persistent monitoring misconception: prometheus.io/blog/2016/07/2 #monitoringlove"
nltk.download(info_or_id="stopwords", quiet=True)
nltk.download(info_or_id="punkt", quiet=True)
nltk.download(info_or_id="averaged_perceptron_tagger", quiet=True)
def cleanup( tokens):

    def validate(word):

        conditions = [
            word not in nltk.corpus.stopwords.words('english'),
            not validators.url(word),
            word.isalnum(),
            word.lower() not in ["i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "it", "us"]
        ]

        return all(conditions)

    result = []

    for word in tokens:
        if validate(word):
            print word
            result.append(word.lower())
    return result
# nltk.download()
def main():
    # print nltk.word_tokenize(data)
    tokenized_text = nltk.TweetTokenizer().tokenize(data)
    # cleaned = [word.lower() for word in tokenized_text if word not in nltk.corpus.stopwords.words('english') and not validators.url(word) and word.isalnum() and word.lower() not in blacklist]
    print cleanup(tokenized_text)
if __name__ == "__main__":
    main()
