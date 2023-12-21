# Twitter Crawler

- 使用 Python 发 Twitter.
- 本项目, 并不使用 Tweepy 库, 而是基于 浏览器登录后, cookie 方式发 Twitter.

## 设置环境变量:

- 如下 cookie 信息, 从浏览器中获得.
- 简单抓包 Twitter web 版页面, 就能获取.
- Twitter CSRF Token 并不是动态生成的, 随便拿一个就行.

```ruby

TWITTER_AUTHORIZATION="web auth"
TWITTER_CSRF_TOKEN="web page csrf token"
TWITTER_COOKIES="browser cookie"


```