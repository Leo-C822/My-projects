#resolution: 1280x720
from tkinter import *
from tkinter import messagebox
import random


window = Tk()

# Creating Leaderboard
def leaderboard():
	lb = Toplevel(window)
	lb.geometry("700x650")
	lb.title("Leaderboard")
	canvas = Canvas(lb, width = 700, height = 650, bg = "green")
	canvas.pack()
	upper_perimeter = canvas.create_line(80, 80, 600,80, fill = "yellow")
	left_perimeter = canvas.create_line(80,80, 80, 580, fill = "yellow")
	right_perimeter = canvas.create_line(600,80, 600, 580, fill = "yellow")
	bottom_perimeter = canvas.create_line(80,580, 600, 580, fill = "yellow")
	column1 = canvas.create_line(190,80, 190, 580, fill = "yellow")
	column2 = canvas.create_line(420,80, 420, 580, fill = "yellow")
	row1 = canvas.create_line(80, 180, 600,180, fill = "yellow")
	row2 = canvas.create_line(80, 280, 600,280, fill = "yellow")
	row3 = canvas.create_line(80, 380, 600,380, fill = "yellow")
	row4 = canvas.create_line(80, 480, 600,480, fill = "yellow")
	rank1 = canvas.create_text(135, 130, text = "1", fill = "black", font = ("Helvetica Bold", 20))
	rank2 = canvas.create_text(135, 230, text = "2", fill = "black", font = ("Helvetica Bold", 20))
	rank3 = canvas.create_text(135, 330, text = "3", fill = "black", font = ("Helvetica Bold", 20))
	rank4 = canvas.create_text(135, 430, text = "4", fill = "black", font = ("Helvetica Bold", 20))
	rank5 = canvas.create_text(135, 530, text = "5", fill = "black", font = ("Helvetica Bold", 20))
	x = open("leaderboard_data.txt")
	rank = [tuple(line.split(' ')) for line in x.readlines()]
	rank.sort(key=lambda tup: tup[1])
	i = len(rank) -1
	player_1_name = canvas.create_text(235, 130, text = rank[i][0], fill = "black", font = ("Helvetica Bold",20))
	player_1_score = canvas.create_text(450, 150, text = rank[i][1], fill = "black", font = ("Helvetica Bold",20))
	player_2_name = canvas.create_text(235, 230, text = rank[i-1][0], fill = "black", font = ("Helvetica Bold",20))
	player_2_score = canvas.create_text(450, 250, text = rank[i-1][1], fill = "black", font = ("Helvetica Bold",20))
	player_3_name = canvas.create_text(235, 330, text = rank[i-2][0], fill = "black", font = ("Helvetica Bold",20))
	player_3_score = canvas.create_text(450, 350, text = rank[i-2][1], fill = "black", font = ("Helvetica Bold",20))	
	player_4_name = canvas.create_text(235, 430, text = rank[i-3][0], fill = "black", font = ("Helvetica Bold",20))
	player_4_score = canvas.create_text(450, 450, text = rank[i-3][1], fill = "black", font = ("Helvetica Bold",20))
	player_5_name = canvas.create_text(235, 530, text = rank[i-4][0], fill = "black", font = ("Helvetica Bold",20))
	player_5_score = canvas.create_text(450, 550, text = rank[i-4][1], fill = "black", font = ("Helvetica Bold",20))


# Movement of player ship
def move_left(e):
	global jet_x_coor
	if(pause_state==0 and jet_x_coor >= 10):
		jet_x_coor -= 50
		plane.place(x=jet_x_coor, y = jet_y_coor)
	
		


def move_right(e):
	global jet_x_coor
	if(pause_state == 0 and jet_x_coor <= 1160):
		jet_x_coor += 50
		plane.place(x=jet_x_coor, y=jet_y_coor)
	
		

# Kill switch
def terminate_game():
	global final_score
	final_score = current_score
	window.destroy()



# pause the game
txt= Label(window, text = "The Game is Paused")
def pause_game(e):
	global pause_state
	global pause_count
	if(pause_count % 2 != 0):
		pause_state = 0
		pause_count += 1
		txt.pack_forget()
		save.pack_forget()
		end.pack_forget()

					
	else:
		pause_state = 1
		pause_count += 1
		txt.pack()
		save.pack()
		end.pack()
		# score_time_incr()



# close toplevel page
def close_cheatbox(top): 
	top.destroy()


