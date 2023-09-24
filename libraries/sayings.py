import sys
import time

# I changed CS50P code for better Output

def main():
    try:
        hello(sys.argv[1])
        time.sleep(2)
        goodbye(sys.argv[1])
    except IndexError:
        hello()
        time.sleep(2)
        goodbye()


def hello(name="world"):
    print(f"hello, {name}")

def goodbye(name="world"):
    print(f"goodbye, {name}")

main()