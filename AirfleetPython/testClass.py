from aircraft import Aircraft

def createNewAircraft(reg: str, type, age):

    newAircraft = Aircraft(reg, type, age)

    print(newAircraft)

createNewAircraft("C-GHPU", "Boeing 787-8", 9.3)