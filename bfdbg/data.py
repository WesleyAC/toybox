class BrainfuckData:
    """
    This class represents a infinitely large array of 8-bit ints.
    It is not currently a very efficent implementation, but this may change.
    Interact with it via standard list syntax.
    """
    def __init__(self):
        self.data = []

    """Extend data arrya to this size"""
    def _extend(self, n):
        self.data.extend([0] * n)

    def __getitem__(self, index):
        if index >= len(self.data):
            self._extend(index - len(self.data) + 1)
        return self.data[index]

    def __setitem__(self, index, num):
        if index >= len(self.data):
            self._extend(index - len(self.data) + 1)
        self.data[index] = num % 256

    def __str__(self):
        return ' '.join(["%03d" % v for v in self.data])

    def __len__(self):
        return len(self.data)
