# Entertainment Quiz Game.. 

[Deployed Site](https://the-entertainment-quiz-game.herokuapp.com/)  
(Note: Ctrl + click to open in a new tab)    

### Developer: Prithpal Phull

I've created a Game as Portfolio Project #3 (Python Essentials) for Diploma in Full Stack Software Development at [Code Institute](https://www.codeinstitute.net).

The project purpose is presentation of an interactive game. The site should respond to the users actions.
  
<br>

# Table of content 

*   [Project](#project)
    *   [Site user goals](#site-owner-goals)
    *   [Site owner goals](#user-goals)
*   [User Experience](#user-experience)
    *   [Target Audience](#target-audience)
    *   [User Requirements and Expectations](#user-requirements-and-expectations)
*   [Features](#features)    
    *   [Game introduction](#game-introduction)
    *   [Entertainment categories](#entertainment-categories)
    *   [Instruction](#instructions)
    *   [Questions](#questions)
    *   [Score](#score)
*   [Technology](#technology)
    *   [Language used](#language-used)
    *   [Tools used](#Tools-used)
    *   [Import requirements](#import-requirements)
*   [Testing and validation](testing-validation)
    *   [Bugs/known issues](#bugsknown-issues)
    *   [Peer review](#peer-review)
*   [Deployment](#deployment)
    *   [Heroku](#heroku)
*   [Credits](#credits)
    *   [Code](#code)
    *   [Learning-Resorces](#learning-resources)
    *   [Acknowledgements](#acknowledgements)

#   Project
##  Site user goals
- To play a quiz game based on Entertainment.
- To test your knowledge on a variety of Entertainment.

## Site owner goals
- To provide a fun entertainment quiz game for a user.
- To provide a variety of entertainment categories to choose from.
- To provide a score, once the quiz is finished. 
- To show which questions the user would of got wrong.

[Back to Top](<#table-of-content>)
## User Experience

### Target Audience
- Anyone who has an interest in General Entertainment.

### User Requirements and Expectations
- When selecting an entertainment category, its on the specific subject they choose.
- To show their score, once the quiz is finished.
- Also to show once finished, which questions they might of got wrong.

[Back to Top](<#table-of-content>)
## Features

### Game Introduction
- When you first run the code, a message will appear saying 'Hi.... Want you to test your 
  Entertainment Knowledge'.
- You choose either, 'A for yes' or 'B for No'.
- If you choose 'A' to game moves on. 
- If you choose 'B' for no. the game will simply end and say 'Hope you come back soon!'.

### Entertainment Categories

- Once you've clicked on 'A for Yes' in wanting to play the quiz.
- There are a series of categories to choose from.
- You can choose by selecting a number 1 to 4 from either - <br>(1). Movies.<br>(2). Music.<br>(3). 
  Sport.<br>(4). Television.

### Instuctions

- Once you've chosen a category of your choice, instructions will appear
  on how to play the quiz. Choosing only the choice letter to the correct answer.
- How much you get for each question right, and how much you loose for getting each 
  question wrong.
- It then mentions the quiz will start momentarily, and wishing you good luck...

### Questions

- Each category has selection of 5 questions you need to get right.
- All the questions are multiple choice.
- You choose either 'a, b, c or d', to the correct answer. You can click either upper or lower case.
- If you click on anything other than the choosen letter, it will say 'Invalid choice. Choose 
  again'. 
- The option will appear again 'Enter choice [a/b/c/d]'.
- Each question carries 1 point, if you get it right.
- If you get it wrong, you loose a point.

### Score

- Once you have completed all 5 questions, results will appear.
- It will show you the resuts to each question you have got right, and which ones you have got 
  wrong.
- Either by displaying 'Correct' or 'Incorrect'
- If it's incorrect, it will display the correct answer.
- Your score will appear at the botton. On how many you have got right, out of 5.

[Back to Top](<#table-of-content>)
## Technology

### Language used
- [Python](https://www.python.org/)

### Tools Used

- [GitPod](https://gitpod.io/)

- [Heroku](https://heroku.com/)

- [GitHub](https://github.com/)

### Import requirements

- [.json](https://www.json.org)

- [time](https://docs.python.org/3/library/time.html)

[Back to Top](<#table-of-content>)
## Testing and validation

I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems.
   * On your Gitpod Workspace, ran the command 'pip3 install pycodestyle'.<br>(Note, that this extention may already be installed, in which case it will do nothing).
   * In your workspace, press Ctrl+Shift+P(or Cmd+Shift+P on Mac).
   * Type the word 'linter' into the search bar that appears, and click on 'python: Select Linter'.<br>As shown in [image 1](views/readme-images/linter.png)
   * Select 'pycodestyle' from the list. As shown in [image 2](views/readme-images/image2.png)
   * PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab besides your terminal.<br>As shown in [image 3](views/readme-images/image3.png)


 ### Peer review

   - I asked my friends and coleagues to test the quiz and I received a lot of positive    feedback, no major issues were reported.
   - Maybe add more questions.
   - For future reference, could add levels of difficulty and a timer.

 [Back to Top](<#table-of-content>)
 ## Deployment

 ### Heroku

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)
  * Log in to your account at heroku.com.
  * Create a new app, add a unique app name and choose your region.
  * Click on create app.
  * Go to "Settings".
  * Under Config Vars store any sensitive data in .json file. Name 'Key' field, copy the .json file paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
  * Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
  * Go to "Deploy" and select "GitHub" in "Deployment method"
  * To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
  * Choose the branch you want to buid your app from.
  * If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
  *  Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

[Back to Top](<#table-of-content>)
##  Credits

### Code
  * Code Institute Slack community, helping me get through this project.
  * My Mentor, Sammy Dartnall making sure i covered all the necessary requirements.

### Learning resources

- [Code Institute course and learning platform](https://codeinstitute.net/)
- [W3Schools](https://www.w3schools.com/js/default.asp)
- [Youtube](https://www.youtube.com/)

###  Acknowledgements

- My Mentor Sammy Dartnell for helpful feedback and guidance on stages of the project. 
- Code Institute Slack Community for being a great knowledge base.

[Back to Top](<#table-of-content>)









