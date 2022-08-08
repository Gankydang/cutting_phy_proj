def on_forever(a_pressed, b_pressed):
    while True:
        distance2 = grove.measure_in_centimeters(DigitalPin.P2)
        if input.button_is_pressed(Button.A):
            a_pressed2 = True
            b_pressed2 = False
        elif input.button_is_pressed(Button.B):
            b_pressed2 = True
            a_pressed2 = False
        if a_pressed2:
            basic.clear_screen()
            basic.show_icon(IconNames.YES)
            while distance2 < 5:
                servos.P0.run(50)
                distance2 = grove.measure_in_centimeters(DigitalPin.P2)
                pins.digital_write_pin(DigitalPin.P1, 1)
            
            servos.P0.stop()
            pins.digital_write_pin(DigitalPin.P1, 0)

        elif b_pressed:
            basic.clear_screen()
            basic.show_icon(IconNames.NO)
        else:
            basic.clear_screen()
            basic.show_icon(IconNames.NO)

b_pressed = False
a_pressed = False
distance = 0
on_forever(a_pressed, b_pressed)
