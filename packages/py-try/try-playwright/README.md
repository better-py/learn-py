# playwright

- playwright 是一个自动化测试工具，可以用来模拟浏览器操作，比如点击、输入、滚动、截图等等。
- playwright 支持多种语言，包括 python、java、js 等等。
- https://playwright.dev/python/docs/library

## development

- install:

```ruby

pip install --upgrade pip
pip install playwright
playwright install


# or:
poetry add "typer[all]" playwright
poetry run playwright install

```

- run: [Taskfile.yml](Taskfile.yml)

```ruby

cd repo-root/

# run task
task try:pw:run01

```