# speak(f"your O S is {systeminfo.system} and {systeminfo.release[0]} version")
#                     speak(f" and processor is {systeminfo.processor}")
import psutil
import platform

def info():
    systeminfo = platform.uname()
    sys_detail=[]
    sys_detail.append(systeminfo.system)
    sys_detail.append(systeminfo.release[0:2])
    sys_detail.append(systeminfo.processor)
    sys_detail.append(systeminfo.machine)
    return sys_detail

def memory():
    memory_detail=[]
    a=psutil.virtual_memory()
    hdd = psutil.disk_usage('/')
    memory_detail.append(int(a[0]/1024000000))  # total ram (0) 
    memory_detail.append(int(a[2]/1024000000))  # usage percentage of ram (1)
    memory_detail.append(int(a[1]/1024000000))  # available ram (2)
    memory_detail.append(int(hdd.total/2**30))  # total hdd (3)
    memory_detail.append(int(hdd.used / (2**30))) #use hdd (4)
    memory_detail.append(int(hdd.free / (2**30))) #free hdd (5)
    return memory_detail
