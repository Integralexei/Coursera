# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user40_ZykUqrYMak_0.py

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]  # pixels per update (1/60 seconds)

paddle1_pos = ([0, HEIGHT/2-HALF_PAD_HEIGHT], [0, HEIGHT/2+HALF_PAD_HEIGHT])
paddle2_pos = ([WIDTH-1, HEIGHT/2-HALF_PAD_HEIGHT], [WIDTH-1, HEIGHT/2+HALF_PAD_HEIGHT])

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left


def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction == RIGHT:
        ball_vel = [random.randrange(2, 5), - random.randrange(1, 4)]
    elif direction == LEFT:
        ball_vel = [- random.randrange(2, 5), - random.randrange(1, 4)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2

    score1 = 0
    score2 = 0

    spawn_ball(random.choice([RIGHT, LEFT]))


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] >= HEIGHT - BALL_RADIUS or ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] += paddle1_vel
    paddle1_pos[1][1] += paddle1_vel
    paddle2_pos[0][1] += paddle2_vel
    paddle2_pos[1][1] += paddle2_vel

    if paddle1_pos[0][1] < 0:
        print paddle1_pos[0][1]
        paddle1_pos = ([0, 0], [0, PAD_HEIGHT])
    elif paddle1_pos[1][1] > HEIGHT-1:
        print paddle1_pos[1][1]
        paddle1_pos = ([0, HEIGHT - PAD_HEIGHT - 1], [0, HEIGHT - 1])

    elif paddle2_pos[0][1] < 0:
        print paddle2_pos[0][1]
        paddle2_pos = ([WIDTH-1, 0], [WIDTH-1, PAD_HEIGHT])
    elif paddle2_pos[1][1] > HEIGHT-1:
        print paddle2_pos[1][1]
        paddle2_pos = ([WIDTH-1, HEIGHT - PAD_HEIGHT - 1], [WIDTH-1, HEIGHT - 1])

    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], 15, 'White')
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], 15, 'White')

    # determine whether paddle and ball collide
    if paddle1_pos[1][1] > ball_pos[1] > paddle1_pos[0][1] and ball_pos[0] <= 0+BALL_RADIUS+PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += ball_vel[0] * 0.1
    elif paddle2_pos[1][1] > ball_pos[1] > paddle2_pos[0][1] and ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH:
        ball_vel[0] += ball_vel[0] * 0.1
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0]-BALL_RADIUS < 0+PAD_WIDTH-10:
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos[0] + BALL_RADIUS > WIDTH-PAD_WIDTH+10:
        score1 += 1
        spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(score1), [250, 100], 50, 'White')
    canvas.draw_text(str(score2), [325, 100], 50, 'White')


def key_down(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 4

    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 4


def key_up(key):
    global paddle1_vel, paddle2_vel,  paddle1_pos

    if key == simplegui.KEY_MAP['s']:
            paddle1_vel -= 4
    elif key == simplegui.KEY_MAP['w']:
            paddle1_vel += 4

    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel += 4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 4

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.add_button('Reset', new_game)


# start frame
new_game()
frame.start()
