# spaCy:

- NLP 工具包
- https://github.com/explosion/spaCy

## Quickstart:

- 安装依赖:

```ruby

# 安装:
task try:spacy:add

# 下载model
task try:spacy:download

```

## Reference:

### docs

- https://spacy.io/usage

### install

- https://spacy.io/usage

```ruby

python -m venv .env
source .env/bin/activate

pip install -U pip setuptools wheel
pip install -U 'spacy[apple]'

python -m spacy download en_core_web_sm
python -m spacy download ja_core_news_sm


```

### guide

- https://course.spacy.io/zh/

### 可视化

- https://spacy.io/usage/visualizers#span