# When you got hit this happens
def game_over():
	global final_score
	final_score = current_score
	game_count = 1
	plane.place_forget()
	ali1.place_forget()
	ali2.place_forget()
	score.place_forget()
	window.bind("<a>", haha)
	window.bind("<d>",haha)
	well_played = Label(window, image = GGWP)
	well_played.pack()
	window.after(5000, terminate_game)




def close_opt(opt):
	opt.destroy()


# unbinding keys
def haha(e):
	pass
	

# break the fourth wall thingy
def load_game():
	messagebox.showinfo("Commander","Load what? This is a war soldier. You get killed and that's it, no second chance for life")


def save_game():
	messagebox.showinfo("Commander","There is no turning back soldier. You have to defend Earth against the aliens. Fight till you can't!")


# something that is buggy
# def ali1_hit(ali1_x_coor, ali1_y_coor, jet_bullet_x, jet_bullet_y):
# 	global current_score
# 	if((abs(ali1_x_coor - jet_bullet_x) <= 100) and (abs(ali1_y_coor - jet_bullet_y) <= 100)):
# 		ali1.destroy()
# 		current_score += 100
# 		score.config(text = "Score: " + str(current_score))
# 		window.after(3000, ali1_deploy)
# 		print("lol")
# 		window.after(10, lambda:ali1_hit(ali1_x_coor, ali1_y_coor, jet_bullet_x, jet_bullet_y))


# Collision detection for player plane from alien 1
def jet_hit1(ali1_bullet_y, jet_x_coor):
	if(cheat_status == 0):
		x = jet_x_coor - ali1_bullet_x
		if(ali1_bullet_y >= 420 and ali1_bullet_y <= 540 and -100 <= x <= 100):
			game_over()


# Collision detection for player plane form alien 2 (Not called as it breaks the game somehow)	
def jet_hit2(ali2_bullet_y, jet_x_coor):
	if(cheat_status == 0):
		if(ali2_bullet_y >= 490 and ali2_bullet_y <= 540 and  abs(jet_x_coor - ali2_bullet_x <= 40)):
			game_over()



# Make jet bullet travels up
def jet_shot_move():
	global jet_bullet_y
	if(jet_bullet_y >= 20 and pause_state == 0 and game_count ==0):
		jet_bullet_y -= 5
		jet_shot.place(x = jet_bullet_x, y = jet_bullet_y)
		if(jet_bullet_y <= 60):
			jet_shot.place_forget()
	#print(jet_bullet_y)
		window.after(30, jet_shot_move)


# Function for player to shoot 
def shoot(e):
	global jet_bullet_x, jet_bullet_y
	if(pause_state == 0):
		jet_bullet_x = jet_x_coor + 65
		jet_bullet_y = jet_y_coor + 50
		jet_shot.place(x= jet_bullet_x, y = jet_bullet_y)
		jet_shot_move()


# Make bullet from alien 1 move
def ali1_bullet_move():
	global ali1_bullet_y
	if(ali1_bullet_y >= 20 and pause_state == 0 and game_count ==0): # Check if the game is paused 
		ali1_bullet_y += 10  
		ali1_shot.place(x = ali1_bullet_x, y = ali1_bullet_y)
		if(ali1_bullet_y >= 700):
			ali1_shot.place_forget()
		
		jet_hit1(ali1_bullet_y, jet_x_coor)
		window.after(30, ali1_bullet_move) # Call the function again to loop through



# Make bullet from alien 2 move
def ali2_bullet_move():
	global ali2_bullet_y
	if(ali2_bullet_y >= 20 and pause_state == 0 and game_count==0):
		ali2_bullet_y += 10
		ali2_shot.place(x = ali2_bullet_x, y = ali2_bullet_y)
		if(ali2_bullet_y >= 700):
			ali2_shot.place_forget()
		
		#jet_hit2(ali2_bullet_y, jet_x_coor)
		window.after(30, ali2_bullet_move)



