# On a single threaded CPU, we execute some functions.  
# Each function has a unique id between 0 and N-1.

# We store logs in timestamp order that describe when a function is entered or exited.

# Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  
# For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  
# "1:end:2" means the function with id 1 ended at the end of timestamp 2.

# A function's exclusive time is the number of units of time spent in this function. 
#  Note that this does not include any recursive calls to child functions.

# The CPU is single threaded which means that only one function is being executed at a given time unit.

# Return the exclusive time of each function, sorted by their function id.

def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    stack = []
    hash_table = {}
    for i in range(n):
        hash_table[i] = 0
    for entry in logs:
        func, ops, time = entry.split(":")
        func, time = int(func), int(time)
        if not stack:
            stack.append([func, time])
        else:
            if ops == 'start':
                hash_table[stack[-1][0]] += time - stack[-1][1]
                stack.append([func, time])
            else:
                hash_table[func] += time - stack[-1][1] + 1
                stack.pop()
                if stack:
                    stack[-1][1] = time + 1
    return hash_table.values()