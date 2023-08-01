import spacy


def nlp_print():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)


def nlp_print2():
    print(f"\n")
    nlp = spacy.load("en_core_web_sm")
    print("Pipeline:", nlp.pipe_names)

    doc = nlp("I was reading the paper.")
    token = doc[0]  # 'I'
    print(token.morph)  # 'Case=Nom|Number=Sing|Person=1|PronType=Prs'
    print(token.morph.get("PronType"))  # ['Prs']


if __name__ == "__main__":
    nlp_print()
    nlp_print2()
