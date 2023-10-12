[![build status](https://github.com/mrswats/flake8-nested-fstrings/actions/workflows/main.yml/badge.svg)](https://github.com/mrswats/flake8-nested-fstrings/actions/workflows/main.yml)

# flake8-nested-fstrings

flake8 plugin which forbids nesting f-strings inside other f-strings.

:warning: Python 3.12+

## Installation

```
pip install flake8-nested-fstrings
```

## Rationale

Quoting the zen of python:

```
Flat is better than nested.

```

## Codes

| Code   | Description            |
| ------ | ---------------------- |
| NFS001 | do not nest f-strings. |

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/pycqa/flake8
  rev: 3.8.4
  hooks:
    - id: flake8
      additional_dependencies: [flake8-nested-fstrings==1.0.0]
```
