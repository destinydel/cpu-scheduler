
#1. Menu driven program (list the algorithms for the user to select)
#2. The program should accept the data such as process name, arrival time and processing time.
#3. Display the results in an appropriate form of output.
#4. The program/output maybe either in command-prompt mode (text) or graphical. 
# However, graphical implementation is preferred.



print("CPU Scheduling Algorithms:")
print(" a. First-Come, First-Served (FCFS)")
print(" b. Round Robin (RR)")
print(" c. Shortest Process Next (SPN)")
print(" d. Shortest Remaining Time (SRT)")
print(" e. Highest Response Ratio Next (HRRN)")
print(" f. Feedback (FB)")

algorthm = input("Select a scheduling algorithm (a-f): ")

processes = [] #list of processes
while True:
    #input process information
    process_name = input("Select a process or enter 'g' when done: ")
    
    if process_name == 'g':
        break
    arrival_time = int(input("Enter arrival time: "))
    processing_time = int(input("Enter processing time: "))

    #dictionary of process information
    processes.append({
        'name': process_name,
        'arrival_time': arrival_time,
        'processing_time': processing_time
    })

if algorthm == 'a':
    print("You selected First-Come, First-Served (FCFS)")

