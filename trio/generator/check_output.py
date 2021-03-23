#check corpus, create concordances
from pyigt import Corpus
import csv
dataset = Corpus.from_path('metadata.json')
dataset.check_glosses()
dataset.write_concordance('lexicon', filename='lexical-concordance.csv')
dataset.write_concordance('grammar', filename='grammatical-concordance.csv')

morph_list = []
for row in csv.DictReader(open("../morphemes.csv")):
    for f in row["Form"].split("; "):
        morph_list.append((f.replace("-", ""), row["Meaning"]))

filenames = ['lexical-concordance.csv', 'grammatical-concordance.csv']
new = []
for tsv_file in filenames:
    for row in csv.DictReader(open(tsv_file), delimiter="\t"):
        if row["GLOSS_IN_SOURCE"].upper() != row["GLOSS_IN_SOURCE"]:
            row["GLOSS_IN_SOURCE"] = row["GLOSS_IN_SOURCE"].replace(".", " ")
        if (row["FORM"], row["GLOSS_IN_SOURCE"]) not in morph_list:
            err = f"{row['FORM']}\t{row['GLOSS_IN_SOURCE']}"
            print(f"Found a missing entry: {err}")
            if err not in new:
                new.append(err)
import pyperclip
pyperclip.copy("\n".join(sorted(new, key=len)))
        #     l_out.append({
        #         "Form": row["FORM"],
        #         "Meaning": row["GLOSS_IN_SOURCE"],
        #     })
        # else:
        #     g_out.append({
        #         "Form": row["FORM"],
        #         "Meaning": row["GLOSS_IN_SOURCE"],
        #     })
        
# with open("generated_morpheme_list.csv", "w") as csvfile:
#     fieldnames = g_out[0].keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for entry in g_out:
#         writer.writerow(entry)
#     for entry in l_out:
#         writer.writerow(entry)