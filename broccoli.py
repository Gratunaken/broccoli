import random
import sys
rcount1=1
rcount2=2
print("GAME STARTED")
#generate enemy
#enemy hp
og_enemy_hp=0
enemy_hp= random.randint(5,10)
int(enemy_hp)
og_enemy_hp=og_enemy_hp+enemy_hp
print("enemy hp is ",enemy_hp)
#enemy atk
og_enemy_atk=0
enemy_atk=random.randint(1,5)
int(enemy_atk)
og_enemy_atk=og_enemy_atk+enemy_atk
print("enemy atk is ",enemy_atk)
#enemy heal
og_enemy_heal=0
enemy_heal=random.randint(1,15)
int(enemy_heal)
og_enemy_heal=og_enemy_heal+enemy_heal
print("enemy heal is ",enemy_heal)
#generate player
og_player_hp=10
player_hp=10
print("you have ",player_hp," hp")
player_atk=5
print("you have ",player_atk,"atk. this is the ammount of hp that will be reduced from the enemy. you can boost this number by using rage\nuse decision ˘attack˘ to attack the enemy")
player_heal=3
print("you can heal ",player_heal," ammount of hp in one round.\n use decision ˘heal˘ to heal")
player_fear=1
print("you can ˘fear˘ your enemy to reduce yor enemys ˘atk˘ and ˘heal˘ stats by ",player_fear)
player_rage=1
print("yo can increase your ˘atk˘ by ",player_rage," but it will reduce your hp by thea same ammount.")
poison_on_enemy=0
player_poison=1
print("you can poison your enemy by using the ˘poison˘ decision. it will reduce enemy hp by ",player_poison," every round")
print("you can skip a round by not writing anything")
while rcount1<rcount2:
    #poison ticks
    enemy_hp=enemy_hp-poison_on_enemy
    #dearh r victory
    if player_hp<=0:
        print("YOU DIED")
        sys.exit()
        exit()
    if enemy_hp<=0:
        print("YOU WIN")
        sys.exit()
        exit()
    #player action
    decision=str(input("decision\n"))
    #attack
    if decision=="attack":
        enemy_hp=enemy_hp-player_atk
    #heal
    if decision=="heal":
        player_hp=player_hp+player_heal
        print("player hp is ",player_hp)
    #fear
    if decision=="fear":
        enemy_atk=enemy_atk-player_fear
        if enemy_atk<=0:
            enemy_atk=1
            enemy_heal=enemy_heal-player_fear
        if enemy_heal<=0:
            enemy_heal=0
    #rage
    if decision=="rage":
        player_atk=player_atk+player_rage
        player_hp=player_hp-player_rage
        print("player atk is ",player_atk)
        print("palyer hp is ", player_hp)
    #poison
    if decision=="poison":
        poison_on_enemy=poison_on_enemy+player_poison
    rcount1=rcount1+1
    while rcount1==rcount2:
        #enemy action
        #does the enemy attack or heal
        #attack
        if enemy_hp>og_enemy_hp/2:
            player_hp=player_hp-enemy_atk
            print("enemy used ATTACK! player hp is ",player_hp)
        if enemy_hp<og_enemy_hp/2:
            enemy_hp=enemy_hp+enemy_heal
            print("enemy used HEAL! enemy hp is ",enemy_hp)
        print("enemy hp is ",enemy_hp)
        rcount2=rcount2+1 
