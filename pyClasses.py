import clips


def FindFactByIndex(idx):
    f = clips.InitialFact()
    while f is not None and f.Index != idx:
        f = f.Next()
    return f

def ListFactByName():
   f = clips.InitialFact()
   while f is not None:
    f.PPrint()
    f = f.Next()