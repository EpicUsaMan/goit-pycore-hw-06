"""Base field class for contact record fields."""


class Field:
    """
    Base class for contact record fields.
    
    Attributes:
        value: The field value
    """
    
    def __init__(self, value: str) -> None:
        """
        Initialize a field with a value.
        
        Args:
            value: The field value to store
        """
        self.value = value
    
    def __str__(self) -> str:
        """
        Return string representation of the field.
        
        Returns:
            String representation of the field value
        """
        return str(self.value)
    
    def __repr__(self) -> str:
        """
        Return developer-friendly representation.
        
        Returns:
            String showing class name and value
        """
        return f"{self.__class__.__name__}(value={self.value!r})"
    
    def __eq__(self, other: object) -> bool:
        """
        Check equality based on value.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if values are equal, False otherwise
        """
        if not isinstance(other, Field):
            return NotImplemented
        return self.value == other.value

