import time
import datetime
import nvidia_smi
import sys

def Watch():
  nvidia_smi.nvmlInit()
  handle = nvidia_smi.nvmlDeviceGetHandleByIndex(1)
  res = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
  time.sleep(1)
  #print(res.used)
  if res.used == 0:
    return 0
  else:
    return 1

if __name__ == "__main__":
  args = sys.argv
  vocab_size = args[1]
  watch = Watch()
  while watch==0:
    time.sleep(1)
    watch = Watch()
  start = time.time()
  while watch==1:
    print(datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc))
    time.sleep(1)
    watch = Watch()
  elapsed_time = time.time() - start
  dt = datetime.datetime.fromtimestamp(elapsed_time, datetime.timezone.utc)
  with open("time_2_test.txt","a",encoding="utf-8") as f:
    dt = dt - datetime.timedelta(days=1)
    Result = "Vocab.size:"+ vocab_size + " ,Time: " + str(dt.day) + " day" + str(dt.hour) + " h" + str(dt.minute) + " min" + str(dt.second) + " sec\n"
    print(Result)
    f.write(Result)
