import userClass

class Task:

    def __init__(self, taskID: int, aircraft: str, description: str, section: str, author: userClass):
        self.taskID = taskID
        self.aircraft = aircraft
        self.taskDescription = description
        self.airframeSection = section
        self.author = author

    def __str__(self):
        return f"ID:{self.taskID} - Task for aircraft {self.aircraft}, section {self.airframeSection}"

    def getAuthor(self):
        return self.author