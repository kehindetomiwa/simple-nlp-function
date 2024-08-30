import wikipedia

def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    print(result, type(result))
    return result