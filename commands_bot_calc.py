
def calc(value):
    try:
        return eval(value)
    except ValueError:
        return 'Упс.Что то пошло не так.Попробуй еще раз'