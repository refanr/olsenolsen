from OlsenState import OlsenState
from mcts import MCTS


def play():
    state = OlsenState()
    mcts = MCTS(state)

    while not state.game_over():
        print("Current state:")
        state.print()

        user_input = int(input("Enter a move: "))
        user_move = state.human_hand[user_input]

        if user_move not in state.get_legal_moves():
            pass

        state.move(user_move)
        mcts.move(user_move)

        if state.game_over():
            print("Player one won!")
            break

        print("Thinking...")

        mcts.search(8)
        num_rollouts, run_time = mcts.statistics()
        print("Statistics: ", num_rollouts, "rollouts in", run_time, "seconds")
        move = mcts.best_move()

        print("MCTS chose move: ", move)

        state.move(move)
        mcts.move(move)

        if state.game_over():
            print("Player two won!")
            break


if __name__ == "__main__":
    play()
