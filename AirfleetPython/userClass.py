class User:

    secret_name = "root"

    secret_pass = "root"

    secret_team = "admin"

    secret_privilege = "admin"

    def __init__(self, user: str, team: str, accessLevel: str, hashedPassword: str):
        self.user = user
        self.team = team
        self.accessLevel = accessLevel

        self._hashedPassword = hashedPassword

    def __str__(self):
        return f"{self.user} with {self.accessLevel} privilege."
    
    def getUser(self):
        return self.user
    
    def getUserAccessLevel(self):
        return self.accessLevel
    
    def _getHashedPassword(self):
        return self._hashedPassword