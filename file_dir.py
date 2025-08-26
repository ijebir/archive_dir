class file_dir(object):

    def __init__(self, parent_path, filename, type):
        self.parent_path = parent_path
        self.filename = filename
        self.type = type

    ###### GETTERS
    def get_parent_path(self): return str(self.parent_path)
    def get_filename(self): return str(self.filename)
    def get_type(self): return str(self.type)

    def build_path(self):
        return self.parent_path + "/" + self.filename
    
    def __str__(self):
        return self.build_path() + " -> " + self.get_type()