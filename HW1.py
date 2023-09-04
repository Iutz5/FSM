import random

s = input("Please put in a string of choice: ")
def FSM_string(s):
    next = {} # This will hold the directed graph
    # This loops through all of the characters in s
    # and keeps track of their indices
    for i, c in enumerate(s): 
        if not c in next:
            # If this is the first time seeing a particular 
            # character, we need to make a new key/value pair for it
            next[c] = []
        if i < len(s)-1: # If there is a character after this
            # Record that s[i+1] is one of the following characters
            next[c].append(s[i+1])

    res = s[0]
    max_len = len(s)
    while len(res) != max_len:
        nex_arr = next[res[-1]]
        if len(nex_arr) > 0:
            rand_char = random.randint(0, len(nex_arr)-1)
            res += nex_arr[rand_char]
        else:
            break
    return res

def run_trial():
    test = FSM_string(s)
    trials = 0
    while test != s:
        trials += 1
        test = FSM_string(s)
    return trials

for i in range(1000):
    attempt = run_trial()
    print("Trial: {}, Attempt: {}".format(i+1, attempt))