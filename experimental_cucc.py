#https://github.com/Gratunaken/broccoli/commit/b62f709d30529066febe1ed396041b1e91ec9203?diff=unified
import random
import sys
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
print("you have ",player_atk,"atk. this is the ammount of hp that will be reduced from the enemy. you can boost this number by using rage\nuse decision ˘attack˘ to attack the enemy  (1)")
player_heal=3
print("you can heal ",player_heal," ammount of hp in one round.\n use decision ˘heal˘ to heal  (2)")
player_fear=1
print("you can ˘fear˘ your enemy to reduce yor enemys ˘atk˘ and ˘heal˘ stats by ",player_fear,"  (3)")
player_rage=1
print("yo can increase your ˘atk˘ by ",player_rage," but it will reduce your hp by thea same ammount.  (4)")
poison_on_enemy=0
player_poison=1
print("you can poison your enemy by using the ˘poison˘ decision. it will reduce enemy hp by ",player_poison," every round  (5)")
stun=2
estun=0
#stun description
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
    print("enemy HP: ",enemy_hp*"I","(",enemy_hp,")" "\n enemy atk ",enemy_atk,"\n enemy heal ",enemy_heal,"\npoison on enemy ",poison_on_enemy)
    #player action
    decision=input("decision\n")
    #attack
    if decision=="attack":
        enemy_hp=enemy_hp-player_atk
    if decision=="1":
        enemy_hp=enemy_hp-player_atk
    #heal
    if decision=="heal":
        player_hp=player_hp+player_heal
        print("player hp is ",player_hp)
    if decision=="2":
        player_hp=player_hp+player_heal
        print("player hp is ",player_hp)
    #fear
    if decision=="fear":
        enemy_atk=enemy_atk-player_fear
        if enemy_atk<=0:
            enemy_heal=0
    #rage
    if decision=="rage":
        player_atk=player_atk+player_rage
        player_hp=player_hp-player_rage
        print("player atk is ",player_atk)
        print("palyer hp is ", player_hp)
    if decision=="4":
        player_atk=player_atk+player_rage
        player_hp=player_hp-player_rage
        print("player atk is ",player_atk)
        print("palyer hp is ", player_hp)
    #poison
    if decision=="poison":
        poison_on_enemy=poison_on_enemy+player_poison
    if decision=="5":
        poison_on_enemy=poison_on_enemy+player_poison
    #stun
    if decision=="stun":
        estun=stun
    if decision=="6":
        estun=stun
    rcount1=rcount1+1
    if estun<=0:
        estun=0
    while rcount1==rcount2:
            if estun==0:
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
                    print("enemy used ATTACK! player hp is ",player_hp)
                    enemy_action=1
                #heal
                if enemy_hp<og_enemy_hp/2 and enemy_action==0:
                    enemy_hp=enemy_hp+enemy_heal
                    print("enemy used HEAL! enemy hp is ",enemy_hp)
                    enemy_action=1
                print("enemy hp is ",enemy_hp)                
                print("enemy is stunned for ",estun," rounds")
                print("\n\n")
                estun=estun-1
                rcount2=rcount2+1
            else:
                print("\n\n")
                estun=estun-1
                rcount2=rcount2+1
                print("the enemy is stunned")   enemy_atk=1
            enemy_heal=enemy_heal-player_fear
        if enemy_heal<=0:
            enemy_heal=0
    if decision=="3":
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
    if decision=="4":
        player_atk=player_atk+player_rage
        player_hp=player_hp-player_rage
        print("player atk is ",player_atk)
        print("palyer hp is ", player_hp)
    #poison
    if decision=="poison":
        poison_on_enemy=poison_on_enemy+player_poison
    if decision=="5":
        poison_on_enemy=poison_on_enemy+player_poison
    #stun
    if decision=="stun":
        estun=stun
    if decision=="6":
        estun=stun
    rcount1=rcount1+1
    if estun<=0:
        estun=0
    while rcount1==rcount2:
            if estun==0:
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
                    print("enemy used ATTACK! player hp is ",player_hp)
                    enemy_action=1
                #heal
                if enemy_hp<og_enemy_hp/2 and enemy_action==0:
                    enemy_hp=enemy_hp+enemy_heal
                    print("enemy used HEAL! enemy hp is ",enemy_hp)
                    enemy_action=1
                print("enemy hp is ",enemy_hp)                
                print("enemy is stunned for ",estun," rounds")
                print("\n\n")
                estun=estun-1
                rcount2=rcount2+1
            else:
                print("\n\n")
                estun=estun-1
                rcount2=rcount2+1
                print("the enemy is stunned")
       

       

       
