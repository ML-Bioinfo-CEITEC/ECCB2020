from fastai2.text.all import *

class LetterTokenizer():
    def __init__(self, **kwargs):
        pass
    def __call__(self, items):
        if isinstance(items, str):
          return self.__tokenize_str(items)
        else:
          return (self.__tokenize_str(t) for t in items)
    def __tokenize_str(self, t):
        return L(list(t.replace("\n","")))

    @property
    def special_toks(self,): return ['xxunk']

tkn = LetterTokenizer()

# because empty list of rules throws error
def do_nothing(x):
    return x

tkn2 = Tokenizer(tkn, rules=[do_nothing])