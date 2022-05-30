import datetime

# Debugging Purposes

def debugging():
    s = "Nipun Shah 📌"
    print(f'{s = }')  # s = 'Nipun Shah 📌'  , useful for debugging purposes

    n = 10
    print(f'{n // 2 = }') # n // 2 = 5

# Conversions
def conversions():
    s3 = "Other 📌"
    print(f'{s3!r}') # 'Other 📌'
    print(f'{s3!a}') # 'Other \U0001f4cc'   | ascii
    print(f'{s3!s}')  # NOTE :- !s is applied before other string formatting

class C1:
    def __format__(self, format_spec) -> str:
        print(f'Inside format dunder {format_spec=!r}')
        return "C1()"

# Formatting
def formatting():
    '''
    format string are specific to type
    '''
    num = 123.323
    now = datetime.datetime.now()

    print(f'{now=:%Y-$m-%d}')
    print(f'{num:.2f}')
    print(f'{C1():----dsdls ldsld----}')

formatting()



