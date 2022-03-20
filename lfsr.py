class LFSR:
    # create an LFSR with initial state 'seed' and tap 'tap'
    def __init__(self, initial_seed="", tap=1):
        self.initial_seed = initial_seed
        self.tap = tap

    # return the bit at index 'i'
    def bit(self, i=int):
        print(type(self.bit))
        return int(self.initial_seed[0])

    # execute one LFSR iteration and return new (rightmost) bit as an int
    # you will find the binary XOR operator useful here
    def step(self):
        new_seed = int(self.initial_seed) << 1
        print(type({self.bit}))
        right_bit = int(self.bit()) ^ self.initial_seed[tap]
        new_seed = new_seed + right_bit
        return new_seed

    # return string representation of the LFSR, ex: 01001010
    def __str__(self):
        return f"{self.new_seed}  {self.right_bit}"


# your executable code that invokes LFSR
if __name__ == '__main__':
    lfsr = LFSR()
    initial_seed = ['0110100111',
                    '0100110010',
                    '1001011101',
                    '0001001100',
                    '1010011101']
    tap = [2, 8, 5, 1, 7]
    i = 0
    for each in initial_seed:
        lfsr.initial_seed = initial_seed[i]
        lfsr.tap = tap[i]
        lfsr.step()
        i += 1
