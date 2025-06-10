import subprocess#type: ignore
import time
def open_powershell_instances(num_instances, command):
    for _ in range(num_instances):
        subprocess.Popen(["powershell", "-NoExit", "-Command", command], creationflags=subprocess.CREATE_NEW_CONSOLE)

determ_target_ip=input("target ip: ")
target_ip=determ_target_ip
determ_num_instances=input("how many terminals doing: ")
num_instances = determ_num_instances
try:
    number = int(determ_num_instances)
    open_powershell_instances
except ValueError:
    print("thats not a number silly")
    time.sleep(1)
    determ_num_instances

command = f"ping -t{target_ip}"
open_powershell_instances(num_instances, command)