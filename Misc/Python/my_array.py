class my_array():
    def __init__(self, size):
        self.size = 0
        self.size_max = size
        self.content = [None] * size

    def insert(self, item):
        if self.size == self.size_max:
            temp = self.content
            self.size_max = int(self.size * 1.5)
            self.content = [None] * self.size_max
            for i in range(len(temp)):
                self.content[i] = temp[i]
            self.content[self.size] = item
        else:
            self.content[self.size] = item
        
        self.size += 1


    def print_array(self):
        """ technically shouldn't be here, but useful for ease of... use """
        print(self.content)