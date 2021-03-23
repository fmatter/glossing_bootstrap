import csv
import pyigt
import random

en = {}
for row in csv.DictReader(open("en.csv")):
    en[row["Gloss"]] = {
        "PST": row["PST"]
    }

prefixes = {}
for row in csv.DictReader(open("person_prefixes.csv")):
    prefixes[row["Function"]] = row

nouns = {"NH": [], "NA": [], "NI": []}
for row in csv.DictReader(open("roots.csv")):
    if row["Class"] in ["NH", "NA", "NI"]:
        nouns[row["Class"]].append({
            "Form": row["Form"].split("; ")[0],
            "Meaning": row["Meaning"]
        })
    
out = []
for row in csv.DictReader(open("roots.csv")):
    obj = row["Form"].split("; ")[0]
    if "; " in row["Form"]:
        redobj = row["Form"].split("; ")[1]
    gloss = row["Meaning"].replace(" ", ".")
    if row["Class"] in ["TR", "sa", "sp"]:
        past = en[row["Meaning"]]["PST"]
        fut = "will " + row["Meaning"]
        if row["env"] in ["eC", "e", "aCə", "ei"]:
            obj12 = "ə" + obj[1:]
        elif row["env"] in ["aCo"]:
            obj12 = "o" + obj[1:]
        elif row["env"] == "ee":
            obj12 = "əə" + obj[2:]
        else:
            obj12 = obj
        if row["env"] in ["ee"]:
            obj2 = obj[1:]
        elif row["env"] in ["ei"]:
            obj2 = "ə" + obj[1:]
        else:
            obj2 = obj
    if row["Class"] == "TR":
        a1 = prefixes["1>3"][row["env"]]
        a2 = prefixes["2>3"][row["env"]]
        a3 = prefixes["3"][row["env"]]
        a12 = prefixes["1+2>3"][row["env"]]
        p1 = prefixes["1P"][row["env"]]
        p2 = prefixes["2P"][row["env"]]
        p12 = prefixes["1+2P"][row["env"]]
        if p2 == "":
            gloss2 = ""
        else:
            gloss2 = "2P-"
        prefs = [
            {"form": a1, "subj": "I", "obj": "it", "gloss": "1A-"},
            {"form": a2, "subj": "You", "obj": "it", "gloss": "2A-"},
            {"form": a12, "subj": "We", "obj": "it", "gloss": "1+2A-"},
            {"form": a3, "subj": "S/he", "obj": "it", "gloss": "3-"},
            {"form": p1, "subj": "S/he", "obj": "me", "gloss": "1P-"},
            {"form": p2, "subj": "S/he", "obj": "you", "gloss": gloss2},
            {"form": p12, "subj": "S/he", "obj": "us", "gloss": "1+2P-"}
        ]
        #Add past sentences for all prefixes
        for pref in prefs:
            out.append({
                "Sentence": f"{pref['form']}{obj}".replace("-", ""),
                "Analyzed": f"{pref['form']}{obj}",
                "Gloss": f"{pref['gloss']}{gloss}",
                "Translation": f"{pref['subj']} {past} {pref['obj']}."
            })
        if row["good"] == "y":
            #Add random objects for A-prefixes
            for i in range(0,3):
                pref = random.choice(prefs[0:2])
                obj_noun = random.choice(nouns["NH"] + nouns["NA"] + nouns["NI"])
                out.append({
                    "Sentence": f"{pref['form']}{obj} {obj_noun['Form']}".replace("-", ""),
                    "Analyzed": f"{pref['form']}{obj} {obj_noun['Form']}",
                    "Gloss": f"{pref['gloss']}{gloss} {obj_noun['Meaning']}",
                    "Translation": f"{pref['subj']} {past} the {obj_noun['Meaning']}."
                })
            #Add random subjects for P-prefixes
            for i in range(0,3):
                pref = random.choice(prefs[3:])
                subj_noun = random.choice(nouns["NH"])
                out.append({
                    "Sentence": f"{subj_noun['Form']} {pref['form']}{obj}".replace("-", ""),
                    "Analyzed": f"{subj_noun['Form']} {pref['form']}{obj}",
                    "Gloss": f"{subj_noun['Meaning']} {pref['gloss']}{gloss}",
                    "Translation": f"The {subj_noun['Meaning']} {past} {pref['obj']}."
                })
            #add random NP>NP scenarios
            for i in range(0,2):
                pref = prefs[3]
                subj_noun = random.choice(nouns["NH"])
                obj_noun = random.choice(nouns["NA"] + nouns["NI"])
                #…one with n-
                out.append({
                    "Sentence": f"{subj_noun['Form']} {pref['form']}{obj} {obj_noun['Form']}".replace("-", ""),
                    "Analyzed": f"{subj_noun['Form']} {pref['form']}{obj} {obj_noun['Form']}",
                    "Gloss": f"{subj_noun['Meaning']} {pref['gloss']}{gloss} {obj_noun['Meaning']}",
                    "Translation": f"The {subj_noun['Meaning']} {past} the {obj_noun['Meaning']}."
                })
                #…one without
                out.append({
                    "Sentence": f"{subj_noun['Form']} {obj_noun['Form']} {obj}".replace("-", ""),
                    "Analyzed": f"{subj_noun['Form']} {obj_noun['Form']} {obj}",
                    "Gloss": f"{subj_noun['Meaning']} {obj_noun['Meaning']} {gloss}",
                    "Translation": f"The {subj_noun['Meaning']} {past} the {obj_noun['Meaning']}."
                })
    elif row["Class"] == "sa":
        a1 = prefixes["1SA"][row["env"]]
        a2 = prefixes["2SA"][row["env"]]
        a3 = prefixes["3"][row["env"]]
        a12 = prefixes["1+2SA"][row["env"]]
        out.append({"Sentence": f"{a1}{obj}".replace("-", ""), "Analyzed": f"{a1}{obj}", "Gloss": f"1A-{gloss}", "Translation": f"I {past}."})
        out.append({"Sentence": f"{a2}{obj}".replace("-", ""), "Analyzed": f"{a2}{obj}", "Gloss": f"2A-{gloss}", "Translation": f"You {past}."})
        out.append({"Sentence": f"{a3}{obj}".replace("-", ""), "Analyzed": f"{a3}{obj}", "Gloss": f"3-{gloss}", "Translation": f"S/he {past}."})
        out.append({"Sentence": f"{a12}{obj}".replace("-", ""), "Analyzed": f"{a12}{obj}", "Gloss": f"1+2A-{gloss}", "Translation": f"We {past}."})
    elif row["Class"] == "sp":
        p1 = prefixes["1P"][row["env"]]
        p2 = prefixes["2P"][row["env"]]
        p12 = prefixes["1+2P"][row["env"]]
        p3 = prefixes["3"][row["env"]]
        if p2 == "":
            gloss2 = ""
        else:
            gloss2 = "2P-"
        out.append({"Sentence": f"{p1}{obj}".replace("-", ""), "Analyzed": f"{p1}{obj}", "Gloss": f"1P-{gloss}", "Translation": f"I {past}."})
        out.append({"Sentence": f"{p2}{obj}".replace("-", ""), "Analyzed": f"{p2}{obj}", "Gloss": f"{gloss2}{gloss}", "Translation": f"You {past}."})
        out.append({"Sentence": f"{p3}{obj}".replace("-", ""), "Analyzed": f"{p3}{obj}", "Gloss": f"3-{gloss}", "Translation": f"S/he {past}."})
        out.append({"Sentence": f"{p12}{obj}".replace("-", ""), "Analyzed": f"{p12}{obj}", "Gloss": f"1+2P-{gloss}", "Translation": f"We {past}."})

