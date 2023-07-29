from django.shortcuts import render
import os
import psutil
import platform
import pkg_resources
import shutil
import math


# miniwebsite view
def miniwebsite(request):
    # gets load average from one minute ago, 5 minutes ago and 15 minutes ago
    load1, load5, load15 = psutil.getloadavg()
    
    # we split the load across the cpu count on the system
    cpu_usage_15minAgo = (load15/os.cpu_count()) * 100
    cpu_usage_5minAgo = (load5/os.cpu_count()) * 100
    cpu_usage_1minAgo = (load1/os.cpu_count()) * 100

    # gets all the current connections on the host
    conns = psutil.net_connections()
    # filters conns list by their ip and port into a format like ip:port
    network_conns = sorted(["Network - %s:%s" % (i.laddr.ip, i.laddr.port)for i in conns])

    # gets all installed packages
    installed_packages = pkg_resources.working_set
    # filters installed_packages list by their name and version number into a format like key==version
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)for i in installed_packages])

    # not my code, gets available ram on the system
    # [0]total: total memory excluding swap
    # [1]available: available memory for processes
    # [2]percent: memory usage in percent
    # [3]used: the memory used
    # [4]free: memory not used at and is readily available
    free_memory = psutil.virtual_memory()[4]/1000000

    # data object to send to html
    data = {
        'success': True,
        'cpu_usage_15minAgo': math.ceil(cpu_usage_15minAgo * 100)/100,
        'cpu_usage_5minAgo': math.ceil(cpu_usage_5minAgo * 100)/100,
        'cpu_usage_1minAgo': math.ceil(cpu_usage_1minAgo * 100)/100,
        "networks": network_conns,
        'available_ram': free_memory,
        # to explain this, /user is the only directory we have access to when running from docker
        # because I set the workdir to /user in the dockerfile's
        # if we run from django, we can ask for available space for the entire system
        # hence if you use django to run your server instead of docker
        # and if you use windows, change what is in the string to "C:/" :  if on linux, change it to "/mnt/c/"
        "available_space": shutil.disk_usage("/usr").free / 1000000000, 
        "modules": installed_packages_list,
        "kernel": platform.platform()
    }
    return render(request, "home/index.html", data)