import tkinter as tk
import subprocess, os, time

# # # # # # # # # # # #

ROOT_WIDTH = 600
ROOT_HEIGHT = 400

ROOT_PADDING_X = 20
ROOT_PADDING_Y = 20

# # # # # # # # # # # #


# # # # # # # # # # # #

root = tk.Tk()
# root.geometry(ROOT_WIDTH + "x" + ROOT_HEIGHT)

# # # # # # # # # # # #


# # # # # # # # # # # #

files = os.listdir("./algos")

algorithms = [i[:-3] for i in files]

# # # # # # # # # # # #


# # # # # # # # # # # #

form_container = tk.Frame(root)
form_container.pack(side=tk.LEFT, padx=ROOT_PADDING_X, pady=ROOT_PADDING_Y)

listbox = tk.Listbox(
	form_container,
	width= 35,
	height = 15,
	selectmode = "multiple",
)
for i in range(len(algorithms)):
	listbox.insert(tk.END, algorithms[i])
	listbox.itemconfig(
		i,
		bg = "lightgray" if i % 2 == 0 else "white"
	)
listbox.pack(side=tk.TOP)

submit_container = tk.Frame(form_container)
submit_container.pack(side=tk.BOTTOM, padx=20, pady=20)

text_input = tk.Text(
	form_container,
	width=18,
	height=1
)
text_input.pack(side=tk.LEFT)

# # # # # # # # # # # #


# # # # # # # # # # # #
grille_container = tk.Frame(root)
grille_container.pack(side=tk.RIGHT, padx=ROOT_PADDING_X, pady=ROOT_PADDING_Y)
grille = [list() for _ in range(len(algorithms)+1)]

CELL_HEIGHT = 2
CELL_WIDTH_0 = 30
CELL_WIDTH_1 = 20
CELL_WIDTH_2 = 50

grille[0].append(tk.Label(
	grille_container,
	bg="lightgray",
	text="Algorithm",
	borderwidth=1,
	relief="solid",
	width=CELL_WIDTH_0,
	height=CELL_HEIGHT
))
grille[0][-1].grid(
	row=0,
	column=0
)
grille[0].append(tk.Label(
	grille_container,
	bg="lightgray",
	text="Result",
	borderwidth=1,
	relief="solid",
	width=CELL_WIDTH_1,
	height=CELL_HEIGHT
))
grille[0][-1].grid(
	row=0,
	column=1
)
grille[0].append(tk.Label(
	grille_container,
	bg="lightgray",
	text="Execution time",
	borderwidth=1,
	relief="solid",
	width=CELL_WIDTH_2,
	height=CELL_HEIGHT
))
grille[0][-1].grid(
	row=0,
	column=2
)

for i in range(1, len(grille)):
	grille[i].append(tk.Label(
		grille_container,
		bg="white" if i%2 else "lightgray",
		borderwidth=1,
		relief="solid",
		width=CELL_WIDTH_0,
		height=CELL_HEIGHT
	))
	grille[i][-1].grid(
		row = i+1,
		column = 0
	)
	grille[i].append(tk.Label(
		grille_container,
		bg="white" if i%2 else "lightgray",
		borderwidth=1,
		relief="solid",
		width=CELL_WIDTH_1,
		height=CELL_HEIGHT
	))
	grille[i][-1].grid(
		row = i+1,
		column = 1
	)
	grille[i].append(tk.Label(
		grille_container,
		bg="white" if i%2 else "lightgray",
		borderwidth=1,
		relief="solid",
		width=CELL_WIDTH_2,
		height=CELL_HEIGHT
	))
	grille[i][-1].grid(
		row = i+1,
		column = 2
	)

def grille_filler(grille_algo=None):
	for i in range(1, len(grille)):
		grille[i][0].config(text="")
		grille[i][1].config(text="")
		grille[i][2].config(text="")
	if grille_algo is not None:
		for i in range(len(grille_algo)):
			grille[i+1][0].config(text=grille_algo[i][0])
			grille[i+1][1].config(text=grille_algo[i][1])
			grille[i+1][2].config(text=grille_algo[i][2])
grille_filler()

# # # # # # # # # # # #


# # # # # # # # # # # #

def calculate():
	global listbox, text_input
	value = text_input.get("1.0",'end-1c')
	selected_algo = [listbox.get(idx) for idx in listbox.curselection()]

	results = list()
	for file in selected_algo:
		time_start = time.time()
		result = subprocess.run(
			["py", "./algos/{}.py".format(file)],
			input=value,
			capture_output=True,
			check=True,
			text=True
		)
		time_end = time.time()
		results.append((
			file,
			result.stdout,
			time_end - time_start
		))

	grille_filler(results)

tk.Button(
	form_container,
	text="Calculate",
	command=calculate
).pack(side=tk.RIGHT)

# # # # # # # # # # # #




root.mainloop()