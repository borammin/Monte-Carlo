class MonteCarlo:
    def __init__(self, start_val=1000, a=24693, c=3517, K=2**17):
        self.start_val = start_val
        self.a = a
        self.c = c
        self.K = K

    def rand_num_gen(self, i):
        if i <= 0:
            return (self.a * self.start_val + self.c) % self.K
        return (self.a * self.rand_num_gen(i - 1) + self.c) % self.K

    def u(self, i):
        return self.rand_num_gen(i) / self.K

# Create an instance and print values
mc = MonteCarlo()
print(f"u51: {mc.u(51)}")
print(f"u52: {mc.u(52)}")
print(f"u53: {mc.u(53)}")