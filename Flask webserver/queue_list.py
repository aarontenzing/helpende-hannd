import numpy as np
from time import strftime

def add_queue(cid, user_list, time_list):

    if(cid not in user_list):
        user_list.append(cid)
        time_list.append(strftime("%H:%M:%S"))
        return user_list, time_list
    
    else:
        for i in range(len(user_list)):
            if(cid == user_list[i]):
                del user_list[i], time_list[i]
                return user_list, time_list
