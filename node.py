class Node:
    array: None
    value: None
    father: None
    choice: None
    alpha: None
    beta: None

    def __init__(self,array):
        self.array=array
        self.value = None
        self.father = None
        self.choice = None
        self.alpha = None
        self.beta = None
