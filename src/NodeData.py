class NodeData:

    def __init__(self, key: int, pos: tuple):
        self._id = key
        self._weight = 0
        self._tag = 0
        self._info = ""
        self._pos = pos
        self.visited = False

    def get_id(self) -> int:
        return self._id

    def get_weight(self) -> float:
        return self._weight

    def get_info(self) -> str:
        return self._info

    def get_pos(self) -> tuple:
        return self._pos

    def set_pos(self, pos : tuple):
        self._pos = pos

    def get_tag(self) -> int:
        return self._tag

    def set_info(self, info: str):
        self._info = info

    def set_tag(self,tag : int):
        self._tag = tag

    def __repr__(self):
        return "nodeData(id: %s , weight: %s , pos: %s  )" % (
            self._id, self._weight, self._pos)
