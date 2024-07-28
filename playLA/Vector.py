class Vector:
    def __init__(self, lst):
        self._values = lst

    def __repr__(self):
        return f"Vector({self._values})"
    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))

