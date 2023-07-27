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
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

    # data object to send to html
    data = {
        'success': True,
        'cpu_usage_15minAgo': math.ceil(cpu_usage_15minAgo * 100)/100,
        'cpu_usage_5minAgo': math.ceil(cpu_usage_5minAgo * 100)/100,
        'cpu_usage_1minAgo': math.ceil(cpu_usage_1minAgo * 100)/100,
        "networks": network_conns,
        'available_ram': free_memory,
        "available_space": shutil.disk_usage("/mnt/c/").free / 1000000000, # if you use windows, change what is in the string to "C:/"
        "modules": installed_packages_list,
        "kernel": platform.platform()
    }
    return render(request, "home/index.html", data)