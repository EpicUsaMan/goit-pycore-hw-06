"""Address book class for managing contact records."""

from collections import UserDict
from typing import Optional
from src.models.record import Record


class AddressBook(UserDict):
    """
    Class for storing and managing contact records.
    
    Inherits from UserDict to provide dictionary-like interface.
    Records are stored with contact name as key.
    
    Attributes:
        data: Dictionary storing contact records (inherited from UserDict)
    """
    
    def add_record(self, record: Record) -> None:
        """
        Add a contact record to the address book.
        
        Args:
            record: The Record object to add
            
        Raises:
            ValueError: If record with this name already exists
        """
        if record.name.value in self.data:
            raise ValueError(f"Record with name {record.name.value} already exists")
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Optional[Record]:
        """
        Find a contact record by name.
        
        Args:
            name: The contact name to search for
            
        Returns:
            Record object if found, None otherwise
        """
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        """
        Delete a contact record by name.
        
        Args:
            name: The contact name to delete
            
        Raises:
            KeyError: If record with this name is not found
        """
        if name not in self.data:
            raise KeyError(f"Record with name {name} not found")
        del self.data[name]
    
    def __str__(self) -> str:
        """
        Return user-friendly string representation.
        
        Returns:
            String showing all contacts in the address book
        """
        if not self.data:
            return "Address book is empty"
        
        contacts = [str(record) for record in self.data.values()]
        return "\n".join(contacts)
    
    def __repr__(self) -> str:
        """
        Return developer-friendly representation.
        
        Returns:
            String showing class name and number of records
        """
        return f"AddressBook(records={len(self.data)})"

