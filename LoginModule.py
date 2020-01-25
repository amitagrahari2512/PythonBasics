
def main():
    if __name__ == '__main__':
        print("__name__ in Login Module : ",__name__)
        print("Welcome Team :")
        print("This lines will print when this page as act as main entry point")
        print("If any one imported that module these lines will not print.")
        print("-------------------------------------------------------------")
        print("If we not use this if statement and not check with __name__, so this method will executed, and all lines"
              "print, so that's the reason we use this statement")
        print("And its is imp to know if any file import module, so on that time all imported module statement will run.")

print("Here main() calling is act like a satement in file LoginModule")
if __name__ == '__main__':
    main()
