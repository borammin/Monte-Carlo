import scipy
import math
import random

class MonteCarlo:

    def __init__(self, start_val=1000, a=24693, c=3517, K=2**17, lambdavar=12):
        self.seed = start_val
        self.a = a
        self.c = c
        self.K = K
        self.lambdavar = lambdavar
        self.current = start_val

    def rand_num_gen(self, i):
        x = self.start_val
        for _ in range(i):
            x = (self.a * x + self.c) % self.K
        return x
        # if i <= 0:
        #     return (self.a * self.start_val + self.c) % self.K
        # return (self.a * self.rand_num_gen(i - 1) + self.c) % self.K

    def u(self, i):
        return self.rand_num_gen(i) / self.K

    def rand_var_gen():
        uniform_samples = self.rand_num_gen(1000)
        return np.array([inverse_cdf(u) for u in uniform_samples])

    def inverse_cdf(u):
        return -math.log(u) / lambdavar

    def next_rand(self):
        self.current = (self.a * self.current + self.c) % self.K
        return self.current / self.K

    def exponential(self):
        u = self.next_rand()
        return -self.lambdavar * math.log(1 - u)
    
    def call_one_customer(self):
        attempts = 0
        total_time = 0
        while attempts < 4:
            attempts += 1
            total_time += 6  # Time to turn on phone and dial
            outcome = self.next_rand()
            if outcome < 0.2:
                # Line is busy
                total_time += 3
            elif outcome < 0.5:
                # Away from phone
                total_time += 25
            else:
                # Available
                answer_time = self.exponential()
                if answer_time <= 25:
                    # Customer answered
                    total_time += answer_time + 1
                    break
                else:
                    # Did not answer in time
                    total_time += 25
            total_time += 1  # Time to end call
        return total_time

    def run_simulation(self, n=10000):
        results = [self.call_one_customer() for _ in range(n)]
        mean = sum(results) / n
        var = sum((x - mean) ** 2 for x in results) / n
        std_dev = math.sqrt(var)
        return mean, std_dev
        
# Create an instance and print values
mc = MonteCarlo()
print(f"u51: {mc.u(51)}")
print(f"u52: {mc.u(52)}")
print(f"u53: {mc.u(53)}")

mean, std_dev = mc.run_simulation()
print(f"Estimated mean time: {mean:.2f} sec")
print(f"Estimated std deviation: {std_dev:.2f} sec")
