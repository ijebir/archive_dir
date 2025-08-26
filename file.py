class file(object):

    def __init__(self, file_name, local_path, type="file"):
        self.file_name = file_name
        self.local_path = local_path
        self.type = type
        self.children = []

    def add_child(local_path):
        tmp = file()
        self.children.append(tmp)

    def get_path():
        return str(self.local_path)
    
    def get_type():
        return str(self.type)
    
    def build_path():
        return self.local_path + "/" + self.file_name

    def __str__(self):
        str = self.build_path() + " (" + self.get_type + ")"
        #for elm in self.children:
        #    str += "--" + elm.get_path()
        #return str