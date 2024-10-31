import datetime

# Sample data for upcoming games
upcoming_games = {
    1: {"teams": "Team A vs Team B", "date": datetime.datetime(2024, 11, 2, 18, 0)},
    2: {"teams": "Team C vs Team D", "date": datetime.datetime(2024, 11, 3, 21, 0)},
    3: {"teams": "Team E vs Team F", "date": datetime.datetime(2024, 11, 4, 19, 30)}
}

user_predictions = {}
game_outcomes = {}
notification_subscribers = []

def show_main_menu():
    print("\n--- Football Prediction System ---")
    print("1. View Upcoming Games")
    print("2. Make a Prediction")
    print("3. View Submitted Predictions")
    print("4. Update Prediction")
    print("5. Record Game Outcome (Admin)")
    print("6. View Prediction Accuracy")
    print("7. View Live Game Results")
    print("0. Exit")

def view_upcoming_games():
    print("\n--- Upcoming Games ---")
    for game_id, game_info in upcoming_games.items():
        print(f"Game ID: {game_id} | {game_info['teams']} | Date: {game_info['date']}")

def make_prediction():
    view_upcoming_games()
    game_id = int(input("Enter Game ID to predict: "))
    if game_id in upcoming_games and game_id not in game_outcomes:
        if game_id in user_predictions:
            print("Prediction for this game already exists. Update instead.")
        else:
            prediction = input("Enter your predicted winner (e.g., Team A): ")
            user_predictions[game_id] = {"prediction": prediction, "date": datetime.datetime.now()}
            print("Prediction recorded successfully.")
    else:
        print("Invalid Game ID or game outcome already recorded.")

def view_predictions():
    print("\n--- Your Predictions ---")
    if not user_predictions:
        print("No predictions made yet.")
    for game_id, details in user_predictions.items():
        print(f"Game ID: {game_id} | Predicted Winner: {details['prediction']} | Date: {details['date']}")

def update_prediction():
    view_predictions()
    game_id = int(input("Enter Game ID to update prediction: "))
    if game_id in user_predictions and upcoming_games[game_id]['date'] > datetime.datetime.now():
        new_prediction = input("Enter your new predicted winner: ")
        user_predictions[game_id]["prediction"] = new_prediction
        print("Prediction updated successfully.")
    else:
        print("Prediction cannot be updated for this game.")

def record_game_outcome():
    game_id = int(input("Enter Game ID to record outcome: "))
    if game_id in upcoming_games:
        outcome = input("Enter the actual winner (e.g., Team A): ")
        game_outcomes[game_id] = outcome
        notify_prediction_result(game_id)
        print("Game outcome recorded successfully.")
    else:
        print("Invalid Game ID.")

def notify_prediction_result(game_id):
    outcome = game_outcomes[game_id]
    for user_game_id, details in user_predictions.items():
        if user_game_id == game_id:
            prediction = details["prediction"]
            result = "correct" if prediction == outcome else "incorrect"
            print(f"Notification: Your prediction for Game {game_id} was {result}.")

def view_prediction_accuracy():
    correct = sum(1 for gid, prediction in user_predictions.items() if gid in game_outcomes and game_outcomes[gid] == prediction["prediction"])
    total = len(user_predictions)
    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"\nPrediction Accuracy: {accuracy:.2f}%")

def view_live_game_results():
    print("\n--- Live Game Results ---")
    for game_id, outcome in game_outcomes.items():
        print(f"Game ID: {game_id} | Outcome: {outcome}")

def main():
    while True:
        show_main_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            view_upcoming_games()
        elif choice == "2":
            make_prediction()
        elif choice == "3":
            view_predictions()
        elif choice == "4":
            update_prediction()
        elif choice == "5":
            record_game_outcome()
        elif choice == "6":
            view_prediction_accuracy()
        elif choice == "7":
            view_live_game_results()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
