# Project Title

A brief description of what this project does and who it's for.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10, Python 3.8

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets

```bash
code block for commands
```

## Help

Any advise for common problems or issues.
```
```bash
command to run if program contains helper info
```


## Authors

Contributors names and contact info
 [@kernferm](https://x.com/kernferm)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

This project was conceived and developed from a personal inspiration. I am grateful for the opportunity to work on this idea and bring it to life. Special thanks to everyone who supports open-source software and the community around it for providing an environment that encourages creative thinking and innovation.
```


KernFerm: PID Identifier

GitHub Copilot: To create a PID (Process Identifier) identifier function in Python, you can use the `os` module to get the current process ID. Here's a step-by-step plan in pseudocode, followed by the actual Python code:

### Pseudocode
1. Import the `os` module which provides a portable way of using operating system-dependent functionality.
2. Define a function named `get_current_pid` that does not take any arguments.
3. Inside the function, use `os.getpid()` to get the current process's ID.
4. Return the obtained PID from the function.

### Python Code
```python
import os

def get_current_pid():
    # Get the current process ID
    current_pid = os.getpid()
    return current_pid

# Example usage
if __name__ == "__main__":
    print(f"The current process ID is: {get_current_pid()}")
```

KernFerm: update this to show current PID processors that are running and not running import psutil
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


GitHub Copilot: To update the code to show processes that are currently running and not running, you can modify the [`list_processes`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fttvbu%2FOneDrive%2FDesktop%2FPID-Identifier-main%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A4%2C%22character%22%3A4%7D%5D "main.py") function to include a condition that checks the process status. If [`filter_status`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fttvbu%2FOneDrive%2FDesktop%2FPID-Identifier-main%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A4%2C%22character%22%3A33%7D%5D "main.py") is not specified, it will show all processes, including those that are running and not running. If [`filter_status`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fttvbu%2FOneDrive%2FDesktop%2FPID-Identifier-main%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A4%2C%22character%22%3A33%7D%5D "main.py") is specified, it will filter the processes based on the provided status. Here's the updated code:

```python
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
            'memory

':

 3,
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
```

This code allows the user to specify a process status to filter by (e.g., running, sleeping) or leave it blank to show all processes. The `list_processes` function will then display processes based on the specified filter and sorting criteria.

KernFerm: make me a README.MD project is called PID Identifier

GitHub Copilot: ```markdown
# PID Identifier

## Overview
PID Identifier is a Python-based tool designed to list and manage operating system processes. It provides detailed insights into running and non-running processes, including their PID (Process Identifier), name, status, memory usage, CPU time, username, and creation time. This tool leverages the `psutil` library for process management and `tabulate` for displaying information in a tabular format, making it easier for users to understand and analyze the process information.

## Features
- **List Processes:** Display all processes with detailed information.
- **Filter Processes:** Filter processes based on their status (e.g., running, sleeping).
- **Sort Processes:** Sort the process list based on various attributes like PID, name, memory usage, etc.
- **User-Friendly Interface:** Easy to navigate options for sorting and filtering processes.

## Installation

To use PID Identifier, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/PID-Identifier.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd PID-Identifier
   ```
3. **Install Dependencies:**
   Make sure you have `pip` installed and then run:
   ```bash
   pip install -r requirements.txt
   ```
   This will install `psutil` and `tabulate`, which are required for the project to run.

## Usage

To start using PID Identifier, run the following command in the terminal:

```bash
python main.py
```

Follow the on-screen prompts to select your sorting and filtering preferences. The process list will be displayed based on your selections.

## Contributing

Contributions to PID Identifier are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

## License

PID Identifier is released under the MIT License. See the LICENSE file for more details.
```

This README provides a basic structure for your project, including sections for an overview, features, installation instructions, usage guide, contribution guidelines, and license information. Adjust the content as necessary to fit your project's specifics.
