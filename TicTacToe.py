import tkinter as tk, math

# ---------- Core game logic (mirrors your console code) ----------
def winner(b):
    for i in range(3):
        if b[i][0]==b[i][1]==b[i][2]!=" ": return b[i][0]
        if b[0][i]==b[1][i]==b[2][i]!=" ": return b[0][i]
    if b[0][0]==b[1][1]==b[2][2]!=" ": return b[1][1]
    if b[0][2]==b[1][1]==b[2][0]!=" ": return b[1][1]
    return None

def full(b): return all(c!=" " for r in b for c in r)

def minimax(b, maxm):
    w = winner(b)
    if w=="O": return 1
    if w=="X": return -1
    if full(b): return 0
    scores=[]
    for r in range(3):
        for c in range(3):
            if b[r][c]==" ":
                b[r][c] = "O" if maxm else "X"
                scores.append(minimax(b, not maxm))
                b[r][c] = " "
    return (max(scores) if maxm else min(scores))

def best_move(b):
    best, move = -math.inf, None
    for r in range(3):
        for c in range(3):
            if b[r][c]==" ":
                b[r][c]="O"
                s = minimax(b, False)
                b[r][c]=" "
                if s>best: best, move = s, (r,c)
    return move

def count_outcomes(b, is_ai):
    w = winner(b)
    if w=="O": return (1,0,0)
    if w=="X": return (0,1,0)
    if full(b): return (0,0,1)
    a=h=d=0; pl = "O" if is_ai else "X"
    for r in range(3):
        for c in range(3):
            if b[r][c]==" ":
                b[r][c]=pl
                x,y,z = count_outcomes(b, not is_ai)
                a+=x; h+=y; d+=z
                b[r][c]=" "
    return a,h,d

# ---------- GUI ----------
BG="#0f1220"; GRID="#2a2f4a"; TILE="#1b2036"; XCOL="#f6c177"; OCOL="#9ccfd8"; TXT="#e6eaf4"; ACC="#c4a7e7"

root = tk.Tk()
root.title("Tic-Tac-Toe – Minimax AI")
root.configure(bg=BG)
root.resizable(False, False)

B = [[" "]*3 for _ in range(3)]
buttons = [[None]*3 for _ in range(3)]

# Container with subtle grid lines
board_frame = tk.Frame(root, bg=GRID, bd=0, highlightthickness=0, padx=3, pady=3)
board_frame.grid(row=0, column=0, padx=16, pady=(16,8))

status = tk.StringVar(value="Your turn (X).")
stats  = tk.StringVar(value="Outcomes → AI: 0  You: 0  Draws: 0")

def refresh_outcomes():
    a,h,d = count_outcomes(B, True)
    stats.set(f"Outcomes → AI: {a}  You: {h}  Draws: {d}")

def set_button(but, ch):
    but.config(text=ch, fg=(XCOL if ch=="X" else OCOL), activeforeground=(XCOL if ch=="X" else OCOL))

def game_over_msg():
    w = winner(B)
    return "Draw!" if not w else (f"{'AI (O)' if w=='O' else 'You (X)'} win!")

def disable_board(disabled=True):
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = ("disabled" if disabled else "normal")

def ai_turn():
    if winner(B) or full(B): return
    mv = best_move(B)
    if mv:
        r,c = mv
        B[r][c]="O"; set_button(buttons[r][c], "O")
    end_check()

def end_check():
    if winner(B) or full(B):
        status.set(game_over_msg())
        disable_board(True)
    refresh_outcomes()

def on_click(r,c):
    if B[r][c]!=" " or winner(B): return
    B[r][c]="X"; set_button(buttons[r][c], "X")
    end_check()
    if not (winner(B) or full(B)):
        root.after(120, ai_turn)  # tiny delay for nicer feel

def reset():
    for i in range(3):
        for j in range(3):
            B[i][j]=" "
            b = buttons[i][j]
            b.config(text=" ", state="normal")
    status.set("Your turn (X).")
    refresh_outcomes()

# Build 3x3 buttons with nice look
for i in range(3):
    for j in range(3):
        btn = tk.Button(
            board_frame, text=" ", font=("Helvetica", 28, "bold"),
            width=3, height=1, bg=TILE, fg=TXT, activebackground="#202642",
            relief="flat", bd=0, highlightthickness=0,
            command=lambda r=i, c=j: on_click(r,c)
        )
        btn.grid(row=i, column=j, padx=3, pady=3, sticky="nsew")
        buttons[i][j]=btn

# Info/footer area
info = tk.Frame(root, bg=BG)
info.grid(row=1, column=0, sticky="ew", padx=16, pady=(0,12))
tk.Label(info, textvariable=status, bg=BG, fg=TXT, font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w")
tk.Button(info, text="Reset", command=reset, font=("Helvetica", 12, "bold"),
          bg=ACC, fg="#11131c", bd=0, relief="flat", padx=10, pady=4,
          activebackground=ACC).grid(row=0, column=1, padx=10)
tk.Label(info, textvariable=stats, bg=BG, fg=TXT, font=("Helvetica", 11)).grid(row=1, column=0, columnspan=2, sticky="w", pady=(6,0))

refresh_outcomes()
root.mainloop()

