import jieba


def clean(text):
    return " ".join(jieba.cut(text))
