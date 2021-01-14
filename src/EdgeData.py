class EdgeData:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = 0
        self.info = ""

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def get_info(self):
        return self.info

    def set_info(self, str):
        self.info = str

    def get_tag(self):
        return self.tag

    def set_tag(self, t):
        self.tag = t

