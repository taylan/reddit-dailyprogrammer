import sys

while True:
    inp = input("Enter input: ")
    if inp == "exit":
        print("exiting")
        sys.exit(0)

    print("--" + inp + "--")
pass

