from address import Address


class People(Address):
    def __init__(self, name, age, active, address, city, state, country):
        super().__init__(address, city, state, country)
        self.name = name
        self.age = age
        self.active = active

    def detailsPeople(self):

        return {
            'name': self.name,
            'age': self.age,
            'active': self.active,
            'address': {
                'address': self.address,
                'city': self.city,
                'state': self.state,
                'country': self.country,
            },
        }
