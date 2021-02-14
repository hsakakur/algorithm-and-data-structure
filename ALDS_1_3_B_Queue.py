import sys, queue


class Process:
    name = ''
    time = 0


first_line_input = list(map(int, input().split(" ")))
if not (1 <= first_line_input[0] <= 100_0000):
    print('Please input integer n of is 1 or more and 100,0000 less.', sys.stderr)
    exit(1)
if not (1 <= first_line_input[1] <= 1000):
    print('Please input quantum is 1 or more and 1000 less.', sys.stderr)
    exit(1)
n = first_line_input[0]
quantum = first_line_input[1]

process_queue = queue.Queue(n)

total_time = 0
for i in range(n):
    next_n_line_input = input().split(" ")
    if not (1 <= len(next_n_line_input[0]) <= 10):
        print('Please input process-name length is 1 or more and 10 less.', sys.stderr)
        exit(1)
    if not (1 <= int(next_n_line_input[1]) <= 50_000):
        print('Please input process-time is 1 or more and 50,000 less.', sys.stderr)
        exit(1)

    process = Process()
    process.name = next_n_line_input[0]
    process.time = int(next_n_line_input[1])

    total_time += process.time
    if not (1 <= total_time <= 1_000_000):
        print('Please input process-time is 1 or more and 1,000,000 less.', sys.stderr)
        exit(1)

    process_queue.put(process)
if process_queue.qsize() != n:
    print('Invalid input. Number of processes != integer n', sys.stderr)
    exit(1)

elapsed_time = 0
while not process_queue.empty():
    exec_process = process_queue.get()

    # 後で一行でかく
    exec_time = exec_process.time if exec_process.time - quantum < 0 else quantum
    exec_process.time = exec_process.time - exec_time
    elapsed_time += exec_time

    if exec_process.time <= 0:
        print(exec_process.name + ' ' + str(elapsed_time))
    else:
        process_queue.put(exec_process)
