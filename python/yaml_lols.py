"""This one requires pyyaml.  pyyaml is pretty not-safe by default.
Takeaway: use yaml.safe_load
"""
from __future__ import annotations

import yaml


def main():
    print(
        '>>> yaml.load('
        '"!!python/object/apply:os.system\\nargs: [\'echo hi\']"'
        ')',
    )
    print(yaml.load("!!python/object/apply:os.system\nargs: ['echo hi']"))


if __name__ == '__main__':
    raise SystemExit(main())
