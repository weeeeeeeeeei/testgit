import sys

def cat():
    print('Meow!')

def default():
    print('Hello')

def dog():
    print('Woof!')

def main():
<<<<<<< HEAD
    if sys.argv[1] == 'cat':
        cat()
=======
    if sys.argv[1] == 'dog':
        dog()
>>>>>>> dog
    else:
        default()

if __name__ == '__name__':
    main()
