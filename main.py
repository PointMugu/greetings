from greets import greetings
from translate import Translator

t = Translator(to_lang ='hmn')
for g in greetings:
    print(t.translate(g).title() + "!")