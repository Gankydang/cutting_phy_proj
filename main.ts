function on_forever(a_pressed: boolean, b_pressed: boolean) {
    let distance2: number;
    let a_pressed2: boolean;
    let b_pressed2: boolean;
    while (true) {
        distance2 = grove.measureInCentimeters(DigitalPin.P2)
        if (input.buttonIsPressed(Button.A)) {
            a_pressed2 = true
            b_pressed2 = false
        } else if (input.buttonIsPressed(Button.B)) {
            b_pressed2 = true
            a_pressed2 = false
        }
        
        if (a_pressed2) {
            basic.clearScreen()
            basic.showIcon(IconNames.Yes)
            while (distance2 < 10) {
                servos.P0.run(50)
                distance2 = grove.measureInCentimeters(DigitalPin.P2)
            }
            servos.P0.stop()
        } else if (b_pressed) {
            basic.clearScreen()
            basic.showIcon(IconNames.No)
        } else {
            basic.clearScreen()
            basic.showIcon(IconNames.No)
        }
        
    }
}

let b_pressed = false
let a_pressed = false
let distance = 0
on_forever(a_pressed, b_pressed)
