# -*- coding: utf-8 -*-

import time
from timeout_decorator import timeout, TimeoutError
import nvidia_smi
from threading import Thread

cond = True

def f():
	global cond
	time.sleep(100000)
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

def watch(memory_max):
	nvidia_smi.nvmlInit()
	handle = nvidia_smi.nvmlDeviceGetHandleByIndex(1)
	res = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
	time.sleep(1)
	if memory_max < res.used:
		memory_max = res.used
	with open("/mnt/mqs02/data/ogawa/BERT/preprocess-for-BERT/conbination/NUMAS/vocab_cost/recipe/32000/memory_cost_3.txt","a",encoding="utf-8") as f:
		result = str(memory_max) + "\n"
		f.write(result)
	print(memory_max)
	return memory_max

if __name__ == "__main__":
	memory_max = 0
	#thread = Thread(target=f)
	#thread.start()
	watchwatch = Watch_fin()
	while watchwatch == 0:
		time.sleep(1)
		watchwatch = Watch_fin() 
	while watchwatch==1:
		memory_max = watch(memory_max)
		watchwatch = Watch_fin()
