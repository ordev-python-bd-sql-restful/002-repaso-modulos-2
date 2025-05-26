from numbers import Real

def meters_to_feet(meters):
    if (not isinstance(meters, Real) or meters < 0):
        raise ValueError("La distancia debe ser >= 0")
    return meters * 3.28084

def feet_to_meters(feet):
     

     return feet * 0.3048

if __name__ == "__main__":
    pass