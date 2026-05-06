from pydantic import ValidationError

from schemas.rhino import RhinoSchema


def validate_rhinos(rhinos):
    print("Validating Rhinos:")
    print()
    for rhino in rhinos:
        try:
            RhinoSchema.model_validate(rhino)
            print(rhino["name"] + " Validated")
        except ValidationError as e:
            print(e.json())
    print()
    print("All Rhinos Validated")