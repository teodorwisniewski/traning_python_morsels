import re
from textwrap import dedent

def normalize_sentences(sentence:str):

    result = re.sub(r"([.?!]\s)([^\s])",r"\1 \2",sentence)
 
    return result


sentences = dedent("""
            This is a paragraph. With two sentences in it.

            And this is one. With three. Three short sentences.
        """).strip()
print(sentences)
print(normalize_sentences(" ".join(sentences)))
print(normalize_sentences("This isn't a sentence."))
print(normalize_sentences("Hello? Yes, this is dog!"))
print(normalize_sentences("Irthg am. Ihtr was. Ihr will be."))

