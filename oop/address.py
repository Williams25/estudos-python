class Address:
    def __init__(self, address, city, state, country):
        self.address = address
        self.city = city
        self.state = state
        self.country = country

    def showAddress(self):
        return {
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country
        }
