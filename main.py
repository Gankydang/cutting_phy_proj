def on_button_pressed_a():
    
    servos.P0.run(50)

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    servos.P0.set_angle(180)
input.on_button_pressed(Button.B, on_button_pressed_b)