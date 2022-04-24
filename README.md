# Baseball League Manager

Baseball League Manager is a web-based application for managing baseball teams, players, and statistics. It allows users to register a team manager account. After registering, users can add and edit their own teams, players, and statistics. Sample baseball stats available for tracking include: wins, losses, and games played; batting averages, fielding percentages, and related data. While all teams and players will be viewable by guests to the web page, only registered team managers have access to add or edit their teams' and players' data. 

## Web Application
[Go to the Baseball League Manager](https://baseball-league-manager.herokuapp.com/)

## Packages
Packages include: League_App, M6_Project, and users. There is no "top-level" package. Dr. Shaffer
indicated that this was fine for this particular project.

## Usage
### View Statistics as a Guest:
```
1. Navigate to Baseball League Manager app via the link above.
2. Select "Stats" in the top left corner next to "Baseball League Manager Home".
3. Select a team from the list to view its statistics.
4. Select a player from the list to view his or her statistics. 
5. Note that you will be unable to add or edit teams or players.
6. If you accidentally select an option you are not permitted to alter, you will
   be directed to a sign-in page. If you do not have an account, you can select
   "Register" in the top right corner of the page.
```

### Register as a Team Manager:
```
1. Navigate to Baseball League Manager app via the link above.
2. Select the blue "Register>>" button.
3. Enter a username and password that meets the stated requirements.
4. Select "Register". You will know that you have registered successfully when you see, 
   "Hello, <username>." in the top right of the screen.
5. To log out, select "Log out" in the top right of the screen.
```
### Register a Team:
```
1. Ensure that you are logged in as a Team Manager. You will know that you are logged in 
   when you see, "Hello, <username>." in the top right of the screen.
2. Select "Stats" in the top left corner next to "Baseball League Manager Home".
3. Select "Register your team" at the bottom in blue.
4. Complete the form with your team's information and click "Add team".
```
### Add a Player to Your Team:
```
1. Ensure that you are logged in as a Team Manager. You will know that you are logged in 
   when you see, "Hello, <username>." in the top right of the screen.
2. Select "Stats" in the top left corner next to "Baseball League Manager Home".
3. Select your team.
4. Click "Add new player" at the bottom in blue.
5. Complete the form with your player's information and stats and click "Add player".
   Note that "Last Name" and "Full Name" are required fields.
```
### Edit Your Team:
```
1. Ensure that you are logged in as a Team Manager. You will know that you are logged in 
   when you see, "Hello, <username>." in the top right of the screen.
2. Select "Stats" in the top left corner next to "Baseball League Manager Home".
3. Select your team under "All League Teams".
4. Click "Edit team" at the bottom in blue.
5. Make desired changes and click "Save changes".
```
### Edit a Player:
```
1. Ensure that you are logged in as a Team Manager. You will know that you are logged in 
   when you see, "Hello, <username>." in the top right of the screen.
2. Select "Stats" in the top left corner next to "Baseball League Manager Home".
3. Select your player under "All League Players".
4. Click "Edit player" at the bottom in blue.
5. Make desired changes and click "Save changes".
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)