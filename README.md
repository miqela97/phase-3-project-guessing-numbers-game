Guessing game
-------------
This is simple python guessing number game. player guesses number and game will tell higher or lower and game will count number of attempts it will take player to guess.

How To play Game 
----------------
 run game in your python enviroment.
 
 when run game player will see game has a menu where player has 6 options :
   1 - Exit the game
   2 - Start the game
   3 - Get all Names and Attempts
   4 - Update a name
   5 - Delete a name
   6 - Search name

To start game player has to chose oprion 2 and then  write name.

after game  is done player will see how many attempts it took him to guess the number.

If player wanna see othere peoples attempts for that is option 3.

also player can delete their name simply choseing option 5.

Or they can change name if they didnt want the name they choose at beginning of the game.


Database Integration
--------------------
1.id (auto-incremented)
2.player_name (text)
3.attempts (integer)
4.save_game_result: Saves a player's game result (name and attempts) in the database.
5.get_all_player_attempts: Retrieves all player names and their corresponding attempts from the database.
6.update_player_name: Updates a player's name in the database.
6.delete_player: Deletes a player's data from the database.
7.search_player_by_name: Searches for a player by name in the database.
