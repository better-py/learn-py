import spacy
from spacy import displacy


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


def nlp_print3():
    text = """When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the
    company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand
    and turn away because I wasn’t worth talking to,” said Thrun, now the co-founder and CEO of online higher
    education startup Udacity, in an interview with Recode earlier this week.

    A little less than a decade later, dozens of self-driving startups have cropped up while automakers around the
    world clamor, wallet in hand, to secure their place in the fast-moving world of fully automated transportation.

    """

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # 彩色显示句子成分
    displacy.serve(doc, style="ent", host="127.0.0.1", auto_select_port=True)


def nlp_print4():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a sentence.")

    # 依赖关系图
    displacy.serve(doc, style="dep", host="127.0.0.1", auto_select_port=True)


def nlp_print5():
    from spacy.tokens import Span

    text = "Welcome to the Bank of China."

    nlp = spacy.blank("en")
    doc = nlp(text)

    doc.spans["sc"] = [
        Span(doc, 3, 6, "ORG"),
        Span(doc, 5, 6, "GPE"),
    ]

    displacy.serve(doc, style="span", host="127.0.0.1", auto_select_port=True)


if __name__ == "__main__":
    nlp_print()
    nlp_print2()
    nlp_print3()
    # nlp_print4()
    # nlp_print5()
