/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Ernest
 * Created on: Oct 2023
 * This program Moves a sprite around the perimiter of the led display
*/

// variables
let sprite: game.LedSprite = null
let pixelLocation = 0
let rotationTime: number = 0

// set up
basic.clearScreen()
basic.showIcon(IconNames.Happy)

input.onButtonPressed(Button.A, function() {
  basic.clearScreen()
  sprite = game.createSprite(0,0)

  // reset pixel movement
  while (rotationTime <= 3) {
    pixelLocation = 0

    // move pixel one
    while (pixelLocation <= 4) {
      basic.pause(500)
      sprite.move(1)
      pixelLocation++
    }

    // rotate sprite 90 degrees
    sprite.turn(Direction.Right, 90)
    rotationTime++
  }

  // end
  sprite.delete()
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})
