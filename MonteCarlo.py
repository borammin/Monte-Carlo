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
        uniform_samples = np.random.uniform(0, 1, size=n_samples)
        return np.array([inverse_cdf(u) for u in uniform_samples])

    def inverse_cdf(u):
        return -math.log(u) / lambdavar

# Create an instance and print values
mc = MonteCarlo()
print(f"u51: {mc.u(51)}")
print(f"u52: {mc.u(52)}")
print(f"u53: {mc.u(53)}")
