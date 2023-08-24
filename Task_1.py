from datetime import time

def dec_time():
    begin_time = time(9,0)
    end_time = time(17,0)
    if begin_time<=Entry_time<=end_time:
       print(f"The entered time {Entry_time} is within working hours.")
    else:
       print(f"The entered time {Entry_time} is not within working hours.")
E_t = input("Enter the time: ")
Entry_time= time.fromisoformat(E_t)
dec_time()