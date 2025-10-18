# Address Book Management System

![Coverage](./coverage.svg)

A Python-based contact management system with a simple and intuitive interface for storing and managing contact information.

## Python Version

Python 3.10+ required

## Project Structure

```
├── src/
│   └── models/
│       ├── field.py           # Base field class
│       ├── name.py            # Name field with validation
│       ├── phone.py           # Phone field with 10-digit validation
│       ├── record.py          # Contact record class
│       └── address_book.py    # Address book management class
├── tests/
│   ├── test_field.py          # Tests for Field class
│   ├── test_name.py           # Tests for Name class
│   ├── test_phone.py          # Tests for Phone class
│   ├── test_record.py         # Tests for Record class
│   └── test_address_book.py   # Tests for AddressBook class
├── example.py                 # Example usage script
└── README.md                  # This file
```

## Data Models

### Field

Base class for all contact record fields.

**Attributes:**
- `value: str` - The field value

**Methods:**
- `__str__() -> str` - Return string representation of the field
- `__repr__() -> str` - Return developer-friendly representation
- `__eq__(other: object) -> bool` - Check equality based on value

### Name

Class for storing contact names. This is a mandatory field that cannot be empty.

**Attributes:**
- `value: str` - The contact's name (automatically stripped of whitespace)

**Inherits from:** `Field`

**Validation:**
- Name cannot be empty or contain only whitespace

### Phone

Class for storing phone numbers with validation.

**Attributes:**
- `value: str` - The validated phone number

**Inherits from:** `Field`

**Validation:**
- Phone number must contain only digits
- Phone number must be exactly 10 digits long

### Record

Class for storing contact information including name and phone numbers.

**Attributes:**
- `name: Name` - Contact's name (Name object)
- `phones: list[Phone]` - List of phone numbers (Phone objects)

**Methods:**
- `add_phone(phone: str) -> None` - Add a phone number to the contact
- `remove_phone(phone: str) -> None` - Remove a phone number from the contact
- `edit_phone(old_phone: str, new_phone: str) -> None` - Edit an existing phone number
- `find_phone(phone: str) -> Optional[Phone]` - Find a phone number in the contact
- `__str__() -> str` - Return user-friendly string representation
- `__repr__() -> str` - Return developer-friendly representation

### AddressBook

Class for storing and managing contact records. Inherits from `UserDict` to provide dictionary-like interface.

**Attributes:**
- `data: dict` - Dictionary storing contact records with name as key

**Inherits from:** `UserDict`

**Methods:**
- `add_record(record: Record) -> None` - Add a contact record to the address book
- `find(name: str) -> Optional[Record]` - Find a contact record by name
- `delete(name: str) -> None` - Delete a contact record by name
- `__str__() -> str` - Return user-friendly string representation of all contacts
- `__repr__() -> str` - Return developer-friendly representation

## Usage Example

```python
from src.models.address_book import AddressBook
from src.models.record import Record

# Create a new address book
book = AddressBook()

# Create a record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to the address book
book.add_record(john_record)

# Create and add a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Display all records in the book
for name, record in book.data.items():
    print(record)

# Find and edit John's phone number
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Find a specific phone in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: John: 5555555555

# Delete Jane's record
book.delete("Jane")
```

## Running the Example

To see the address book in action, run the example script:

```bash
python example.py
```

## Running Tests

This project uses `pytest` for testing. Make sure you have pytest installed:

```bash
pip install pytest
```

### Run all tests:

```bash
pytest
```

### Run tests with verbose output:

```bash
pytest -v
```

### Run specific test file:

```bash
pytest tests/test_address_book.py
pytest tests/test_record.py
pytest tests/test_phone.py
pytest tests/test_name.py
pytest tests/test_field.py
```

### Run tests with coverage:

```bash
pip install pytest-cov
pytest --cov=src --cov-report=html
```

### Generate coverage badge:

```bash
pip install coverage-badge
pytest --cov=src --cov-report=json
coverage-badge -o coverage.svg -f
```

The coverage badge will be automatically displayed at the top of this README.

## Features

✅ **Contact Management**
- Add, edit, and delete contacts
- Store multiple phone numbers per contact
- Name validation (cannot be empty)
- Phone validation (exactly 10 digits)

✅ **Search Functionality**
- Find contacts by name
- Find specific phone numbers within a contact

✅ **Data Integrity**
- Prevents duplicate contacts with the same name
- Prevents duplicate phone numbers in the same contact
- Validates phone number format before storage

✅ **User-Friendly Output**
- Clear string representations for contacts
- Informative error messages for validation failures

## Error Handling

The system provides clear error messages for common issues:

- **Empty Name**: `ValueError: Name cannot be empty`
- **Invalid Phone Format**: `ValueError: Phone number must contain only digits`
- **Wrong Phone Length**: `ValueError: Phone number must be exactly 10 digits`
- **Duplicate Contact**: `ValueError: Record with name {name} already exists`
- **Duplicate Phone**: `ValueError: Phone {phone} already exists for this contact`
- **Phone Not Found**: `ValueError: Phone {phone} not found`
- **Contact Not Found**: `KeyError: Record with name {name} not found`

## Design Principles

This project follows Python best practices:

- **Object-Oriented Design**: Clear class hierarchy with inheritance
- **Type Hints**: All methods have proper type annotations
- **Comprehensive Documentation**: Every class and method has detailed docstrings
- **Extensive Testing**: Full test coverage for all functionality
- **Simple and Readable Code**: Low complexity, shallow nesting, clear naming
- **Validation**: Input validation at the field level
- **Error Handling**: Informative error messages for all edge cases

## License
This project is created as homework for the Python Core course of Neoversity.
