from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('walkingsprite_remove_background.png')

def handle_events():
    global running, x_dir, y_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
            if event.key == SDLK_LEFT:
                x_dir += 1
            if event.key == SDLK_UP:
                y_dir -= 1
            if event.key == SDLK_DOWN:
                y_dir += 1


running = True
x, y = 800 // 2, 600 // 2

frame = 0
x_dir = 0
y_dir = 0

MIN_X, MAX_X = 50, 700
MIN_Y, MAX_Y = 100, 500

frame_width = [108, 146, 144, 144, 139, 146, 146, 152, 191]
frame_height = 180

while running:
    clear_canvas()
    grass.draw(400, 300)

    current_width = frame_width[frame]

    if frame == 0:
        x_start = 0
    else:
        x_start = sum(frame_width[:frame])

    character.clip_draw(x_start, 3 * frame_height, current_width, frame_height, x, y)

    frame = (frame + 1) % 9

    update_canvas()
    handle_events()

    x += x_dir * 5
    y += y_dir * 5

    if x < MIN_X:
        x = MIN_X
    elif x > MAX_X:
        x = MAX_X

    if y < MIN_Y:
        y = MIN_Y
    elif y > MAX_Y:
        y = MAX_Y

    delay(0.05)

close_canvas()
