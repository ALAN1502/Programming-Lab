contacts1={
    "Anu":"9996663330",
    "Teena":"2233445566",
}
contacts2={
    "John":"1234567890",
    "Priya":"0987654321",
}
print("Contacts1:",contacts1)
print("Contacts2",contacts2)
merged_contacts=contacts1.copy()
merged_contacts.update(contacts2)
print("Merged contacts:")
print(merged_contacts)