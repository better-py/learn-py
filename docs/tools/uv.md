# uv

- python 包管理工具, 本项目基于此工具管理包.

## usage

```ruby
pip install uv

uv add --dev pytest isort black ruff mypy
  
  
uv add --group docs mkdocs mkdocs-material
uv run mkdocs new .

     
```

## reference

- https://docs.astral.sh/uv/concepts/projects/dependencies/#workspace-member
- uv workspace: https://docs.astral.sh/uv/concepts/projects/workspaces/