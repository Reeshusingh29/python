import os

if(os.path.exists("data")):
  os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data.day{i+1}")
    #od.mkdir(f"")