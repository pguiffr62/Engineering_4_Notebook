# Engineering_4_Notebook

## Dice Roller
I found the code of this assignment not too difficult as it was just a while loop and setting a range. What was difficult was staying connected to my internet I fixed this by adding another network under my etc/wpa_supplicant... nano for both my phone hotspot and home network. Once my network was up I was able to connect to my GitHub and commit and push code. 

## Calculator 
This code got more difficult because it I had to refresh myself on manual inputs. I kept on haveing errors with indentation because Im using BegalTerm so it doesnt format for you, I fixed this issue by rewritting the lines that had errors and ensuring I used the right tabs. 

## Quadratic Solver
This required inputs for a, b, c that could be manually typed by user and then those values could were added to the Quadratic formula to find the discriminant. The function prints roots for positive outcomes and no real roots for negitive. The hardest part of this assignment was pushing the code to GitHud because I was getting the error "updates were rejected because the remote contains work that you do.." 

I fixed this by searching the error where I found this solution... 

git remote add origin [//your github url]

//pull those changes

git pull origin master 

// or optionally, 'git pull origin master --allow-unrelated-histories' if you have initialized repo in github and also committed locally

//now, push your work to your new repo

git push origin master

![Screenshot 2021-01-04 at 7 53 54 PM](https://user-images.githubusercontent.com/55250502/103598830-903d4d00-4ed1-11eb-963b-b7c9d294855d.png)
the correct code for this assignment is "QuadraticSolver.py"

## Strings and Loops
This project was more confusing than it had to be I am not very familar with for loops so had to watch a few videos, initially I put the split function inside of my for loop but then had to take it out. I also had my code look like this-
for i in range(0, len(sentence)):
which was causing an error because I was asking for a input of an unset amount of numbers, switching it to- 
for letter sentence: 
  print(letter) 
worked a lot better! 

## Hang Man
This assignment took me so long and much trial and error. I found the most difficult part was connecting all of the information I had learned into one peice of code. I had to do really reteach myself how while loops and for loops worked within each other. The most important thing I had to relearn was using an array for the stick figures and word then using the while loop to test if an input letter is in the word and if its not moving to the next figure in the array. 

<img width="354" alt="Screen Shot 2021-01-29 at 6 43 38 PM" src="https://user-images.githubusercontent.com/55250502/106338507-f499c500-6261-11eb-9614-a85b6c2ac341.png">

## GPIO Pins – Bash
I had to remeber how to wire an LED(short to ground with resistor long to pin). Im not super comfortable with bash but this helped. It took me a very long time to understand how to set up bash and make it a .sh file instead of .py and to run it with bash instead of python3. the actual coding with bash was fairly simple but little syntax mistakes like counter=1 instead of counter=$1. I also used gpio -g to be able to use the actual pins like 17 and 18 instead of 0. 
## GPIO pins -Python
This was a lot of remebering old assignments with python and led and using GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) to set up pins and start at off. Then I used a while loop that ran until the counter reached 10 to turn it on sleep and then off while counting. 
## GPIO pins -SSH 
I wired the battery to the ground and 5v where my usb pins used to be and hooked up the powerbost with a micro usb. I had been using my chromebook but just switched to using the mac terminal and it is infinately better. I looked up the pin using pi@raspberrypi.local 
and then hostname -I. I made a simple bash script and it worked perfectly. 

## GPIO pins -i2c 
In this assignment I had to wire up both aaccelerometer and a OLED display and have the X, Y, and Z data displayed on the screen. I connected the aaccelerometer and a OLED display to the bread board and wired them to ground and 3.3v as well as SDA and SDL which are the 3 and 5 giopins. I uses the two copywritted codes (shapes.py and simpletest.py) as the basis for my code and jammed them together. I took out the shapes and inserted the draw.text lines into the while loop. I replaced hello world with the outputs for accel X, Y, and Z and it worked perfectly. If the conditions for my pi configuration and display screen are true then my while loop I draw three lines of text with X, Y and Z values using the accel values of the accelerometer. 

## Headless
I had to modify my code from i2c to display the data graphically for one variable on the OLED screen and have the code run when the pi starts up and be able to collect data remotely. I decided to do a line graph to depict the data. I had to add a few aspects to the code like defining a map range to create a graph for the data. I learned how to store data onto my pi and display it.

## Hello Flask
In this assignment I had to create a flask python file on my Pi that would allow me to enter my IP adress into a web browser to turn my Pi into an internet connected device. I created a App.py file and copy and pasted the flask code from canvas. I pushed it to github and then enterd my IP into a search browser and the browser retured "hello World." 
<img width="400" alt="Screen Shot 2021-03-22 at 12 54 27 PM" src="https://user-images.githubusercontent.com/55250502/112030896-1c463480-8b11-11eb-8212-2420627b7ece.png">
