from Parts import Building, BuildingPart, Room, Hallway, Stairway

# This method uses the Factory Pattern to create objects of different types based on the given "part_type" argument.
class BuildingFactory():

    # FACTORY PATTERN
    def create_part(part_type, id, **kwargs):
        if part_type == "building":
            return Building(id=id, faculty=kwargs["faculty"])
        elif part_type == "building_part":
            return BuildingPart(id=id, building_id=kwargs["building_id"])
        elif part_type == "room":
            return Room(id=id, building_part_id=kwargs["building_part_id"])
        elif part_type == "hallway":
            return Hallway(id=id, building_part_id=kwargs["building_part_id"])
        elif part_type == "stairway":
            return Stairway(id=id, building_part_id=kwargs["building_part_id"])
        else:
            raise ValueError("Unsupported building type!")
