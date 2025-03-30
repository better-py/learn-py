# Django 5.x 实测

- 作为 Django 老用户, 很久没使用.
- 验证一下最新版本的特性.

## Features

- [django-rest-framework](https://www.django-rest-framework.org/tutorial/quickstart/)
  - token auth: [authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- [OpenAPI: Spectacular](https://github.com/tfranzel/drf-spectacular/)
- [sentry](https://sentry.io/)
- [django-simpleui]()

## Quick start

### init db

```ruby
cd git-repo-root/
task web:drf:init

# or
task init
```

### create admin user

```ruby
cd git-repo-root/
task web:drf:init:user

# or
task init:user  # input: admin/admin
```

### run http server

```ruby
cd git-repo-root/
task web:drf:run

# or
cd this-dir/
task run
```

## Manual

### new project

```ruby

django-admin startproject mysite
```

### new app

```ruby

django-admin startapp myapp
```
