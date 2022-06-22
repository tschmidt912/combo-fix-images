def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    basic.pause(5000)
    Drones.Basic_action(Drones.Basicoptions.TAKEOFF)
    Drones.Rotation_action(Drones.Angleoptions.RIGHT, 180)
    Drones.Move_action(Drones.Directionoptions.UP, 50)
    Drones.Rotation_action(Drones.Angleoptions.LEFT, 180)
    Drones.Basic_action(Drones.Basicoptions.LANDING)
    basic.show_icon(IconNames.CHESSBOARD)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString == "stop":
        radio.send_string("copy")
        basic.show_icon(IconNames.SAD)
        Drones.Basic_action(Drones.Basicoptions.LANDING)
        basic.show_icon(IconNames.GHOST)
        control.reset()
radio.on_received_string(on_received_string)

basic.show_icon(IconNames.SQUARE)
radio.set_group(33)
Drones.init_module(Drones.Runmodes.MASTER)
basic.show_icon(IconNames.YES)