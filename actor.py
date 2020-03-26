class Actor:

    def __init__(self):

        # infection values
        self.immune = False
        self.currently_infectious = False
        self.days_since_exposed = 0
        self.is_quarantined = False

        # personality traits
        self.social_distancing_effectiveness = 0
        self.ignores_quarantine_procedures = False

        # location values
        self.recreation_places = dict()
        self.friend_group = set()

    def wear_mask(self):
        mas
