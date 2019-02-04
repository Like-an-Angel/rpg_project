from persons import Person
from magics import Magic

start_prompt = "You are playing the Demontower!\nEnter the name of the player:\n > "
player_name = input(start_prompt)

firebolt = Magic("Firebolt", 10, 30, "Dark")
magmaspike = Magic("Magma spike", 15, 50, "Dark")
meteorite = Magic("Meteorite", 20, 70, "Dark")

magic_list = [firebolt, magmaspike, meteorite]

# Person.addmagic(firebolt, magmaspike, meteorite)

p = Person(player_name,150,100,70, magic_list)
e = Person("The Evil Guy",100,100,50, magic_list)
# iterate the battle until the end
while True:
    # output the state of the parties
    p.statout()
    e.statout()
    # Actions of all characters
    while True:
        p.choose_action()
        try:
            pact = int(input("Choose your action (in a digit format):\n")) # TODO
        except ValueError:
            print("Choose a number")
            continue
        if pact < 1 or pact > len(p.action):
            print("Action not in the list, try again!")
        else:
            p.act_index = pact - 1
            break
    # Performing the actions
    if p.act_index == 0:
        dmg = p.generate_attack_damage()
        e.take_damage(dmg)
        print("\n{} is performing {}, dealing {} damage".format(p.name, p.action[p.act_index], dmg))
    elif p.act_index == 1:
        while True:
	        p.choose_magic()
	        try:
	            pmag = int(input("Choose your magic (in a digit format):\n")) # TODO
	        except ValueError:
	            print("Print a digit (Example: '1'): \n")
	            continue
	        if pmag < 1 or pmag > len(p.magic):
	            print("Magic is not in the list, try again!")
	        else:
	            p.mag_index = pmag - 1
	            break
        sdmg = p.magic[p.mag_index].generate_magic_dmg()
        e.take_damage(sdmg)
        print(p.magic[p.mag_index].cost)
        p.reduce_mp(p.magic[p.mag_index].cost)
        print("\n{} is casting {}, dealing {} damage".format(p.name, p.magic[p.mag_index].spell, sdmg))

    # Enemy is attacking by default
    e.act_index = 0
    if e.act_index == 0:
        dmg = e.generate_attack_damage()
        p.take_damage(dmg)
        print("{} is doing a {}, dealing {} damage".format(e.name, e.action[e.act_index], dmg))
    # p.statout()
    # e.statout()
    # Checking battle ending
    if p.hp <= 0 or e.hp <= 0:
        break

print("\nAftermath of the battle:")
if p.hp > 0:
    print("Brave {} has survived the fight with {} hp remaining!".format(p.name, p.hp))
else:
    print("Brave {} hasn't survived the fight...")
if e.hp > 0:
    print("Enemy is grinning, being left alive with {} hp".format(e.hp))
else:
    print("Enemy was defeated. Bards will sing ballads of this epic fight")
