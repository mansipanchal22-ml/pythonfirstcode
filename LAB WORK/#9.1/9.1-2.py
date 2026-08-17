#Q.2 Counter with count initialized to zero

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print(f"Count: {self.count}")


c1 = Counter()

c1.display()

c1.increment()
c1.increment()
c1.increment()

c1.display()