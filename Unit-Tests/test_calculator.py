from calculator import square

# I modified the CS50P code for better output

def main():
    test_square()

def test_square():
    for arg in range(20):
        arg += 1
        try:
            assert square(arg) == arg * arg
        except AssertionError:
            print(f'{arg} squared, is not {arg * arg}')
        else:
            print(f'{arg} squared, is {arg * arg}')


if __name__ == "__main__":
    main()