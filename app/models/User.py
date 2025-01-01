import uuid

class User:
    def __init__(self, name, weight, height, gender, target_weight=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.weight = weight
        self.height = height
        self.gender = gender
        self.target_weight = target_weight
        self.plans = []

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_target_weight(self, new_target_weight):
        self.target_weight = new_target_weight

    def add_plan(self, plan):
        self.plans.append(plan)

    def __repr__(self):
        return (f"<User(name={self.name}, weight={self.weight}, "
                f"target_weight={self.target_weight}, height={self.height}, gender={self.gender})>")