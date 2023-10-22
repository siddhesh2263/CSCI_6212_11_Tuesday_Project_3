import sys
import time

# Magical eggs and floors

def solve(e, f):
    
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f
    if mem_matrix[e][f] != -1:
        return mem_matrix[e][f]
    
    min_attempts = sys.maxsize

    for k in range(1, f + 1):

        if mem_matrix[e - 1][k - 1] != -1:
            LOW = mem_matrix[e - 1][k - 1]
        else:
            LOW = solve(e - 1, k - 1)
            mem_matrix[e - 1][k - 1] = LOW
        
        if mem_matrix[e][f - k] != -1:
            HIGH = mem_matrix[e][f - k]
        else:
            HIGH = solve(e, f - k)
            mem_matrix[e][f - k] = HIGH
        
        temp = 1 + max(LOW, HIGH)
    
        min_attempts = min(min_attempts, temp)

        mem_matrix[e][f] = min_attempts

    return min_attempts

# Test cases:

e_list = [1, 5, 10, 15, 20, 25, 30, 35]
f_list = [5, 25, 50, 75, 100, 125, 150, 175]

for i in range(len(e_list) - 1):

    e = e_list[i]
    f = f_list[i]

    # The below section is written in order to execute the above algorithm 
    # multiple  times, in order to get an average consistent experimental value.
    # More number of iterations result in a better experimental value.

    rows = e + 1
    columns = f + 1
    mem_matrix = [[-1] * columns] * rows

    sum = 0
    counter = 1000000
    temp_counter = counter

    while counter > 0:
        start_time = time.time_ns()
        attempts = solve(e, f)
        end_time = time.time_ns()
        sum  = sum + (end_time - start_time)
        counter -= 1
    
    avg = sum / temp_counter

    print('e = {}, f = {} | Time: {} | Min Attempts Req: {}'.format(e, f, avg, attempts))