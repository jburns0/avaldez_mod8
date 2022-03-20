class LFSR:
    """
    Per the lab guidelines we include a class that will hold methods and
    local variables (should we see fit to run).
    """

    def __init__(self, seed: str, tap: int):
        """
        We declare a constructor to create the LFSR with initial state of:
        seed being a string, and tap being an int.

        :param seed: the seed needed for the lfsr to run
        :param tap: the tap needed for the XOR to run
        """
        print(f"init function triggered")
        self.seed = list(seed)
        self.tap = tap

    def __getitem__(self, index: int):
        """
        This function is in charge of returning the bit at index ‘i’ within
        the seed.

        :param index: the location of the bit we want to return
        :return: the bit at a specific index
        """
        print(f"get_index function triggered")
        return self.seed[index]

    def step(self):
        """
        This function is in charge of executing only one LFSR iteration and
        will return the new (rightmost) bit as an int.

        :return: the rightmost bit as an int
        """
        print(f"step function triggered")

    def __str__(self):
        """
        This function is in charge of returning a string representation of the
        LFSR
        :return: string representation of itself
        """
        print(f"return self __str__ triggered")
        pass

    # your executable code that invokes LFSR
    """ 
    main():
        if __name__ == “__main__”:
            main()
    """

lfsr1 = LFSR(['0110100111'], 2)
print({lfsr1})
print(lfsr1[0][3])