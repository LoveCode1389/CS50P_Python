def column():
    def main():
        print_column(int(input("How many columns? ")))


    def print_column(h):
        print("#\n" * h, end="")

    main()

def row():
    def main():
        print_row(int(input("How many rows? ")))


    def print_row(w):
        print("?" * w, end="")

    main()

def square():
    def main():
        print_square(int(input("How many size? ")))

    def print_square(size):

        # For each row in square
        for i in range(size):
            print_row(size)

    main()

def print_row(w):
    print("#" * w)

user_input = input("{column / row / square} ?")


if user_input == "column":
    column()
elif user_input == "row":
    row()
elif user_input == "square":
    square()
else:
    print(f'{user_input} Does Not Exist!!')