from BuildingFactory import BuildingFactory


class BuildingDatabase():

    def __init__(self) -> None:
        self.buildings = []
        self.building_parts = []
        self.rooms = []
        self.hallways = []
        self.stairways = []