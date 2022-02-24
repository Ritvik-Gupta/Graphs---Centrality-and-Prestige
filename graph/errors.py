class NodesWithSameID(Exception):
    def __init__(self, id: str):
        super().__init__(f"Same ID encountered twice ID = {id}")


class NoSuchNodeWithID(Exception):
    def __init__(self, id: str):
        super().__init__(f"No such Node found with ID = {id}")
