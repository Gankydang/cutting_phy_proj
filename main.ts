input.onButtonPressed(Button.A, function on_button_pressed_a() {
    servos.P0.run(50)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    servos.P0.setAngle(180)
})
