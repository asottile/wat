"""This one requires pyyaml.  pyyaml is pretty not-safe by default.
Takeaway: use yaml.safe_load
"""
import yaml


def main():
    print(
        '>>> yaml.load('
        '"!!python/object/apply:os.system\\nargs: [\'echo hi\']"'
        ')'
    )
    print(yaml.load("!!python/object/apply:os.system\nargs: ['echo hi']"))


if __name__ == '__main__':
    raise SystemExit(main())
