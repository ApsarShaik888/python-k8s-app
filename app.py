import time
import os
import sys

print("="*50,flush=True)
print(f" Hostname : {os.getenv('hostname', 'unknown')}", flush=True)
print("="*50,flush=True)

counter=0
while True:
    counter+=1
    print(f"{counter} Hello! This app is alive and running!", flush=True)
    time.sleep(5)
