import time
from random import randint

def number_generate_with_delay(start,end):
    
    for num in range(start,end+1):
       delay_seconds = int(input("delay seconds:"))
       time.sleep(delay_seconds)
       yield num
start_num = 1

end_num = 10

Generator = number_generate_with_delay(start_num,end_num)

for result in Generator:
    print(result)