# Final Project : Capstone

Web Programming with Python and JavaScript

I have build a web application which is mobile responsive and consists of  simple game which is the main feature of the web application.
The web application utilizes Django on the back-end and JavaScript on the front-end.

App name is game which consists of all the files required to run the web application.
in templates folder there are 6 html file

1) layout.html : this is layout, it is like a base for all html file which all other html file extend.

2) login.html : it consists of  login form which will allow the user to access his/her game account.

3) registeration.html : it consists of  registration form which will allow the user to make his/her game account. When the user fills all the fields correctly and presses the register button account is created and user is automatically created.

4) lndex.html : it consists of  various options  depending on if the user is logged in or not like if the user is not logged in it will show options to either register for account or login and will redirect user accordingly.
but if the user is logged in, it will show option to play game or to see gameplay history and will redirect user accordingly. Indexpage have changing background images in which background image changes every 5 second.

5) guessgame.html : this is html page which consists of game and javascript code needed for running the game. the game is guess the secret number from 0 to 100. the game have different difficulty levels which the user can choose. The input field which accepts numbers validate number by  javascript regular expression (some call it regex). The user is also given hints depending upon the user inputs. The userhistory is also saved if the user is logged-in.

6) playerhistory.html : this is html page which show the user gameplay history like difficult level, whetter he won or lost, date-time , the secret number etc.
# Guess-a-secret-Number-game
