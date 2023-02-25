import spacy
#that's the library
nlp = spacy.load("en_core_web_sm")
#that's a specific language model for that library

#text ="Imagine a time when you could pay your taxes with honey or even salt! Yes, you heard it right! In ancient times, some civilizations used these everyday commodities as a form of currency. However, the use of money as a standardized medium of exchange was not developed until around 600 BC in Lydia, a region in modern-day Turkey. King Alyattes of Lydia was the first to mint coins made of a naturally occurring alloy of gold and silver called electrum. The coins had different weights and denominations and were stamped with symbols to guarantee their authenticity. This invention of standardized currency revolutionized trade and commerce and facilitated the growth of economies and civilizations worldwide. The use of money has come a long way since then, from paper notes to digital transactions, but it all started with the humble coin of Lydia. So, next time you pay for something with cash or card, remember the fascinating history behind it!"
#that's my sample text

def getkeywords(text):
    doc = nlp(text)
    return set(doc.ents)
    # even though return set(doc.ents) returns type <class 'tuple'> (Tuples are used to store multiple items in a single variable.), set() converts that tuple
    # to a set so that it doesn't have duplicates

