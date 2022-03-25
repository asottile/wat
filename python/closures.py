from __future__ import annotations
x = (1, 2, 3)

for (replace_key, replace_value) in ((2, 4), (3, 5)):
    x = (replace_value if replace_key == p else p for p in x)

print(tuple(x))

OUTPUT = """\
(1, 2, 5)
"""
