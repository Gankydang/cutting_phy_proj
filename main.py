def on_forever():
    while True:
        
        if input.button_is_pressed(Button.A):
            a_pressed2 = True
            b_pressed2 = False
        elif input.button_is_pressed(Button.B):
            b_pressed2 = True
            a_pressed2 = False
            
        if a_pressed2: # Activate the cutter if button a is pressed
            distance2 = grove.measure_in_centimeters(DigitalPin.P2) # Records the distance
            basic.clear_screen()
            basic.show_icon(IconNames.YES) # A tick indicates that cutter is activated
            
            while distance2 < 5: # When there is a plant blocking the sensor
                servos.P0.run(50) # Start cutting
                distance2 = grove.measure_in_centimeters(DigitalPin.P2)
                pins.digital_write_pin(DigitalPin.P1, 1) # While cutting, turn on the warning light
            
            servos.P0.stop()
            pins.digital_write_pin(DigitalPin.P1, 0)

        elif b_pressed: # Deactivate the cutter if button b is pressed
            basic.clear_screen()
            servos.P0.stop()
            basic.show_icon(IconNames.NO) # A cross indicates that the cutter is deactivated
        else:
            basic.clear_screen()
            basic.show_icon(IconNames.NO)

on_forever()
