from collections import deque

monster_armor = deque([int(hp) for hp in input().split(',')])
player_attack = [int(hit) for hit in input().split(',')]

killed_monsters = 0

while player_attack and monster_armor:
    
    current_monster = monster_armor.popleft()
    current_hit = player_attack.pop()
    

    if current_hit >= current_monster:
        killed_monsters += 1
        decreased_hit = current_hit - current_monster

        if player_attack:    
            player_attack[-1] += decreased_hit

        elif decreased_hit > 0:
            player_attack.append(decreased_hit)

    else:
        reduced_armor = current_monster - current_hit
        monster_armor.append(reduced_armor)

if not monster_armor:
    print("All monsters have been killed!")

if not player_attack:
    print("The soldier has been defeated.")    


print(f"Total monsters killed: {killed_monsters}")