# Make alien 1 move randomly and shoot
def ali1_move():
	global ali1_x_coor, ali1_y_coor, ali1_bullet_x, ali1_bullet_y
	ali1_direction = 0
	if(pause_state == 0 and game_count == 0):
		ali1_direction = random.randint(0,3)
		if(ali1_direction == 0):
			ali1_x_coor += 30
			ali1.place(x = ali1_x_coor, y = ali1_y_coor)
			ali1_bullet_x = ali1_x_coor   # Get x and y coordinates to place the bullet
			ali1_bullet_y = ali1_y_coor
			ali1_shot.place(x= ali1_bullet_x, y = ali1_bullet_y)
			ali1_bullet_move()
		elif(ali1_direction == 1):
			ali1_x_coor -= 30
			ali1.place(x = ali1_x_coor, y = ali1_y_coor)
			ali1_bullet_x = ali1_x_coor 
			ali1_bullet_y = ali1_y_coor
			ali1_shot.place(x= ali1_bullet_x, y = ali1_bullet_y)
			ali1_bullet_move()
		elif(ali1_direction == 2):
			ali1_y_coor -= 30
			ali1.place(x = ali1_x_coor, y = ali1_y_coor)
			ali1_bullet_x = ali1_x_coor 
			ali1_bullet_y = ali1_y_coor
			ali1_shot.place(x= ali1_bullet_x, y = ali1_bullet_y)
			ali1_bullet_move()
		elif(ali1_direction == 3):
			ali1_y_coor += 30
			ali1.place(x = ali1_x_coor, y = ali1_y_coor)
			# ali1_bullet_x = ali1_x_coor 
			# ali1_bullet_y = ali1_y_coor
			# ali1_shot.place(x= ali1_bullet_x, y = ali1_bullet_y)
			# ali1_bullet_move()		
	window.after(3000, ali1_move)
	


# Make alien 2 move randomly and shoot
def ali2_move():
	global ali2_x_coor, ali2_y_coor, ali2_bullet_x, ali2_bullet_y
	ali2_direction = 0
	if(pause_state == 0 and game_count ==0):
		ali2_direction = random.randint(0,3)
		if(ali2_direction == 0):
			ali2_x_coor += 30
			ali2.place(x = ali2_x_coor, y = ali2_y_coor)
			ali2_bullet_x = ali2_x_coor 
			ali2_bullet_y = ali2_y_coor
			ali2_shot.place(x= ali2_bullet_x, y = ali2_bullet_y)
			ali2_bullet_move()
		elif(ali2_direction == 1):
			ali2_x_coor -= 30
			ali2.place(x = ali2_x_coor, y = ali2_y_coor)
			ali2_bullet_x = ali2_x_coor 
			ali2_bullet_y = ali2_y_coor
			ali2_shot.place(x= ali2_bullet_x, y = ali2_bullet_y)
			ali2_bullet_move()
		elif(ali2_direction == 2):
			ali2_y_coor -= 30
			ali2.place(x = ali2_x_coor, y = ali2_y_coor)
			ali2_bullet_x = ali1_x_coor 
			ali2_bullet_y = ali1_y_coor
			ali2_shot.place(x= ali1_bullet_x, y = ali1_bullet_y)
			ali2_bullet_move()
		elif(ali2_direction == 3):
			ali2_y_coor += 30
			ali2.place(x = ali2_x_coor, y = ali2_y_coor)
			# ali1_bullet_x = ali1_x_coor 
			# ali1_bullet_y = ali1_y_coor
			# ali1_shot.place(x= ali1_bullet_x, y = ali1_bullet_y)
			# ali1_bullet_move()				
	window.after(3000, ali2_move)


# Makes alien 1 spawn randomly on window
def ali1_deploy():
	global ali1_x_coor, ali1_y_coor
	if(pause_state == 0 and game_count ==0):
		ali1_x_coor = random.randint(150,650)
		ali1_y_coor = random.randint(70,340)
		ali1.place(x = ali1_x_coor, y = ali1_y_coor)
		window.after(2000,ali1_move)

# Alien 2 spawn randomly		
def ali2_deploy():
	global ali2_x_coor, ali2_y_coor
	if(pause_state == 0 and game_count == 0):
		ali2_x_coor = random.randint(150,1100)
		ali2_y_coor = random.randint(70,340)
		ali2.place(x = ali2_x_coor, y = ali2_y_coor)
		ali2_move()


# Boss key (only double clicking 'B' triggers it)
work = PhotoImage(file = "work.png") # Screenshot of my VM
def boss_key(e):
	global boss_count
	if(boss_count % 2 != 0):
		boss_count += 1
		#pause_game(e)
		boss_here = Toplevel(window)
		boss_here.geometry = ("1280x720")
		boss = Label(boss_here, image = work)
		boss_here.title("Work work work")
		boss.pack()			
	else:
		boss_count += 1
		#pause_game(e)
		
		

