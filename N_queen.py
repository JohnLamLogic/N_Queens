def success(state):
   board = state[0]
   return (len(board) == n)


def is_safe(board, row, col):
   i = 0
   while i < len(board):
       if board[i] == row:
           return False
       if (board[i] + i) == (row + col) or (board[i] - i) == (row - col):
           return False
       i += 1
   return True


def print_b(board):
   r = 0
   while r < n:
       line = ""
       c = 0
       while c < n:
           if c < len(board) and board[c] == r:
               line += " Q "
           else:
               line += " - "
           c += 1
       print(line)
       r += 1




def Score(state):
   board = state[0]
   col = len(board)
   safe_rout = 0
   for r in range(n):
       if is_safe(board, r, col):
           safe_rout += 1
   score = len(board) + (safe_rout / float(n))
   return -score



#PART 2
def solve_bfs(initial_state, closed):
   heap = []
   tie = 0
   initial_prior = Score(initial_state)
   heapq.heappush(heap, (initial_prior, tie, initial_state))
   tie += 1


   while heap:
       cur_pri, _, current_s = heapq.heappop(heap)
       board = current_s[0]
       if success(current_s):
           print("BFS solution (moves):", current_s[1])
           print_b(board)
           return True


       board_hash = tuple(board)
       if board_hash in closed:
           continue
       closed.add(board_hash)


       col = len(board)
       for r in range(n):
           if is_safe(board, r, col):
               new_b = board + [r]
               new_rout = current_s[1] + [(col, r)]
               new_st = [new_b, new_rout]
               new_pri = Score(new_st)
               heapq.heappush(heap, (new_pri, tie, new_st))
               tie += 1
   print("No solution found by BFS.")
   return False

#PART 1
def solve_dfs(state, closed, depth):
   board = state[0]
   if success(state):
       print("DFS solution (moves):", state[1])
       print_b(board)
       return True


   board_H = tuple(board)
   if board_H in closed:
       return False
   closed.add(board_H)


   col = len(board)
   r = 0
   found = False
   while r < n:
       if is_safe(board, r, col):
           new_B = board + [r]
           new_moves = state[1] + [(col, r)]
           new_ST = [new_B, new_moves]
           if solve_dfs(new_ST, closed, depth + 1):
               found = True
               break
       r += 1
   return found


def run():
   global n
   while(True):
       try:
           n = int(input("Enter board size for N-Queens: "))
       except (ValueError):
           continue


       closed = set()
       init_State = [[], []]
       if not solve_dfs(init_State, closed, 0):
           print("No solution found by DFS.")


       closed2 = set()
       init_state2 = [[], []]
       solve_bfs(init_state2, closed2)


run()
