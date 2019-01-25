from tkinter import *
from functools import partial
from random import randint
from tkinter import messagebox


def button_text_changer(val, buttons):
    '''Changes text of buttons'''

    buttons[val].config(text = str(int(buttons[val].config('text')[-1]) ^ 1)) # Change the text of the button pressed to 0 if it was 1 and 1 if it was 0

    # Change text of adjacent buttons
    if val == 0:
        buttons[1].config(text = str(int(buttons[1].config('text')[-1]) ^ 1))
        buttons[3].config(text = str(int(buttons[3].config('text')[-1]) ^ 1))
        chk_win(buttons)
        
    if val == 1:
        buttons[0].config(text = str(int(buttons[0].config('text')[-1]) ^ 1))
        buttons[2].config(text = str(int(buttons[2].config('text')[-1]) ^ 1))       
        buttons[4].config(text = str(int(buttons[4].config('text')[-1]) ^ 1))
        chk_win(buttons)
    if val == 2:
        buttons[1].config(text = str(int(buttons[1].config('text')[-1]) ^ 1))    
        buttons[5].config(text = str(int(buttons[5].config('text')[-1]) ^ 1))
        chk_win(buttons)
        
    if val == 3:
        buttons[0].config(text = str(int(buttons[0].config('text')[-1]) ^ 1))    
        buttons[4].config(text = str(int(buttons[4].config('text')[-1]) ^ 1))
        buttons[6].config(text = str(int(buttons[6].config('text')[-1]) ^ 1))
        chk_win(buttons)
 
    if val == 4:     
        buttons[1].config(text = str(int(buttons[1].config('text')[-1]) ^ 1))      
        buttons[3].config(text = str(int(buttons[3].config('text')[-1]) ^ 1))
        buttons[5].config(text = str(int(buttons[5].config('text')[-1]) ^ 1))     
        buttons[7].config(text = str(int(buttons[7].config('text')[-1]) ^ 1))
        chk_win(buttons)
      
    if val == 5:    
        buttons[2].config(text = str(int(buttons[2].config('text')[-1]) ^ 1))
        buttons[4].config(text = str(int(buttons[4].config('text')[-1]) ^ 1))      
        buttons[8].config(text = str(int(buttons[8].config('text')[-1]) ^ 1))
        chk_win(buttons)
        
    if val == 6:
        buttons[3].config(text = str(int(buttons[3].config('text')[-1]) ^ 1))     
        buttons[7].config(text = str(int(buttons[7].config('text')[-1]) ^ 1))
        chk_win(buttons)
        
    if val == 7:      
        buttons[4].config(text = str(int(buttons[4].config('text')[-1]) ^ 1))    
        buttons[6].config(text = str(int(buttons[6].config('text')[-1]) ^ 1))
        buttons[8].config(text = str(int(buttons[7].config('text')[-1]) ^ 1))
        chk_win(buttons)
        
    if val == 8:  
        buttons[5].config(text = str(int(buttons[5].config('text')[-1]) ^ 1))
        buttons[7].config(text = str(int(buttons[7].config('text')[-1]) ^ 1))
        chk_win(buttons)


def chk_win(buttons):
     if (int(buttons[0].config('text')[-1]) ^ 1)==1 and (int(buttons[1].config('text')[-1]) ^ 1)==1 and (int(buttons[2].config('text')[-1]) ^ 1)==1 and (int(buttons[3].config('text')[-1]) ^ 1)==1 and (int(buttons[4].config('text')[-1]) ^ 1)==1 and (int(buttons[5].config('text')[-1]) ^ 1)==1  and (int(buttons[6].config('text')[-1]) ^ 1)==1 and (int(buttons[7].config('text')[-1]) ^ 1)==1 and (int(buttons[8].config('text')[-1]) ^ 1)==1 :  
          messagebox.showinfo("LIGHTSOUT","Congradulation!.. You won The Game")
def get_rand_list():
    #Returns a list of size 9 with zeros and ones which are randomly chosen

    rand_list = []

    for i in range(9):
        if randint(0, 1) == 0:
            rand_list.append(0)
        else:
            rand_list.append(1)

    # Checking if all lights are off
    all_lights_off = True
    for i in range(9):
        if rand_list[i] == 1:
            all_lights_off = False

    if all_lights_off:
        rand_list = get_rand_list() # Generate random list once again
    else:
        return rand_list

def add_Buttons(root, rand_list):
    '''Add buttons to root(first argument), with their text corresponding to the values in the list provided(second argument)'''

    row = 0
    buttons = []

    for i in range(9):

        if i != 0 and i % 3 == 0:
            row += 1

        button = Button(root, text = rand_list[i], font = ('arial', 25, 'bold'))
        button.grid(row = row, column = i % 3)

        buttons.append(button)

    for i in range(9):
        buttons[i].config(command = partial(button_text_changer, i, buttons))

def start_game():
    '''Starts the Lights Off game'''

    root = Tk()
  
    add_Buttons(root, get_rand_list())

    root.mainloop()


if __name__ == '__main__':
    start_game()
