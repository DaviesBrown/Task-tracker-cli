import sys

from tracker import tracker


def main():
    args = sys.argv
    l_args = len(args)

    if l_args >= 2:
        command = args[1].lower()
        match command:
            case 'add':
                if l_args == 3:
                    message = tracker.create_task(sys.argv[2])
                    print(message)
                else:
                    print("Usage: app.py add <description>")
            case 'list':
                if l_args == 2:
                    return tracker.list_all()
                elif l_args == 3:
                    status = args[2]
                    return tracker.list(status)
                else:
                    print("Usage: app.py list <status(optional)>")
            case 'update':
                if l_args == 4:
                    [_, _, id, description] = args
                    message = tracker.update_task(id=id, description=description)
                    print(message)
                else:
                    print("Usage: app.py update <id> <description>")
            case 'delete':
                if l_args == 3:
                    tracker.delete_task(sys.argv[2])
                else:
                    print("Usage: app.py delete <id>")
            case 'mark-in-progress':
                if l_args == 3:
                    tracker.mark_in_progress(sys.argv[2])
                else:
                    print("Usage: app.py mark-in-progress <id>")
            case 'mark-done':
                if l_args == 3:
                    tracker.mark_done(sys.argv[2])
                else:
                    print("Usage: app.py mark-done <id>")
            case _:
                print("""
                Task CLI Help Desk
                Add Task        - Usage: task-cli add <description>
                Update Task     - Usage: task-cli update <id> <description>
                List Task       - Usage: task-cli list <status(optional)>
                Delete Task     - Usage: task-cli delete <id>
                Mark InProgress - Usage: task-cli mark-in-progress <id>
                Mark Done       - Usage: task-cli mark-done <id>
                """)


if __name__ == '__main__':
    main()
