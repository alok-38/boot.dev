def get_title(first_name, last_name, job):
    if not first_name or not last_name or not job:
        return "Invalid input: All fields must be filled."

    title = f"{first_name} {last_name} the {job}"
    return title

print(get_title("", "Doe", "Engineer"))
print(get_title("Jane", "Doe", "Engineer"))

