import ast

import pytest

from flake8_nested_fstrings import Plugin


def results(s):
    return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


@pytest.mark.parametrize(
    "src",
    [
        "",
        "'not an fstring'",
        'f"{1}"',
    ],
)
def test_negative_cases(src):
    assert not results(src)


@pytest.mark.parametrize(
    "src",
    [
        'f"{f"{1}"}"',
        'f"{f"this is a string withing another fstring"} {1}"',
    ],
)
def test_nested_fstrings(src):
    (msg, *_) = results(src)
    assert msg == "1:0: NFS001 do not nest f-strings."
