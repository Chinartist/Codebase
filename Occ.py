import torch
import os
import gc
gpu_id = [1,2,3,4,5]
# os.environ["CUDA_VISIBLE_DEVICES"] = ",".join([str(i) for i in gpu_id])
mem = 50#G
x = torch.zeros(mem*1024*1024*250)
l = []
for i in gpu_id:
    l.append((x+0).to(i))
del x

gc.collect()
print("占用成功")
while 1:
    a=0
