class file(object):

    def __init__(self, local_path, type="file"):
        self.local_path = local_path
        self.type = type
        self.children = []

    def add_child(local_path):
        tmp = file()
        self.children.append(tmp)

    def __str__(self):
        print("filepath: ", self.local_path)