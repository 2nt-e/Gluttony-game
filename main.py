import time
import keyboard

print("Use usual 'W', 'A', 'S' and 'D' keys to move... \nstarting in 3 seconds...")
time.sleep(3)

timerr = 0
newliness = "\n\n\n\n\n\n\n\n"*5
default_structure = {}
for x in range(10):
    default_structure[x] = {}
    for y in range(10):
        default_structure[x][y] = 0
orignal_str = default_structure
box_pos = [5, 5]
default_structure[box_pos[0]][box_pos[1]] = 1

def print_structure(): 
    print(newliness)
    text = ''
    for x in range(len(default_structure)):
        for y in range(len(default_structure[x])):
            if default_structure[x][y] == 100:
                text = text + "🟩"
            else:
                if default_structure[x][y] == 1:
                    text = text + "🔲"
                elif default_structure[x][y] == 0:
                    text = text + "⬛"
                elif default_structure[x][y] in (9, 8):
                    text = text + "⬜️"
                    default_structure[x][y] -= 1
                elif default_structure[x][y] in (7, 6):
                    default_structure[x][y] -= 1
                    text = text + "🟥"
                elif default_structure[x][y] in (5, 4):
                    default_structure[x][y] -= 1
                    text = text + "🟨"
                elif default_structure[x][y] == 3:
                    default_structure[x][y] = 100
                    text = text + "🟩"
        text = text + '\n'
    print(text, flush=True)

print_structure()
def game_end():
    m_list = []
    for i in range(len(default_structure)):
        for j in range(len(default_structure[i])):
            m_list.append(default_structure[i][j])
    if 0 not in m_list:
        return True
    else: 
        return False

while not game_end():
    if keyboard.is_pressed('s') == True:
        if box_pos[0] < 9:
            default_structure[box_pos[0]][box_pos[1]] = 9
            box_pos[0] += 1
            default_structure[box_pos[0]][box_pos[1]] = 1
            print_structure()
    if keyboard.is_pressed('w') == True:
        if box_pos[0] > 0:
            default_structure[box_pos[0]][box_pos[1]] = 9
            box_pos[0] -= 1
            default_structure[box_pos[0]][box_pos[1]] = 1
            print_structure()
    if keyboard.is_pressed('d') == True:
        if box_pos[1] < 9:
            default_structure[box_pos[0]][box_pos[1]] = 9
            box_pos[1] += 1
            default_structure[box_pos[0]][box_pos[1]] = 1
            print_structure()
    if keyboard.is_pressed('a') == True:
        if box_pos[1] > 0:
            default_structure[box_pos[0]][box_pos[1]] = 9
            box_pos[1] -= 1
            default_structure[box_pos[0]][box_pos[1]] = 1
            print_structure()
    time.sleep(0.05)
    timerr += 0.05

else:
    print(newliness, f"YOU BEAT THE GAME!!! in {timerr} seconds")
    print('closing in 15 seconds...')
    time.sleep(15)
