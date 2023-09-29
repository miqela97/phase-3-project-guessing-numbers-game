import random
import sqlite3

class Game:
    def __init__(self):
        self.secret_number = 0
        self.player_name = ""

    def initialize_game(self):
        self.secret_number = random.randint(1, 100)
        print("Welcome to the Number Guessing Game!")
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}!")

    def play_game(self):
        attempts = 0
        while True:
            guess = input("Guess a number between 1 and 100: ")
            try:
                guess = int(guess)
                attempts += 1

                if guess < self.secret_number:
                    print("Too low! Try again.")
                elif guess > self.secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations, {self.player_name}! You guessed the number {self.secret_number} in {attempts} attempts.")
                    Database.save_game_result(self.player_name, attempts)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def update_player_name(self):
        new_name = input("Enter your new name: ")
        Database.update_player_name(self.player_name, new_name)
        self.player_name = new_name
        print(f"Your name has been updated to {new_name}.")

    def delete_player(self):
        search_term = input("Enter the name of the player you want to delete: ")
        Database.delete_player(search_term)
        print(f"Player {search_term}'s data has been deleted.")

    def search_player_by_name(self):
        search_term = input("Enter the name of the player you want to search for: ")
        results = Database.search_player_by_name(search_term)
        if results:
            for row in results:
                print(f"Player: {row[0]}, Attempts: {row[1]}")
        else:
            print(f"No player with the name '{search_term}' found.")

    def main_menu(self):
        while True:
            self.menu()
            choice = input("> ")
            if choice == "1":
                print(f"Goodbye, {self.player_name}!")
                exit()
            elif choice == "2":
                self.initialize_game()
                self.play_game()
            elif choice == "3":
                Database.get_all_player_attempts()
            elif choice == "4":
                self.update_player_name()
            elif choice == "5":
                self.delete_player()
            elif choice == "6":
                self.search_player_by_name()
            else:
                print("Invalid choice")

    @staticmethod
    def menu():
        print("Please select an option:")
        print("1 - Exit the program")
        print("2 - Start the game")
        print("3 - Get all Names and Attempts")
        print("4 - Update a name")
        print("5 - Delete a name")
        print("6 - Search name")


class Database:
    @staticmethod
    def save_game_result(player_name, attempts):
        conn = sqlite3.connect('your_database_name')
        cursor = conn.cursor()
        sql = """
            INSERT INTO game_results (player_name, attempts)
            VALUES (?, ?)
        """
        cursor.execute(sql, (player_name, attempts))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_player_attempts():
        conn = sqlite3.connect('your_database_name')
        cursor = conn.cursor()
        sql = """
            SELECT player_name, attempts
            FROM game_results
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        if results:
            for row in results:
                print(f"Player: {row[0]}, Attempts: {row[1]}")
        else:
            print("No game results found.")

    @staticmethod
    def update_player_name(old_name, new_name):
        conn = sqlite3.connect('your_database_name')
        cursor = conn.cursor()
        sql = """
            UPDATE game_results
            SET player_name = ?
            WHERE player_name = ?
        """
        cursor.execute(sql, (new_name, old_name))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_player(player_name):
        conn = sqlite3.connect('your_database_name')
        cursor = conn.cursor()
        sql = """
            DELETE FROM game_results
            WHERE player_name = ?
        """
        cursor.execute(sql, (player_name,))
        conn.commit()
        conn.close()

    @staticmethod
    def search_player_by_name(player_name):
        conn = sqlite3.connect('your_database_name')
        cursor = conn.cursor()
        sql = """
            SELECT player_name, attempts
            FROM game_results
            WHERE player_name = ?
        """
        cursor.execute(sql, (player_name,))
        results = cursor.fetchall()
        conn.close()
        return results


if __name__ == "__main__":
    conn = sqlite3.connect('your_database_name')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_results (
            id INTEGER PRIMARY KEY,
            player_name TEXT,
            attempts INTEGER
        )
    """)
    conn.commit()
    conn.close()

    game = Game()
    game.main_menu()
