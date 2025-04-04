class BubbleSort:
    def __init__(self, data):
        self.data = data.copy()
        self.steps = []
        self.run()

    def run(self):
        arr = self.data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                self.steps.append(arr.copy())

    def get_step(self, index):
        if index < len(self.steps):
            return self.steps[index]
        return self.steps[-1] if self.steps else self.data
