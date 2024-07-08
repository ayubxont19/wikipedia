import wikipedia
wikipedia.set_lang("uz")

def wiki_bot(text):
    try:
        result = wikipedia.summary(text)
        return result
    except:
        return "Kechirasiz bunday ma'lumot topilmadi"