

class Plant:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def __repr__(self):
        return {'name':self.name, 'ID':self.ID}



plant1 = Plant("ROB", 1256)

#plant1.greet()