from Parts import Building, BuildingPart, Room, Hallway, Stairway
from BuildingDatabase import BuildingDatabase
from BuildingFactory import BuildingFactory

# This class acts as a builder class to manipulate the BuildingDatabase (Builder Pattern)
class BuildingDatabaseManager():

    def __init__(self):
        self.building_database = BuildingDatabase()
        pass

    def get_part_list(self, part_type):
        return getattr(self.building_database, part_type+"s")

    def check_if_part_exists(self, part_type, id):
        part_list = self.get_part_list(part_type)
        for part in part_list:
            if part.id == id:
                return True
        return False

    def create_part(self, part_type, id, **kwargs):
        if not(self.check_if_part_exists(part_type, id)):
            new_part = BuildingFactory.create_part(
                part_type=part_type, id=id, **kwargs)
            part_list = self.get_part_list(part_type)
            part_list.append(new_part)
        else:
            raise ValueError("Part already exists!")
    
    def get_all_problems(self, part_type, id):
        for part in self.get_part_list(part_type):
            if part.id == id:
                return part.problems


    def get_problem(self, part_type, id, problem_id):
        if self.check_if_part_exists(part_type, id):
            for part in self.get_part_list(part_type):
                if part.id == id:
                   return part.get_problem(problem_id)
        else:
            raise ValueError("Part of type <"+part_type+"> does not exist!")

    def report_problem(self, part_type, id, problem_text, rz_username):
        if self.check_if_part_exists(part_type, id):
            for part in self.get_part_list(part_type):
                if part.id == id:
                    return part.report_problem(problem_text, rz_username)
        else:
            raise ValueError("Part of type <"+part_type+"> does not exist!")

    
    def set_problem_state(self, part_type, id, problem_id, new_state):
        if self.check_if_part_exists(part_type, id):
            for part in self.get_part_list(part_type):
                if part.id == id:
                    return part.set_problem_state(problem_id, new_state)
        else:
            raise ValueError("Part of type <"+part_type+"> does not exist!")
