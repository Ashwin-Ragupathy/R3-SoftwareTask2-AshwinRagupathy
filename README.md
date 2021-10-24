# R3-SoftwareTask2-AshwinRagupathy
 Task: Controlling a rover that has 4 wheels. First receive input from either a keyboard or a controller, then send this input (client) over to 
 the rover(server). The rover will then use this input to determine how to drive the motors. Must also use PWM to control the motor speed.
 
 My project works by connecting the input and output through the same socket with the output acting as the server/rover. Using pygame, the input
 program collects a keyboard input in a 200 by 200 window. This is collected from the user using events for a key being pressed to determine rover 
 speed and direction which translates to the movement that is sent to the output. Speed is determined using values 0-5 where 0 would be no movement, 
 1 is (1/5)*255, 2 is (2/5)*255,  3 is is (3/5)*255, 4 is is (4/5)*255 and 5 is 255. The direction is determined by the wasd keys with w being 
 forward, a being left, s being backward and d being right. The speed can be changed at any time and will be held for the next direction change of 
 the rover. The movement is then sent to the output program over the connected socket. If the c key is pressed the output program is told to shut off 
 the rover/server and the input  program is also closed. The output program continously waits and produces the input from the client until it is told 
 by the client to close. The direction and speed keys pressed are also repeated in the input console as confirmation of the output. 
 
 Input Method: Keyboard
 
 Screenshots of the output can be found in the github folder.
 
 Video Link: https://drive.google.com/file/d/1MKyj45QUVZHgoQFrDlq13Acgd3iWQPo4/view?usp=sharing 