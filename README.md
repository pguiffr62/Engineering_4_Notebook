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
I had to remeber how to wire an LED. Im not super comfortable with bash but this helped.
