class Person:
    def __init__(self):
        self.name = None
        self.height = None
        self.mass = None
        self.hair_color = None
        self.skin_color = None
        self.eye_color = None
        self.birth_year = None
        self.gender = None
        self.homeworld = None
        self.films = None
        self.species = None
        self.vehicles = None
        self.starships = None
        self.created = None
        self.edited = None
        self.url = None

    def from_json(self, person_dict):
        self.name = person_dict.get('name')
        self.height = person_dict.get('height')
        self.mass = person_dict.get('mass')
        self.hair_color = person_dict.get('hair_color')
        self.skin_color = person_dict.get('skin_color')
        self.eye_color = person_dict.get('eye_color')
        self.birth_year = person_dict.get('birth_year')
        self.gender = person_dict.get('gender')
        self.homeworld = person_dict.get('homeworld')
        self.films = person_dict.get('films')
        self.species = person_dict.get('species')
        self.vehicles = person_dict.get('vehicles')
        self.starships = person_dict.get('starships')
        self.created = person_dict.get('created')
        self.edited = person_dict.get('edited')
        self.url = person_dict.get('url')
    
    def print_name(self):
        return f"My name is {self.name}"
    

    def compare_age(self, person):
        if self.birth_year < person.birth_year:
            return f"I, {self.name}, am younger than {person.name}"

        elif self.birth_year > person.birth_year:
            return f"I, {self.name}, am older than {person.name}"

        else:
            return f"I, {self.name}, am the same age as {person.name}"
        
    
    def count_starships(self):
        starships = len(self.starships)
        return f"I, {self.name}, have {starships} starships"