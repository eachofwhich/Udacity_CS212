# Unit 2-17


import time





def timecall(fn, *args):
    start = time.clock()
    fn(*args)
    return time.clock() - start
