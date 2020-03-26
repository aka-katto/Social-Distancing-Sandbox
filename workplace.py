from socialplace import SocialPlace
import names


class Sector:
    def __init__(self, sector_name: str, mean_salary: int, density: int, social_distancing_layoff: float):
        self.sector_name = sector_name
        self.mean_salary = mean_salary
        self.social_distancing_layoff = social_distancing_layoff
        self.density = density


class WorkPlace(SocialPlace):

    def __init__(self, sector: Sector, employees: int):
        self.name = essential_store_name = names.get_full_name() + sector.sector_name + " Establishment"

        super(sector.density, self.name).__init__()
        self.sector = sector
        self.workplace_instance = SocialPlace(sector.density, self.name)


# Places that serve people

class ServerPlace(SocialPlace):
    def __init__(self, sector: Sector, employees: int):
        self.name = essential_store_name = names.get_full_name() + sector.sector_name + " Server Store"

        super(sector.density, self.name).__init__()
        self.sector = sector
        self.workplace_instance = SocialPlace(sector.density, self.name)


