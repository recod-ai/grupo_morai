---
title: Formatação e Documentação
linkTitle: Formatação
weight: 1
---

## Documentação

```bash
pip install mkdocstrings-python
pip install mkdocs-api-autonav
pip install mkdocs-material
mkdocs new .
mkdocs serve
mkdocs build
```

```yaml
mkdocs.yml
site_name: Snee


theme:
 name: readthedocs


nav:
- index.md


plugins:
- mkdocstrings
- mkdocs-jupyter
- api-autonav:
   modules: ['molearn']

```

## Formatação

- Ruff: https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff
- É bom seguir pep8 e formatar com black (ruff consegue fazer isso).
- Consegue dar sugestões.
- Formata documento com, click right -> Format Document
- mypy: https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker
- `pip install mypy (no sistema todo)`

