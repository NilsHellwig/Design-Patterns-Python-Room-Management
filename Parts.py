import uuid
from datetime import datetime


class Part:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.problems = []

    def as_dict(self):
        return self.__dict__
        

    def get_german_date_string(self):
        return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def report_problem(self, problem_text, rz_username_reporter):
        new_problem_id = str(uuid.uuid4())
        reporting_date = self.get_german_date_string()
        new_problem = {"problem_id": new_problem_id, "problem_text": problem_text,
                       "reporting_date": reporting_date, "last_change": reporting_date,
                       "rz_username_reporter": rz_username_reporter, "problem_state": "gemeldet"}
        self.problems.append(new_problem)
        return new_problem

    def get_problem(self, problem_id):
        for problem in self.problems:
            if problem["problem_id"] == problem_id:
                return problem

    def set_problem_state(self, problem_id, new_state):
        for problem in self.problems:
            if problem["problem_id"] == problem_id:
                if problem["problem_state"] != new_state:
                    problem["problem_state"] = new_state
                    problem["last_change"] = self.get_german_date_string()
                return problem


class Building(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faculty = kwargs["faculty"]


class BuildingPart(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.building_id = kwargs["building_id"]


class Room(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.building_part_id = kwargs["building_part_id"]


class Hallway(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.building_part_id = kwargs["building_part_id"]


class Stairway(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.building_part_id = kwargs["building_part_id"]
