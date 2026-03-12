class ChainedList:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def append(self, value):
        if self.value is None:
            self.value = value
        elif self.next is None:
            self.next = ChainedList(value)
        else:
            self.next.append(value)
        print("appended " + value)

    def __next__(self):
        if self.first:
            self.first = False
            return self
        self.current = self.current.next
        if self.current is None or self.current.value is None:
            raise StopIteration
        else:
            return self.current

    def __iter__(self):
        self.current = self
        self.first = True
        return self

    def __str__(self):
        r = ""
        for clelem in self:
            print("appending: " + clelem.value)
            r += clelem.value + " "
        return r


cl = ChainedList()
cl.append("a")
cl.append("b")
cl.append("c")
print(cl)
