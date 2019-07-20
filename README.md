# anki-vocabulary-builder

A python script works with Anki that helps you build your vocabulary

## overview

Anki is great for vocabulary building, but add personal learning cards to it is tedious, you don't want to click and type for adding a word each time, this script automate the procedure, which allows you to add card to Anki use dictionary from [vocabulary.com](https://www.vocabulary.com/) in your console.

## setup

* Anki: Version 2.1.14 (7b93e985)
* Addon: [AnkiConnect](https://ankiweb.net/shared/info/2055492159), addon code: `2055492159`
* Python env: python=3.6, with `requests`, `termcolor`, `textwrap` and `bs4`
* Create a deck named `GRE`, or you can use any name but you have to modify the script a little bit
* Create a note type named `vocabulary.com` from **Basic (and reversed card)**, use the following fields
![image](https://user-images.githubusercontent.com/29735669/61583442-b4924780-aaec-11e9-968e-95f1d7e5ffec.png)
and the layout:
![card1](https://user-images.githubusercontent.com/29735669/61583449-d4c20680-aaec-11e9-9e91-25e38f6c8e38.png)
![card2](https://user-images.githubusercontent.com/29735669/61583531-1f904e00-aaee-11e9-99ef-f714ebd397ac.png)

Then you are done

## usage

After the setup, lauch anki, and `./run.sh`, you'll be able to look up words, and the words you looked up will be automatically added to anki for reviewing memorizing.

Demo:

![image](https://user-images.githubusercontent.com/29735669/61583483-4c903100-aaed-11e9-9aef-7353042bb0e9.png)

![image](https://user-images.githubusercontent.com/29735669/61583495-66ca0f00-aaed-11e9-934b-40fd12bb352b.png)
![image](https://user-images.githubusercontent.com/29735669/61583537-3e8ee000-aaee-11e9-82a6-27f3a7fcf09c.png)

## Reference

* [Anki Tutorial: Type Your Answer](https://www.youtube.com/watch?v=LNDwt4kHYo4)
* [Anki User Manual](https://apps.ankiweb.net/docs/manual.html)
* [AnkiConnect Documentation](https://foosoft.net/projects/anki-connect/)

