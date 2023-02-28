dice_combinations = {
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}

for dice_1 in range(1, 7):
    for dice_2 in range(1, 7):
        sum_of_dice = dice_1 + dice_2

        dice_combinations[sum_of_dice].append((dice_1, dice_2))

print(dice_combinations)
