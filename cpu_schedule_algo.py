
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


processes = [] #list of processes
while True:
    #input process information
    process_name = input("Enter a process name (or enter '0' to stop): ")

    if process_name == '0':
        break

    arrival_time = int(input("Enter arrival time: "))
    processing_time = int(input("Enter processing time: "))
    remaining_time = processing_time

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
"""



def fcfs(processes):
    scheduled = [] #list of scheduled processes (output)
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
    scheduled = [] #list of scheduled processes (output)
    current_time = 0;
    queue = []

    while processes:
        for process in processes:
            if process['arrival_time'] <= current_time and process not in queue:
                queue.append(process)

        if queue:
            process = queue.pop(0)

            time_slice = min(q, process['processing_time'])
            for _ in range(time_slice):
                scheduled.append({'name': process['name']})
                current_time += 1
                process['processing_time'] -= 1

                #check arrivals during execution
                for p in processes:
                    if p['arrival_time'] <= current_time and p not in queue and p != process:
                        queue.append(p)

            if process['processing_time'] > 0:
                queue.append(process)
            else:
                processes.remove(process)

        else:
            current_time += 1   

    

    return scheduled



def spn(processes):
    scheduled = [] #list of scheduled processes (output)
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


def srt(processes): 
    scheduled = [] #list of scheduled processes (output)
    current_time = 0

    fcfs(processes)

    queue = []

    while processes:
        for process in processes:
            if process['arrival_time'] <= current_time and process not in queue:
                queue.append(process)
        if queue:
            # sort by processing time
            queue.sort(key=lambda x: x['processing_time'])
            process = queue.pop(0)

            # run for 1 time unit
            scheduled.append({'name': process['name']})
            current_time += 1
            process['processing_time'] -= 1

            if process['processing_time'] == 0:
                processes.remove(process)

        else:
            current_time += 1

        queue = [p for p in processes if p['arrival_time'] <= current_time] #update ready queue
    return scheduled


def hrrn(processes):
    scheduled = [] #list of scheduled processes (output)
    current_time = 0

    while processes:
        queue = [p for p in processes if p['arrival_time'] <= current_time] #ready queue

        if queue:
            # calculate response ratio
            for process in queue:
                waiting_time = current_time - process['arrival_time']
                response_ratio = (waiting_time + process['processing_time']) / process['processing_time']
                process['response_ratio'] = response_ratio

            # sort by response ratio
            queue.sort(key=lambda x: x['response_ratio'], reverse=True)
            process = queue.pop(0)

            for _ in range(process['processing_time']):
                scheduled.append({'name': process['name']})
                current_time += 1

            processes.remove(process)

        else:
            current_time += 1

    return scheduled

def fb(processes, q):
    scheduled = [] #list of scheduled processes (output)
    current_time = 0
    queue1 = []
    queue2 = []
    queue3 = []

    fcfs(processes) 
    for process in processes:
        process['remaining_time'] = process['processing_time']
        queue1.append(process)

    while queue1 or queue2 or queue3:
        if queue1:
            current_process = queue1.pop(0)
            time_slice = min(q, current_process["remaining_time"])
        elif queue2:
            current_process = queue2.pop(0)
            time_slice = min(q, current_process["remaining_time"])
        elif queue3:
            current_process = queue3.pop(0) 
            time_slice = min(q, current_process["remaining_time"])




        for _ in range(time_slice):
            scheduled.append({'name': current_process["name"]})
            current_time += 1
            current_process["remaining_time"] -= 1

        if current_process["remaining_time"] > 0:
            if current_process in queue1:
                queue2.append(current_process) 
            elif current_process in queue2:
                queue3.append(current_process) 
            else:
                queue3.append(current_process)

    return scheduled

##############################################################################

if algorthm == 'a':
    print("You selected First Come First Served (FCFS)")
    print("Process execution order:")
    output = fcfs(processes)
    for o in output:
        print(o['name'])

elif algorthm == 'b':
    print("You selected Round Robin (RR)")
    q = int(input("Enter time quantum: "))
    print("Process execution order:")
    output = rr(processes, q)
    for o in output:
        print(o['name'])

elif algorthm == 'c':
    print("You selected Shortest Process Next (SPN)")
    print("Process execution order:")
    output = spn(processes)
    for o in output:
        print(o['name'])

elif algorthm == 'd':
    print("You selected Shortest Remaining Time (SRT)")
    print("Process execution order:")
    output = srt(processes)
    for o in output:
        print(o['name'])

elif algorthm == 'e':
    print("You selected Highest Response Ratio Next (HRRN)")
    print("Process execution order:")
    output = hrrn(processes)
    for o in output:
        print(o['name'])

elif algorthm == 'f':
    print("You selected Feedback (FB)")
    q = int(input("Enter time quantum: "))
    print("Process execution order:")
    output = fb(processes, q)
    for o in output:
        print(o['name'])



