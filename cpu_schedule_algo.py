
#1. Menu driven program (list the algorithms for the user to select)
#2. The program should accept the data such as process name, arrival time and processing time.
#3. Display the results in an appropriate form of output.
#4. The program/output maybe either in command-prompt mode (text) or graphical. 
# However, graphical implementation is preferred.

#------------------------------

print("CPU Scheduling Algorithms:")
print(" a. First Come First Served (FCFS)")
print(" b. Round Robin (RR)")
print(" c. Shortest Process Next (SPN)")
print(" d. Shortest Remaining Time (SRT)")
print(" e. Highest Response Ratio Next (HRRN)")
print(" f. Feedback (FB)")

algorthm = input("Select a scheduling algorithm (a-f): ")

"""
processes = [] #list of processes
while True:
    #input process information
    process_name = input("Enter a process name (or enter '0' to stop): ")

    if process_name == '0':
        break

    arrival_time = int(input("Enter arrival time: "))
    processing_time = int(input("Enter processing time: "))

    #dictionary of process information
    processes.append({
        'name': process_name,
        'arrival_time': arrival_time,
        'processing_time': processing_time
    })

"""


processes = [] #list of processes
processes.append({'name': 'A', 'arrival_time': 0, 'processing_time': 1})
processes.append({'name': 'B', 'arrival_time': 1, 'processing_time': 9})
processes.append({'name': 'C', 'arrival_time': 2, 'processing_time': 1})
processes.append({'name': 'D', 'arrival_time': 3, 'processing_time': 9})

scheduled = [] #list of scheduled processes (output)


def fcfs(processes):
    current_time = 0
    # sort by arrival time
    processes.sort(key=lambda x: x['arrival_time'])

    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']

        for _ in range(process['processing_time']):
            scheduled.append({'name': process['name']})
            current_time += 1

    return scheduled
    

def rr(processes, q):
    current_time = 0


def spn(processes):
    current_time = 0
    queue = [p for p in processes if p['arrival_time'] <= current_time] #ready queue

    while processes:
        if queue:
            # sort by processing time
            queue.sort(key=lambda x: x['processing_time'])
            process = queue.pop(0)

            for _ in range(process['processing_time']):
                scheduled.append({'name': process['name']})
                current_time += 1

            processes.remove(process)

        else:
            current_time += 1

        queue = [p for p in processes if p['arrival_time'] <= current_time] #update ready queue
    return scheduled


def srt(processes): #copy original process list for preemption
    current_time = 0
    completed_processes = []
    queue = [p for p in processes if p['arrival_time'] <= current_time] #ready queue

    while processes:
        if queue:
            # sort by processing time
            queue.sort(key=lambda x: x['processing_time'])
            process = queue.pop(0)

            for _ in range(process['processing_time']):
                scheduled.append({'name': process['name']})
                current_time += 1

            processes.remove(process)

        else:
            current_time += 1

        queue = [p for p in processes if p['arrival_time'] <= current_time] #update ready queue
    return scheduled


##############################################################################

if algorthm == 'a':
    print("You selected First Come First Served (FCFS)")
    output = fcfs(processes)
    for o in output:
        print(o['name'])

elif algorthm == 'b':
    print("You selected Round Robin (RR)")
    q = int(input("Enter time quantum: "))
    #output = rr(processes, q)
    #for o in output:
    #    print(o['name'])

elif algorthm == 'c':
    print("You selected Shortest Process Next (SPN)")
    output = spn(processes)
    for o in output:
        print(o['name'])

elif algorthm == 'd':
    print("You selected Shortest Remaining Time (SRT)")
    #output = srt(processes)
    #for o in output:
    #    print(o['name'])

elif algorthm == 'e':
    print("You selected Highest Response Ratio Next (HRRN)")
    #output = hrrn(processes)
    #for o in output:
    #    print(o['name'])

elif algorthm == 'f':
    print("You selected Feedback (FB)")
    #output = fb(processes)
    #for o in output:
    #    print(o['name'])



