def init_piles(n): #sizes board based of original Nim game so 1 3 5 7 .... N, N+2=M, M+2 and so on
    return [1 + 2*i for i in range(n)]

def game_over(piles):
    return not any(piles)

def gen_moves(piles): #all possible moves the AI can make (Dont use high number if ya gonna test it
    #to many sticks will have mannnnnnny moves)
    moves = []
    for i in range(len(piles)):
        for take in range(1, piles[i] + 1):
            moves.append((i, take))
    return moves


def apply_move(piles, move): #Makes a move
    new = piles.copy()
    new[move[0]] -= move[1]
    return new

def eval_term(perspective, current):
    return 1 if perspective == current else -1 #Evaluates kinda self explanitory

def min_max_thing(piles, perspective, current, other):
    if game_over(piles):
        return eval_term(perspective, current), None

    best_max, best_min = -2, 2
    best_max_move = best_min_move = None

    for m in gen_moves(piles):
        nxt = apply_move(piles, m)
        score, _ = min_max_thing(nxt, perspective, other, current)

        if score > best_max:
            best_max, best_max_move = score, m
            #Did add slightly agressive prune for garrunteed win or lose for timing on larger
            #sets of data testing
            if current == perspective and best_max == 1:
                return best_max, best_max_move
        if score < best_min:
            best_min, best_min_move = score, m
            if current != perspective and best_min == -1:
                return best_min, best_min_move

    if current == perspective:
        return best_max, best_max_move
    else:
        return best_min, best_min_move

def print_piles(piles): # Print curr baord with xor for user
    w = max(piles).bit_length()
    for p in piles:
        print(p, ':', format(p, f"0{w}b"))
    xor_val = 0
    for p in piles:
        xor_val ^= p
    print("XOR:", format(xor_val, f"0{w}b"))
    print()

def run():
    n = int(input("Number of piles? "))
    mode = input("Mode (H for Human vs AI, A for AI vs AI)? ")
    piles = init_piles(n)
    move_count = 0
    is_human_turn = True


    if mode == 'A':
        first, second = 'A1', 'A2'
    else:
        first, second = 'H', 'A'

    print_piles(piles)
    while True:
        if is_human_turn:
            current, other = first, second
        else:
            current, other = second, first

        # Decide move
        if current == 'H':
            r, c = input("Your move (pile count)? ").split()
            choice = (int(r) - 1, int(c))
        else:
            score, choice = min_max_thing(piles, current, current, other)
            print(current, "chooses pile", choice[0] + 1,
                  "take", choice[1], "(score", score, ")")

        piles = apply_move(piles, choice)
        move_count += 1
        print("After move", move_count)
        print_piles(piles)

        if game_over(piles):
            print(other, "wins")
            break

        is_human_turn = not is_human_turn

if __name__ == '__main__':
    while True:
        run()
