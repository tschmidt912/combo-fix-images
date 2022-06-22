input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(5000)
    Drones.Basic_action(Drones.Basicoptions.Takeoff)
    Drones.Rotation_action(Drones.Angleoptions.Right, 180)
    Drones.Move_action(Drones.Directionoptions.Up, 50)
    Drones.Rotation_action(Drones.Angleoptions.Left, 180)
    Drones.Basic_action(Drones.Basicoptions.Landing)
    basic.showIcon(IconNames.Chessboard)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "stop") {
        radio.sendString("copy")
        basic.showIcon(IconNames.Sad)
        Drones.Basic_action(Drones.Basicoptions.Landing)
        basic.showIcon(IconNames.Ghost)
        control.reset()
    }
})
basic.showIcon(IconNames.Square)
radio.setGroup(33)
Drones.initModule(Drones.Runmodes.Master)
basic.showIcon(IconNames.Yes)
