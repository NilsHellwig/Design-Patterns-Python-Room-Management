from Parts import Building, BuildingPart, Room, Hallway, Stairway
from BuildingDatabase import BuildingDatabase
from BuildingFactory import BuildingFactory

# This class acts as a builder class to manipulate the BuildingDatabase (Builder Pattern)


class BuildingDatabaseManager:

    def __init__(self, strategy):
        self.strategy = strategy
        self.is_authorized = False
        self.building_database = BuildingDatabase()
        pass

    def authenticate(self, user, password):
        self.is_authorized = self.strategy.authenticate(user, password)
        return self.is_authorized

    def check_auth(func):
        def wrapper(self, *args, **kwargs):
            if not(self.is_authorized):
                raise ValueError(
                    "Please login to use the BuildingDatabaseManager!")
            else:
                pass
            return func(self, *args, **kwargs)
        return wrapper

    @check_auth
    def get_all_part_data(self, part_type, as_json=False):
        retrieved_part_data = []
        for part in self.get_part_list(part_type):
            if as_json:
               part = part.as_dict()
            retrieved_part_data.append(part)
        return retrieved_part_data
    
    @check_auth
    def get_part(self, part_type, id, as_json=False):
        for part in self.get_part_list(part_type):
            if part.id == id:
                if as_json:
                   part = part.as_dict()
                return part

    @check_auth
    def get_part_list(self, part_type):
        return getattr(self.building_database, part_type+"s")

    @check_auth
    def check_if_part_exists(self, part_type, id):
        part_list = self.get_part_list(part_type)
        for part in part_list:
            if part.id == id:
                return True
        return False

    
    @check_auth
    def delete_part(self, part_type, id):
        self.building_database[part_type+"s"] = filter(lambda x: x["id"] != id, self.get_part_list(part_type))


    @check_auth
    def create_part(self, part_type, id, **kwargs):
        if not(self.check_if_part_exists(part_type, id)):
            new_part = BuildingFactory.create_part(
                part_type=part_type, id=id, **kwargs)
            part_list = self.get_part_list(part_type)
            part_list.append(new_part)
        else:
            raise ValueError("Part already exists!")

    @check_auth
    def get_all_problems(self, part_type, id):
        for part in self.get_part_list(part_type):
            if part.id == id:
                return part.problems

    @check_auth
    def get_problem(self, part_type, id, problem_id):
        if self.check_if_part_exists(part_type, id):
            for part in self.get_part_list(part_type):
                if part.id == id:
                    return part.get_problem(problem_id)
        else:
            raise ValueError("Part of type <"+part_type+"> does not exist!")

    @check_auth
    def report_problem(self, part_type, id, problem_text, rz_username_reporter):
        if self.check_if_part_exists(part_type, id):
            for part in self.get_part_list(part_type):
                if part.id == id:
                    return part.report_problem(problem_text, rz_username_reporter)
        else:
            raise ValueError("Part of type <"+part_type+"> does not exist!")

    @check_auth
    def set_problem_state(self, part_type, id, problem_id, new_state):
        if self.check_if_part_exists(part_type, id):
            for part in self.get_part_list(part_type):
                if part.id == id:
                    return part.set_problem_state(problem_id, new_state)
        else:
            raise ValueError("Part of type <"+part_type+"> does not exist!")
