from actor import Actor

class SocialPlace:
    actor_list = set()
    density = 0
    shutdown = False
    name = ""

    def __init__(self, density: int, name="None"):
        self.actor_list = set()
        self.density = density
        self.shutdown = False
        self.name = name

    # actor related methods
    def add_person(self, added_person: Actor):
        self.actor_list.add(added_person)

    def actor_list(self, removed_person: Actor):
        self.actor_list.remove(removed_person)

    def clear_place(self):
        self.actor_list.clear()

    # functionality related methods
    def close_place(self):
        self.shutdown = True

    def open_place(self):
        self.shutdown = False

    def is_open(self):
        return self.shutdown

    # virtual method
    def tick(self):
        pass


