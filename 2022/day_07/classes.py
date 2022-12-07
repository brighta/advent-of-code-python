class Directory:
    def __init__(self, path, name):
        self.type = "d"
        self.path = path
        self.name = name

    def __repr__(self):
        return self.path + " - " + self.type + " - " + self.get_directory_path()

    def get_directory_path(self):
        if self.path == "/":
            return "/" + self.name
        return self.path + "/" + self.name


class File:
    def __init__(self, path, name, size):
        self.type = "f"
        self.path = path
        self.name = name
        self.size = size

    def __repr__(self):
        return self.path + " - " + self.type + " - " + self.name + " - " + self.size
