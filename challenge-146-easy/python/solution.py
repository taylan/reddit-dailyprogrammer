
def main():
    try:
        score = int(input('Enter score: '))
        print('Invalid score' if score < 0 or score in [1, 2, 4, 5] else 'Valid score')
    except ValueError:
        print('Invalid score')

if __name__ == '__main__':
    main()