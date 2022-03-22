def on_gesture_tilt_left():
    Player.change(LedSpriteProperty.X, -1)
    music.play_melody("C5 - - - - - - - ", 500)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    global Bullet, Player, Enemy
    Bullet = game.create_sprite(Player.get(LedSpriteProperty.X), 3)
    basic.pause(250)
    for index in range(5):
        if Bullet.is_touching(Enemy):
            Player.delete()
            Enemy.delete()
            Bullet_from_enemy.delete()
            music.play_melody("E G F G A F A G ", 296)
            game.add_score(1)
            Bullet.delete()
            Player = game.create_sprite(2, 4)
            Enemy = game.create_sprite(0, 0)
        elif Bullet.is_touching(Bullet_from_enemy):
            Bullet_from_enemy.delete()
            Bullet.delete()
        else:
            Bullet.change(LedSpriteProperty.Y, -1)
            basic.pause(250)
    Bullet.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_tilt_right():
    Player.change(LedSpriteProperty.X, 1)
    music.play_melody("C5 - - - - - - - ", 500)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

Enemy_speed = 0
sprite = 0
EF1 = 0
Enemy_fever_1: game.LedSprite = None
Bullet_from_enemy: game.LedSprite = None
Bullet: game.LedSprite = None
Enemy: game.LedSprite = None
Player: game.LedSprite = None
Player = game.create_sprite(2, 4)
music.play_melody("B A G B E C5 E C5 ", 500)
Enemy = game.create_sprite(0, 0)

def on_every_interval():
    game.add_score(1)
loops.every_interval(60000, on_every_interval)

def on_forever():
    global Enemy_fever_1, EF1, sprite, Enemy_speed, Bullet_from_enemy
    if game.score() == 10:
        for index2 in range(5):
            Enemy_fever_1 = game.create_sprite(4, 0)
            basic.pause(250)
            EF1 = randint(0, 4)
            if EF1 == 0:
                Enemy_fever_1.delete()
                Enemy_fever_1 = game.create_sprite(0, 0)
                basic.pause(250)
                if Bullet.is_touching(Enemy_fever_1):
                    Enemy_fever_1.delete()
                    game.add_score(1)
            elif EF1 == 1:
                Enemy_fever_1.delete()
                Enemy_fever_1 = game.create_sprite(1, 0)
                basic.pause(250)
                if Bullet.is_touching(Enemy_fever_1):
                    Enemy_fever_1.delete()
                    game.add_score(1)
            elif EF1 == 2:
                Enemy_fever_1.delete()
                Enemy_fever_1 = game.create_sprite(2, 0)
                basic.pause(250)
                if Bullet.is_touching(Enemy_fever_1):
                    Enemy_fever_1.delete()
                    game.add_score(1)
            elif EF1 == 3:
                Enemy_fever_1.delete()
                Enemy_fever_1 = game.create_sprite(3, 0)
                basic.pause(250)
                if Bullet.is_touching(Enemy_fever_1):
                    Enemy_fever_1.delete()
                    game.add_score(1)
            else:
                Enemy_fever_1.delete()
                Enemy_fever_1 = game.create_sprite(4, 0)
                basic.pause(250)
                if Bullet.is_touching(Enemy_fever_1):
                    Enemy_fever_1.delete()
                    game.add_score(1)
    for index3 in range(4):
        sprite = randint(0, 1)
        if sprite == 0:
            Enemy.change(LedSpriteProperty.X, 1)
            Enemy_speed = randint(0, 2)
            if Enemy_speed == 0:
                basic.pause(100)
            elif Enemy_speed == 1:
                basic.pause(250)
            else:
                basic.pause(500)
        else:
            Bullet_from_enemy = game.create_sprite(Enemy.get(LedSpriteProperty.X), 1)
            basic.pause(500)
            Enemy.change(LedSpriteProperty.X, 1)
            if Enemy.is_deleted():
                Bullet_from_enemy.delete()
            for index4 in range(4):
                if Enemy.is_deleted():
                    Bullet_from_enemy.delete()
                Bullet_from_enemy.change(LedSpriteProperty.Y, 1)
                basic.pause(250)
                if Bullet_from_enemy.is_touching(Player):
                    Player.delete()
                    Enemy.delete()
                    music.play_melody("E B C5 A B G A F ", 300)
                    music.play_melody("E - - - - - - - ", 103)
                    basic.show_icon(IconNames.SMALL_HEART)
                    basic.show_icon(IconNames.HEART)
                    basic.show_icon(IconNames.SMALL_HEART)
                    basic.show_string("Thank you for supporting this game.")
                    basic.show_string("Made by DanielY121")
                    basic.pause(250)
                    game.game_over()
            Bullet_from_enemy.delete()
    for index5 in range(4):
        sprite = randint(0, 1)
        if sprite == 0:
            Enemy.change(LedSpriteProperty.X, -1)
            Enemy_speed = randint(0, 2)
            if Enemy_speed == 0:
                basic.pause(100)
            elif Enemy_speed == 1:
                basic.pause(250)
            else:
                basic.pause(500)
        else:
            Bullet_from_enemy = game.create_sprite(Enemy.get(LedSpriteProperty.X), 1)
            basic.pause(500)
            Enemy.change(LedSpriteProperty.X, -1)
            if Enemy.is_deleted():
                Bullet_from_enemy.delete()
            for index6 in range(4):
                if Enemy.is_deleted():
                    Bullet_from_enemy.delete()
                Bullet_from_enemy.change(LedSpriteProperty.Y, 1)
                basic.pause(250)
                if Bullet_from_enemy.is_touching(Player):
                    Player.delete()
                    Enemy.delete()
                    music.play_melody("E B C5 A B G A F ", 300)
                    music.play_melody("E - - - - - - - ", 103)
                    basic.show_icon(IconNames.SMALL_HEART)
                    basic.show_icon(IconNames.HEART)
                    basic.show_icon(IconNames.SMALL_HEART)
                    basic.show_string("Thank you for supporting this game.")
                    basic.show_string("Made by DanielY121")
                    basic.pause(250)
                    game.game_over()
            Bullet_from_enemy.delete()
basic.forever(on_forever)
