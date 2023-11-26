import sieve

def detect(text):
    langid = sieve.function.get("sieve/langid")
    output = langid.run(text)
    return output