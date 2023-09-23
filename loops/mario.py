def column():
    def main():
        print_column(3)


    def print_column(h):
        print("#\n" * h, end="")

    main()

def row():
    def main():
        print_row(4)


    def print_row(w):
        print("?" * w, end="")

    main()

def square():
    def main():
        print_square(3)


    def print_square(size):
        for i in range(size):
            

    main()

user_input = input("{column / row / square} ?")


if user_input == "column":
    column()
elif user_input == "row":
    row()
elif user_input == "square":
    square()
else:
    print(f'{user_input} Does Not Exist!!')