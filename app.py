import sys

from tracker import tracker


def main():
    args = sys.argv
    if len(args) >= 2:
        if args[1].lower() == 'add':
            if len(args) == 3:
                return tracker.create_task(sys.argv[2])
            else:
                print("Usage: app.py add <description>")
        elif args[1].lower() == 'list':
            print(let)
        elif args[1].lower() == 'update':
            if len(args) == 4:
                [_, _, id, description] = args
                message = tracker.update_task(id=id, description=description)
                print(message)
            else:
                print("Usage: app.py update <id> <description>")
        elif args[1].lower() == 'delete':
            if len(args) == 3:
                tracker.delete_task(sys.argv[2])
            else:
                print("Usage: app.py delete <id>")
        elif args[1].lower() == 'mark-in-progress':
            if len(args) == 3:
                tracker.mark_in_progress(sys.argv[2])
            else:
                print("Usage: app.py mark-in-progress <id>")
        elif args[1].lower() == 'mark-done':
            if len(args) == 3:
                tracker.mark_done(sys.argv[2])
            else:
                print("Usage: app.py mark-done <id>")
    else:
        print('help wanted')


if __name__ == '__main__':
    main()
