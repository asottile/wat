import traceback


def eval_and_print(s):
    try:
        print('>>> {}'.format(s))
        print(eval(s))
    except Exception:
        traceback.print_exc()


def main():
    eval_and_print('not False == True')
    eval_and_print('True == not False')


if __name__ == '__main__':
    raise SystemExit(main())
