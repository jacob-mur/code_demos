import pandas
from pydantic import BaseModel, field_validator
from typing import Optional

# define your model — each field has a type, Pydantic enforces it
class User(BaseModel):
    name: str
    age: int
    email: str
    bio: Optional[str] = None  # Optional field with a default of None

    # custom validator: age must be 0–120
    @field_validator("age") # validator function acts as a @classmethod by default, 
                            # which is why it requires @classmethod below @field_validator decorator.
    @classmethod # @classmethod is used to create a method that works with the class instead of an object instance
    def age_must_be_realistic(cls, age):
        if not (0 <= age <= 120):
            raise ValueError("Age must be between 0 and 120")
        return age

    # custom validator: email must include an @
    @field_validator("email")
    @classmethod
    def email_must_have_at(cls, email):
        if "@" not in email:
            raise ValueError("Email must have @ sign")
        return email

# --- valid data ---
raw_json = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
        "bio": 'graduated 2020'

}

# upacking
user = User(**raw_json)
print(user)

## --- invalid data ---
invalid_raw_json = {
    "name": "Alice",
    "age": 300,
    "email": "alice@example.com"   
    }

# upacking
user_2 = User(**invalid_raw_json)
print(user_2)

## --- invalid data ---
invalid_raw_json_2 = {
    "name": "Alice",
    "age": 23,
    "email": "aliceexample.com"
    }

# upacking
user_2 = User(**invalid_raw_json_2)

