# the following was generated using a short prompt

class Person:
    """
    A class to represent a person with validated name and age properties.
    
    Attributes:
        name (str): The person's name (must be non-empty string)
        age (int): The person's age (must be positive integer)
    """
    
    def __init__(self, name: str, age: int):
        """
        Initialize a Person instance with validated name and age.
        
        Args:
            name (str): The person's name
            age (int): The person's age
            
        Raises:
            ValueError: If name is empty or age is not positive
            TypeError: If name is not a string or age is not an integer
        """
        self.name = name
        self.age = age
    
    @property
    def name(self) -> str:
        """Get the person's name."""
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """
        Set the person's name with validation.
        
        Args:
            value (str): The name to set
            
        Raises:
            TypeError: If value is not a string
            ValueError: If value is an empty string
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    @property
    def age(self) -> int:
        """Get the person's age."""
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        """
        Set the person's age with validation.
        
        Args:
            value (int): The age to set
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not positive
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Age must be an integer")
        if value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value
    
    def __repr__(self) -> str:
        """Return a string representation of the Person."""
        return f"Person(name='{self.name}', age={self.age})"