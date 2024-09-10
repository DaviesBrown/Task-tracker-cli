import sys

from tracker import tracker


def main():
    args = sys.argv
    if len(args) < 2:
        print('help')
    elif args[1].lower() == 'add':
            tracker.create_task(sys.argv[2])
    elif args[1].lower() == 'list':
        print('let')
    elif args[1].lower() == 'update':
        print('let')
    elif args[1].lower() == 'delete':
        print('let')
    elif args[1].lower() == 'mark-in-progress':
        print('let')
    elif args[1].lower() == 'mark-done':
        print('let')


if __name__ == '__main__':
    main()
