def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * .75
    return lesser_cursed, greater_cursed

damage_value = 100
print(curse(damage_value))
print(curse(float(damage_value)))

