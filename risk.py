import random

def risk_roller():
    """
    Emulates the battles that take place during a game of risk
    """

    
    attacker = int(input('Attacker, how many units are you attacking with? '))
    defeat = int(input('Attacker, how many units are you willing to lose? '))

    while attacker < defeat:
        defeat = int(input(f"You aren't attacking with enough units. Please enter a number less than or equal to {attacker}. "))

    defender = int(input('Defender, how many units are you defending with? '))

    units_lost = 0
    
    
    attack_rolls = []
    defend_rolls = []

    while units_lost != defeat and defender > 0:
        # checks how many dice the attacker can roll based on number of units attacker has
        if attacker >= 3:
            attack_rolls.append(random.randint(1,6))
            attack_rolls.append(random.randint(1,6))
            attack_rolls.append(random.randint(1,6))
            attack_rolls.sort(reverse = True)
        elif attacker == 2:
            attack_rolls.append(random.randint(1,6))
            attack_rolls.append(random.randint(1,6))
            attack_rolls.sort(reverse = True)
        elif attacker == 1:
            attack_rolls.append(random.randint(1,6))

        # checks how many dice the defender can roll based on number of units defender has has
        if defender >= 2:
            defend_rolls.append(random.randint(1,6))
            defend_rolls.append(random.randint(1,6))
            defend_rolls.sort(reverse=True)
        elif defender == 1:
            defend_rolls.append(random.randint(1,6))

        # compares highest roll of attacker and defender 
        if attack_rolls[0] > defend_rolls[0]:
            defender = defender - 1
        elif attack_rolls[0] == defend_rolls[0]:
            attacker = attacker - 1
            units_lost = units_lost + 1
        elif attack_rolls[0] < defend_rolls[0]:
            attacker = attacker - 1
            units_lost = units_lost + 1
        
        # Checks second highest roll of attacker and defender if attacker has more than one unit
        if attacker and defender >= 2:
            if attack_rolls[1] > defend_rolls[1]:
                defender = defender - 1
            elif attack_rolls[1] == defend_rolls[1]:
                attacker = attacker - 1
                units_lost = units_lost + 1
            elif attack_rolls[1] < defend_rolls[1]:
                attacker = attacker - 1
                units_lost = units_lost + 1
        

        attack_rolls = []
        defend_rolls = []



    if defender == 0:
        print(f'The attacker has {attacker} units left, Defender has {defender} units left. Attack has won')
    elif units_lost == defeat:
        print(f'The attacker has lost {defeat} units, the Defender has survived with {defender} units left')



risk_roller()