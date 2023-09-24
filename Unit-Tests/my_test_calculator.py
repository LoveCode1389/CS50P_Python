from calculator import square

# I modified the CS50P code for better output

def main():
    test_square()


def test_square():
    correct = 0

    for arg in range(20):
        arg += 1
        try:
            assert square(arg) == arg * arg
        except AssertionError:
            print(f'{arg} squared, was not {arg * arg}')
        else:
            print(f'{arg} squared, is {arg * arg}')
            correct += 1
    for j in range(5):
        print()
    print(f"This function answered {correct} out of 20 questions correctly")


if __name__ == "__main__":
    main()