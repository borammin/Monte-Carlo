import numpy as np
import matplotlib.pyplot as plt
import math

# Parameters
lambdavar = 1/12
a = 24693
c = 3517
K = 2**17
seed = 1000

# Random number generator function
def rand_num_gen(n):
    values = []
    var = seed
    for _ in range(n):
        var = (a*var+c) % K
        values.append(var/K)
    return values

# Random variable generator function
def rand_var_gen(u):
    return -math.log(1 - u)/lambdavar

# Function simulating calling one customer, including the total time and the four attempts
def call_once(nums, start):
    attempts = 0
    total_time = 0
    trackind = start

    while attempts < 4:
        attempts += 1
        total_time += 6  # Time to turn on phone and dial
        outcome = nums[trackind]
        trackind += 1

        if outcome < 0.2:
            # Line is busy
            total_time += 3 # 3 to detect busy line
        elif outcome < 0.5:
            # Away from phone
            total_time += 25 # 25 to wait 5 rings
        else:
            # Available
            answer_time = nums[trackind]
            trackind += 1
            var = rand_var_gen(answer_time)
            if var <= 25:
                # Customer answered
                total_time += var # var time to speak to customer
                break
            else:
                # Did not answer in time
                total_time += 25 # 25 to wait
        total_time += 1  # 1 to hang up
    return total_time, trackind

# Running the simulation
def run(n=1000):
    randsize = n*10
    randvals = rand_num_gen(randsize)

    # Printing the requested u values
    print("u1: ", randvals[0])
    print("u2: ", randvals[1])
    print("u3: ", randvals[2])
    print("u51: ", randvals[50])
    print("u52: ", randvals[51])
    print("u53: ", randvals[52])

    ind = 0
    Wlist = []
    for _ in range(n):
        W, index = call_once(randvals, ind)
        Wlist.append(W)
    return Wlist

def statistical_analysis(Wlist):
    Wmatrix = np.array(Wlist)
    mean = np.mean(Wlist)
    quartile1 = np.percentile(Wmatrix, 25)
    median = np.median(Wmatrix)
    quartile3 = np.percentile(Wmatrix, 75)

    print("Mean: ", mean)
    print("Median: ", median)
    print("Q1: ", quartile1)
    print("Q3: ", quartile3)

    # Right tail
    for _ in [10, 20, 30, 40]:
        probability = np.mean(Wmatrix > _)
        print(f"P[W > {_}] = ", probability)

    # Left tail
    for _ in [15, 20, 30]:
        probability = np.mean(Wmatrix <= _)
        print(f"P[W <= {_}] = ", probability)

def cdf_grapher(Wlist):
    sorted_Wlist = sorted(Wlist)
    cdf = np.arange(1, len(sorted_Wlist) + 1) / len(sorted_Wlist)
    plt.plot(sorted_Wlist, cdf, marker='.', linestyle='-', label='CDF', color='blue')
    plt.title("Cumulative Distribution Function (CDF) for Total Call Time")
    plt.xlabel("Total Call Time (sec)")
    plt.ylabel("CDF Value (no unit)")
    plt.grid(True)
    plt.show()

def totaltime_calls_grapher(Wlist):
    plt.figure()
    plt.plot(range(1, len(Wlist) + 1), Wlist, marker='.', linestyle='-', color='blue')
    plt.title("Total Call Time For Each Call Attempt")
    plt.xlabel("Call Attempt")
    plt.ylabel("Total Call Time (sec)")
    plt.grid(True)
    plt.show()

def main():
    W = run(1000)
    statistical_analysis(W)
    cdf_grapher(W)
    totaltime_calls_grapher(W)

if __name__ == "__main__":
    main()