#control bindings
def confirm_control(x):
	if(x==1):
		window.bind("<Left>",move_left)
		window.bind("<Right>", move_right)
		window.bind("<a>", haha)
		window.bind("<d>",haha)

# increasing score	
def score_time_incr():
	global current_score
	if(pause_state == 0 and game_count ==0):
		current_score += 10
		score.config(text = "Score: " + str(current_score))
		if(cheat_status == 1 and current_score == 120):
			game_over()

	window.after(1000, score_time_incr)


# in-game story line
def story():
	plot= Label(window, text = "They have energy barriers! Your weapon is useless. Try to Sruvive!!")
	plot.pack()
	



# Display instructions in main menu when the red question mark is clicked
def show_score_mech():
	table = Toplevel(window)
	scroll = Scrollbar(table)
	content = Text(table, height = 18, width = 66)
	content.pack()
	math = """        Scoring Mechanism:
	Every second you survive: + 10 points;
	Each alien you bring down: + 100 points;
	(if you can)

	Control:
	1) 'A' to move left and 'D' to move right;
	2) '<-' to move left and '->' to move right;
	3) Press 'P' to pause and 'B' for boss key;

	Life count:
	What life count? this isn't a game soldier. You get hit,
	YOU DIE! 

	Good luck soldier. Glory to menkind

	???: double click 'B' when your boss is near.

	C.K: Don't forget to enter your name first before playing!"""
	content.insert(END, math)

	


# Check if cheat code is correct
def cheat_check(code):  
	global cheat_status 

	if (code == cheatcode):
		messagebox.showinfo("???", "Never gonna give you up, Never gonna let you down. You're powered up, get in there")
		cheat_status = 1
		create_initial_menu()
	
	else:
		messagebox.showinfo("C.K", "Come back when you found the correct code mate")
		cheat_status = 0
		



def close_name_box(name):
	name.destroy()



# Return entered value to global variable palyer_name
def info_pass(player_entry):
	global player_name
	player_name = player_entry


# Store name of player
def player_name_box():
	name= Toplevel(window)
	name.geometry = ("450x200")
	name.title("Your name")
	player_entry = Entry(name, width = 25)
	player_entry.pack()
	send = Button(name, text = "Set", command = lambda:[info_pass(player_entry.get()),close_name_box(name)])
	send.pack()
	



# Cheat code entry box
def cheat_box():   
	top = Toplevel(window)
	top.geometry = ("450x200")
	top.title("???")
	code = Entry(top, width = 25)
	code.pack()
	exe = Button(top, text = "Execute", command = lambda:[cheat_check(code.get()),close_cheatbox(top)])
	exe.pack()
	exit = Button(top, text = "Leave", command = lambda:close_cheatbox(top))
	exit.pack()
	

	
# Main game loop
def start_game():  
	play.place_forget()
	option.place_forget()
	cheat.place_forget()
	explain.place_forget()
	load.place_forget()
	bg_label.place_forget()
	info.place_forget()
	board.place_forget()
	plane.place(x=jet_x_coor, y = jet_y_coor)
	score.place(x = 1050, y = 60)
	if(control_method.get() == 0):
		window.bind("<a>",move_left)
		window.bind("<d>", move_right)
	score_time_incr()
	ali1_deploy()
	window.after(1500, story)
	window.after(10000, ali2_deploy)

	
		
			
		
# Function for changing movement type
def option_menu():   
	opt = Toplevel(window)
	opt.geometry = ("450x200")
	opt.title("Option Menu")
	op1 = Radiobutton(opt, text = "'A' and 'D' control", value = 0,
		font = ("Helvetica", 15), variable = control_method)
	op1.pack()
	op2 = Radiobutton(opt, text = "'<-' and '->' control", value = 1, 
		font = ("Helvetica", 15), variable = control_method)
	op2.pack()
	confirm = Button(opt, text = "Confirm", command = lambda:[confirm_control(control_method.get()),close_opt(opt)])
	confirm.pack()


	
# Function for creating main menu
def create_initial_menu():  
		bg_label.place(x=10,y=5)
		play.place(x = 520, y = 150)
		load.place(x=520, y = 340 )
		option.place(x= 520, y =520)
		cheat.place(x=35, y= 35)
		explain.place(x=1100, y = 35)
		info.place(x=200, y= 450)
		board.place(x=200, y=250)
		if(cheat_status == 1):
			hax.place(x = 1150, y=670)


	
