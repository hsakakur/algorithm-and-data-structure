import sys

INSERT_COMMAND_NAME = 'insert'
DELETE_COMMAND_NAME = 'delete'
DELETE_FIRST_COMMAND_NAME = 'deleteFirst'
DELETE_LAST_COMMAND_NAME = 'deleteLast'

command_name_list = [INSERT_COMMAND_NAME, DELETE_COMMAND_NAME, DELETE_FIRST_COMMAND_NAME, DELETE_LAST_COMMAND_NAME]


class DoublyLinkedListElement:
    key = None
    previous = None
    next = None


class Command:
    name = ''
    key = 0


def show_list(head):
    print_line = ''
    current = head
    while not current is None:
        print_line += (current.key + ' ')
        current = current.next
    print(print_line)


n = int(input())
delete_command_count = 0
if not (0 <= n <= 2_000_000):
    print('Please integer n is 0 or more and 2,000,000 less.', sys.stderr)
    exit(1)

command_list = []
for i in range(n):
    command = Command()
    input_command = input().split(" ")
    if not input_command[0] in command_name_list:
        print('Command name [' + input_command[0] + '] is invalid. ', sys.stderr)
        exit(1)
    if input_command[0] == INSERT_COMMAND_NAME or input_command[0] == DELETE_COMMAND_NAME:
        if not (0 <= int(input_command[1]) <= 10 ** 9):
            print('Please input process-time is 0 or more and 10**9 less.', sys.stderr)
            exit(1)
    if input_command[0] == DELETE_COMMAND_NAME:
        delete_command_count += 1
        if delete_command_count > 20:
            print('\'delete\' command Should be 20 times or less', sys.stderr)

    command.name = input_command[0]
    if input_command[0] == INSERT_COMMAND_NAME or input_command[0] == DELETE_COMMAND_NAME:
        command.key = input_command[1]
    command_list.append(command)

head = None
tail = None
for command in command_list:
    if command.name == INSERT_COMMAND_NAME:
        if head is None:
            head = tail = DoublyLinkedListElement()
            head.key = command.key
        else:
            new_head = DoublyLinkedListElement()
            new_head.key = command.key
            new_head.next = head
            head.previous = new_head
            head = new_head
    elif command.name == DELETE_COMMAND_NAME:
        current = head
        while not current is None:
            if current.key == command.key:
                if current == head:
                    current.next.previous = None
                    head = current.next
                elif current == tail:
                    current.previous.next = None
                    tail = current.previous
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                break
            current = current.next
    elif command.name == DELETE_FIRST_COMMAND_NAME:
        if not head.next is None:
            head.next.previous = None
            head = head.next
        else:
            head = None
            tail = None
    elif command.name == DELETE_LAST_COMMAND_NAME:
        if not tail.previous is None:
            tail.previous.next = None
            tail = tail.previous
        else:
            head = None
            tail = None

show_list(head)
