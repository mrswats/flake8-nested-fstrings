from __future__ import annotations

import ast
from collections.abc import Generator
from typing import Any

MSG = "NFS001 do not nest f-strings."


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.nested_fstrings: list[tuple[int, int]] = []

    def node_contains_nested_fstring(self, node: ast.expr) -> bool:
        for fieldname, value in ast.iter_fields(node):
            if fieldname == "values":
                for inner_node in value:
                    return self.node_contains_nested_fstring(inner_node)

            if fieldname == "value":
                if isinstance(value, ast.JoinedStr):
                    return True

        return False

    def visit_JoinedStr(self, node: ast.JoinedStr) -> None:
        if self.node_contains_nested_fstring(node):
            self.nested_fstrings.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]]]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col in visitor.nested_fstrings:
            yield line, col, MSG, type(self)