with open("generated_paradigms.csv", "w") as csvfile:
    fieldnames = out[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in out:
        writer.writerow(entry)

out = []
full_out = []
for row in csv.DictReader(open("generated_paradigms.csv")):
    out.append({key: row[key] for key in ["Sentence", "Translation"]})
    full_out.append(row)
for row in csv.DictReader(open("manual_examples.csv")):
    out.append({key: row[key] for key in ["Sentence", "Translation"]})
    full_out.append(row)

#write all sentences for the dataset
with open("../sentences.csv", "w") as csvfile:
    fieldnames = out[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in out:
        writer.writerow(entry)

#write glossed sentences
with open("all_sentences.csv", "w") as csvfile:
    fieldnames = ["ID"] + list(full_out[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i, entry in enumerate(full_out):
        entry["ID"] = i+1
        writer.writerow(entry)
        
#write all morphemes for the dataset
out = []
for row in csv.DictReader(open("affixes.csv")):
    out.append(row)
for row in csv.DictReader(open("roots.csv")):
    obj = row["Form"].split("; ")[0]
    all_forms = [obj]
    if "; " in row["Form"]:
        redobj = row["Form"].split("; ")[1]
        all_forms.append(redobj)
    if row["env"] in ["eC", "e", "aCə", "ei"]:
        all_forms.append("ə" + obj[1:])
    elif row["env"] in ["aCo"]:
        all_forms.append("o" + obj[1:])
    elif row["env"] == "ee":
        all_forms.append(obj[2:])
        all_forms.append(obj[1:])
    row["Form"] = "; ".join(all_forms)
    out.append({key: row[key] for key in ["Form", "Meaning"]})
with open("../morphemes.csv", "w") as csvfile:
    fieldnames = out[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in out:
        writer.writerow(entry)
        
import check_output