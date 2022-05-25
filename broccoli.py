import sys
import random
rcount1=1
rcount2=2
print("GAME STARTED")
#generate enemy
#enemy hp
og_enemy_hp=0
enemy_hp= random.randint(6,10)
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
enemy_heal=random.randint(1,8)
int(enemy_heal)
og_enemy_heal=og_enemy_heal+enemy_heal
print("enemy heal is ",enemy_heal)
#generate player
og_player_hp=10
player_hp=10
print("you have ",player_hp," hp")
player_atk=5
print("you have ",player_atk,"atk. this is the ammount of hp that will be reduced from the enemy. you can boost this number by using rage\nuse decision ˘attack˘ to attack the enemy  ATTACK(1)")
player_heal=3
print("you can heal ",player_heal," ammount of hp in one round.\n use decision ˘heal˘ to heal HEAL(2)")
player_fear=1
print("you can ˘fear˘ your enemy to reduce yor enemys ˘atk˘ and ˘heal˘ stats by ",player_fear," FEAR(3)")
player_rage=1
print("you can increase your ˘atk˘ by ",player_rage," but it will reduce your hp by thea same ammount. RAGE(4)")
poison_on_enemy=0  
player_poison=1
print("you can poison your enemy by using the ˘poison˘ decision. it will reduce enemy hp by ",player_poison," every round POISON(5)")
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
    print("attack(1) heal(2) fear(3) rage(4) poison(5)" )
    print("enemy hp is ",enemy_hp," enemy atk is ",enemy_atk," enemy heal is ",enemy_heal)
    print("player hp is ", player_hp)
    decision=str(input("decision\n"))
    #attack
    if decision=="attack":
        enemy_hp=enemy_hp-player_atk
    if decision=="1":
        enemy_hp=enemy_hp-player_atk
    #heal
    if decision=="heal":
        player_hp=player_hp+player_heal
    if decision=="2":
        player_hp=player_hp+player_heal
    #fear
    if decision=="fear":
        enemy_atk=enemy_atk-player_fear
        enemy_heal=enemy_heal-player_fear
        if enemy_atk<=0:
            enemy_atk=1
        if enemy_heal<=0:
            enemy_heal=0
    if decision=="3":
        enemy_atk=enemy_atk-player_fear
        enemy_heal=enemy_heal-player_fear 
        if enemy_atk<=0:
            enemy_atk=1
        if enemy_heal<=0:
            enemy_heal=0
    #rage
    if decision=="rage":
        player_atk=player_atk+player_rage
        player_hp=player_hp-player_rage
        print("player atk is ",player_atk)
    if decision=="4":
        player_atk=player_atk+player_rage
        player_hp=player_hp-player_rage
        print("player atk is ",player_atk)
    #poison
    if decision=="poison":
        poison_on_enemy=poison_on_enemy+player_poison
        print("enemy poisoned!")
    if decision=="5":
        poison_on_enemy=poison_on_enemy+player_poison
        print("enemy poisoned!")
    rcount1=rcount1+1
    while rcount1==rcount2:
        #enemy action
        enemy_action=0
        #does the enemy attack or heal
        #cleanse
        if poison_on_enemy>=3 and enemy_action==0:
            poison_on_enemy=0
            print("enemy has cleansed himself!")
            enemy_action=1
        #attack
        if enemy_hp>og_enemy_hp/2 and enemy_action==0:
            player_hp=player_hp-enemy_atk
            enemy_action=1
        #heal
        if enemy_hp<og_enemy_hp/2 and enemy_action==0:
            enemy_hp=enemy_hp+enemy_heal
            enemy_action=1
        rcount2=rcount2+1
       
