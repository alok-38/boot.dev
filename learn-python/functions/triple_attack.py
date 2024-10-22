def triple_attack(damage_one, damage_two, damage_three):
    damage_sum = damage_one + damage_two + damage_three
    return damage_sum

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)
print(f"Total damage is {first_triple_attack_damage}")

