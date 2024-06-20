import psutil
from tabulate import tabulate
from datetime import datetime

def list_processes(sort_by=None, filter_status=None):
    # Get the list of all processes
    processes = psutil.process_iter(['pid', 'name', 'status', 'memory_info', 'cpu_times', 'username', 'create_time'])
    process_list = []
    
    for proc in processes:
        try:
            # Retrieve process information
            pid = proc.info['pid']
            name = proc.info['name']
            status = proc.info['status']
            memory_info = proc.info['memory_info']
            cpu_times = proc.info['cpu_times']
            username = proc.info['username']
            create_time = datetime.fromtimestamp(proc.info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
            
            memory = memory_info.rss / (1024 * 1024)  # Convert bytes to MB
            cpu_time = cpu_times.user + cpu_times.system
            
            # Check if a specific status is filtered or show all
            if not filter_status or status.lower() == filter_status.lower():
                process_list.append([pid, name, status, f"{memory:.2f} MB", f"{cpu_time:.2f} sec", username, create_time])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    # Sort processes by the specified field
    if sort_by:
        sort_fields = {
            'pid': 0,
            'name': 1,
            'status': 2,
            'memory': 3,
            'cpu_time': 4,
            'username': 5,
            'create_time': 6
        }
        process_list.sort(key=lambda x: x[sort_fields[sort_by]])
    
    # Print the process information in a tabular format
    headers = ["PID", "Name", "Status", "Memory Usage", "CPU Time", "Username", "Creation Time"]
    print(tabulate(process_list, headers=headers, tablefmt="grid"))

def get_user_input():
    print("Process List Options:")
    print("1. No Sorting")
    print("2. Sort by PID")
    print("3. Sort by Name")
    print("4. Sort by Status")
    print("5. Sort by Memory Usage")
    print("6. Sort by CPU Time")
    print("7. Sort by Username")
    print("8. Sort by Creation Time")
    
    sort_options = {
        '1': None,
        '2': 'pid',
        '3': 'name',
        '4': 'status',
        '5': 'memory',
        '6': 'cpu_time',
        '7': 'username',
        '8': 'create_time'
    }
    
    sort_choice = input("Enter the number corresponding to your sort choice: ")
    sort_by = sort_options.get(sort_choice, None)
    
    filter_status = input("Enter the process status to filter by (e.g., running, sleeping) or leave blank for no filter: ")
    
    return sort_by, filter_status

if __name__ == "__main__":
    sort_by, filter_status = get_user_input()
    list_processes(sort_by, filter_status)