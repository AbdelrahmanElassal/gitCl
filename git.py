import sys
from CInit import InitCommand
from ChashObj import hashObjectCommand



def main():
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", str(sys.argv))
    
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        InitCommand()
    elif len(sys.argv) > 2 and sys.argv[1] == "hash-object":
        print(hashObjectCommand(sys.argv[2]))
    


if __name__ == "__main__":
    main()