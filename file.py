class file(object):

    def __init__(self, file_name, parent_path, local_path=".", type="file"):
        self.file_name = file_name
        self.local_path = local_path
        self.parent_path = parent_path
        self.type = type
        self.children = []

    def add_child(self, local_path):
        tmp = file()
        self.children.append(tmp)

    def get_local_path(self):
        return str(self.local_path)
    
    def get_type(self):
        return str(self.type)
    
    def build_path(self):
        return self.local_path + "/" + self.local_path

    def __str__(self):
        file_str = self.build_path() + " -> " + str(self.get_type())
        #for elm in self.children:
        #    str += "--" + elm.get_path()
        return file_str