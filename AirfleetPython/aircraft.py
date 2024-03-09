class Aircraft:

    def __init__(self, registration: str, aircraftType: str, age: int):
        self.aircraftRegistration = registration

        self.aircraftType = aircraftType

        self.age = age

    def __str__(self):
        return f"{self.aircraftRegistration}: {self.aircraftType}"