window.title("Space fighter")
window.geometry("1280x720")
window.configure(background = "#000000")
window.resizable(False, False)

# Creating variables, images and buttons for use in functions
background1 = PhotoImage(file = "space_bg.png") # (Volkmer, 2016)
do_not_press = PhotoImage(file = "cheat.png") # (Schludi, 2019)
jet = PhotoImage(file = "jet.png") #I drew this image myself
lol = PhotoImage(file = "hax.png") # (Niu, 2019)
scoring = PhotoImage(file = "ques.png") # (Secci, 2020)
alien1 = PhotoImage(file = "alien.png") #drew it myself
alien2 = PhotoImage(file = "alien_01.png")  #drew it myself
alien3 = PhotoImage(file = "alien_02.png")  #drew it myself
GGWP = PhotoImage(file = "ggwp.png") # (Canva, )
plane_bullet = PhotoImage(file = "jbullet.png")  #my drawing
ali1_bullet = PhotoImage(file = "alien_shot.png") #my drawing
ali2_bullet = PhotoImage(file = "alien_shot.png")
ali3_bullet = PhotoImage(file = "alien_shot.png")


# Creating all of the labels
bg_label = Label(window, image = background1)

hax = Label(window, image=lol)

ali1 = Label(window, image = alien1, bg = "#000000")

ali1_shot = Label(window, image = ali1_bullet, bg = "#000000")

ali2_shot = Label(window, image = ali2_bullet, bg = "#000000")

ali2 = Label(window, image = alien2, bg = '#000000')

ali3 = Label(window, image = alien3)

plane = Label(window, image = jet, bg = "#000000")

jet_shot = Label(window, image = plane_bullet, bg = "#000000")

score = Label(window, fg = "white", text = "Score: 0", font = ("Helvetica", 15), bg = "#000000")


# Creating buttons for main menu
play = Button(window, fg = "white", text = "Start", 
		font = ("Helvetica", 20), background = "#000000", 
		width = 25, height = 5, highlightbackground = "#000000", 
		command = start_game)

info = Button(window, fg = "white", text = "Name here", 
		font = ("Helvetica", 15), background = "#000000", 
		width = 18, height = 6, highlightbackground = "#000000", 
		command = player_name_box)

load = Button(window, fg = "white", text = "Load", 
		font = ("Helvetica", 20), background = "#000000", 
		width = 25, height = 5, highlightbackground = "#000000", 
		command = load_game)

option = Button(window, fg = "white", text = "Options", font = ("Helvetica", 20), 
	background = "#000000", width = 25, height = 5, 
	highlightbackground = "#000000",command = option_menu)

save = Button(window, fg = "white", text = " Save Game", font = ("Helvetica", 10), 
	background = "#000000", width = 10, height = 5, 
	highlightbackground = "#000000",command = save_game)


board = Button(window, fg = "white", text = " Leaderboard", font = ("Helvetica", 20), 
	background = "#000000", width = 10, height = 5, 
	highlightbackground = "#000000",command = leaderboard)


end = Button(window, fg = "white", text = "Exit", font = ("Helvetica", 10), 
	background = "#000000", width = 10, height = 5, 
	highlightbackground = "#000000",command = terminate_game)

cheat = Button(window, image = do_not_press, width = "52", height = "37",
		command = cheat_box)

explain = Button(window, image = scoring, command = show_score_mech)



#Global variables
cheatcode = "MLG pro"
cheat_status = 0
current_score = 0
final_score = 0
control_method = IntVar()
#control_scheme = 0
life_count = 1
jet_x_coor = 570
jet_y_coor = 530
pause_state = 0
pause_count = 0
boss_count = 0
jet_bullet_x = 0
jet_bullet_y = 0
ali1_x_coor = 0
player_name = ""
ali1_y_coor = 0
ali2_x_coor = 0
ali2_y_coor = 0
ali3_x_coor = 0
ali3_y_coor = 0
ali1_bullet_x = 0
ali1_bullet_y = 0
ali2_bullet_x = 0
ali2_bullet_y = 0
ali3_bullet_x = 0
ali3_bullet_y = 0
game_count = 0


# key bindings
window.bind("<p>", pause_game)
window.bind("<b>", boss_key)
window.bind("<j>", shoot)

create_initial_menu()


window.mainloop()

# Storing player name and result to leaderboard file
if(final_score != 0):
	f = open("leaderboard_data.txt", "a")
	f.write(player_name + " " + str(final_score) + "\n")
	f.close()