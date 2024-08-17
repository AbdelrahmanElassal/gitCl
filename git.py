import sys
from Init.CInit import InitCommand



def main():
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", str(sys.argv))
    
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        InitCommand()

    


if __name__ == "__main__":
    main()