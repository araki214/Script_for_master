# -*- encoding: utf-8 -*-

import psutil
import nvidia_smi
import time
from threading import Thread

cond = True
def f():
	global cond
	time.sleep(1800)
	cond = False

def Watch_fin():
	nvidia_smi.nvmlInit()
	handle = nvidia_smi.nvmlDeviceGetHandleByIndex(1)
	res = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
	time.sleep(1)
	if res.used == 0:
		return 0
	else:
		return 1

pid = 20049
p = psutil.Process(pid)
cpu_used_rss = 0
cpu_used_vms = 0

watchwatch = Watch_fin()
while watchwatch == 0:
	time.sleep(1)
	watchwatch = Watch_fin()

thread = Thread(target=f)
thread.start()
while cond:
	time.sleep(1)
	mem_rss = p.memory_info().rss
	mem_vms = p.memory_info().vms
	if cpu_used_rss < mem_rss:
		cpu_used_rss = mem_rss
	with open("result_cpu_used_rss.txt","a") as f:
		result = str(cpu_used_rss) + "\n"
		f.write(result)
	if cpu_used_vms < mem_vms:
		cpu_used_vms = mem_vms
	with open("result_cpu_used_vms.txt","a") as g:
		result = str(cpu_used_vms) + "\n"
		g.write(result)

