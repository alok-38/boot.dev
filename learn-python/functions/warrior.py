def become_warrior(first_name, last_name, power):
    title = first_name + ' ' + last_name + " the warrior"
    power += 1
    return title, power

print(become_warrior("Frodo", "Baggins", 5))


