# "Stopwatch: The Game"
"""
The aim of the game is to click at the time when the tenth fraction of a second is 0 (zero)
http://www.codeskulptor.org/#user40_0UWQVO7H7aT2sF1_0.py
"""

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

time = 0
format_time = ""
count_stops = 0
count_hits = 0
timer_is_running = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def form(t):
    global format_time
    minutes = "0"
    seconds = "00"
    tenth = "0"
    if t < 10:
        tenth = str(time)

    elif 10 < t < 600:
        seconds = str(t // 10)
        tenth = str(t % 10)
        if len(seconds) < 2:
            seconds = "0" + seconds

    elif t >= 600:
        mod_time = t // 100 / 6
        minutes = str(mod_time)
        mod_t = (t-(600 * mod_time))

        if mod_t < 10:
            tenth = str(mod_t)
        elif mod_t >= 10:
            seconds = str(mod_t // 10)
            if len(seconds) < 2:
                seconds = "0" + seconds

    format_time = minutes + ":" + seconds + "." + tenth
    return format_time


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global timer_is_running
    timer_is_running = True
    timer.start()


def stop_timer():
    global time, count_stops, count_hits, timer_is_running
    timer.stop()
    if timer_is_running:
        count_stops += 1
        if format_time[-1] == "0":
            count_hits +=1
    timer_is_running = False


def reset_timer():
    global time, count_stops, count_hits
    time = 0
    count_stops = 0
    count_hits = 0
    timer.stop()


# define event handler for timer with 0.1 sec interval
def increment():
    global time
    time += 1
    return str(time)


# define draw handler
def draw(canvas):
    global time, format_time, count_stops, count_hits
    format_time = form(time)
    canvas.draw_text(format_time, [70, 130], 70, "Green")
    canvas.draw_text(str(count_hits) + "/", [230, 30], 36, "Blue")
    canvas.draw_text(str(count_stops), [256, 30], 36, "Blue")

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, increment)
frame.set_draw_handler(draw)

frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)

# start frame
frame.start()





