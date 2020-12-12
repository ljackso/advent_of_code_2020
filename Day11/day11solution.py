


def main():
	seating_chart = get_input_list('day11_input.txt')

	model_count = 0
	is_stable = False
	prev_chart = list(map(list, seating_chart))
	while is_stable == False:
		model_count += 1
		new_chart = list(map(list, model_seating(prev_chart)))
		is_stable = check_match(new_chart,prev_chart)
		prev_chart = list(map(list, new_chart))

	print(model_count)
	print(get_occupied_seats(prev_chart))

def get_occupied_seats(chart):
	count = 0
	for i in range(0,len(chart)):
		count += chart[i].count('#')
	return count

def check_match(chart1, chart2):
	for i in range(0,len(chart1)):
		for j in range(0,len(chart1[0])):
			if chart1[i][j] != chart2[i][j]:
				return False
	return True

def print_chart(chart):
	for row in chart:
		print(row)
	print('')

def model_seating(og_chart):
	new_chart = list(map(list, og_chart))
	for i in range(0,len(og_chart)):
		for j in range(0,len(og_chart[0])):
			if og_chart[i][j] != '.':
				occ = visible_seats_adjacent(i,j,og_chart)
				if og_chart[i][j] == 'L':
					if occ == 0 : new_chart[i][j] = '#'
				if og_chart[i][j] == '#':
					if occ >= 5 : new_chart[i][j] = 'L'
	return new_chart

def is_occ_seats_direction(y,x,y_i,x_i,chart):
	y += y_i
	x += x_i
	while y >= 0 and x >= 0 and y < len(chart) and x <len(chart[0]):
		if chart[y][x] == '#' : return True
		if chart[y][x] == 'L' : return False
		y += y_i
		x += x_i
	return False

def visible_seats_adjacent(y,x,chart):
	occ_count = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if (i,j) != (0,0):
				if is_occ_seats_direction(y,x,i,j,chart): occ_count += 1
	return occ_count

def seats_adjacent(y,x,chart):
	occ_count = 0
	for i in range(y-1,y+2):
		for j in range(x-1,x+2):
			if (i,j) != (y,x) and i >= 0 and j >= 0 and i < len(chart) and j <len(chart[0]):
				if chart[i][j] == '#' : occ_count += 1
				if chart[i][j] == 'L' : empt_count += 1
	return occ_count

def get_input_list(fileName):
	file = open(fileName, "r")
	input_list = []
	for line in file:
		char_list = []
		for char in line:
			if char != '\n': char_list.append(char)	
		input_list.append(char_list)
	return input_list

if __name__ == "__main__":
    main()