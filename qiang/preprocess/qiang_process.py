import pyigt
from pyigt import Corpus
corpus = Corpus.from_path("./lapollaqiang/cldf/cldf-metadata.json")
translations = open("./lapollaqiang/translations.txt").read().split("\n")
def expr(ex):
    obj = ex.phrase_text
    gloss = ex.gloss_text
    out_obj = []
    out_gloss = []
    exlabel = f"({ex.id}) "
    if int(ex.id)-1 < len(translations):
        trans = translations[int(ex.id)-1]
    else:
        trans = "Missing"
    if len(trans) > 90: trans = "Missing"
    for o, g in zip(obj.split(" "), gloss.split(" ")):
        diff = len(o)-len(g)
        if diff < 0:
            o += " "*-diff
        else:
            g += " "*diff
        out_obj.append(o)
        out_gloss.append(g)
    print(exlabel + " ".join(out_obj))
    print(" "*len(exlabel) + " ".join(out_gloss))
    print(" "*len(exlabel) + f"'{trans}'")
    print("")

# for id, ex in corpus._igts.items():
#     if ex.properties["Text_ID"] != "3": continue
#     expr(ex)
# expr(corpus._igts["63"])

corpus.write_concordance('lexicon', filename='lexicon-concordance.tsv')
corpus.write_concordance('grammar', filename='gramm-concordance.tsv')
