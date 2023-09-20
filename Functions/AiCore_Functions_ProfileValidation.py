def validate_profile(name, age, email):
    invalid_chars = set('!@£$%^&*()')
    if any((c in invalid_chars) for c in name):
        print("found")
    else:
        print("not found")
        
validate_profile("seb @", 22, "ass")

