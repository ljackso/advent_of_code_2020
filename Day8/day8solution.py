'''
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

Your puzzle answer was 1744.

--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

Your puzzle answer was 1174.

'''

def main():
	instr_list = get_input_list('day8_input.txt')

	print('Part 1')
	index_history = [0]
	index = 0
	acc_val = 0
	while index_history.count(index) < 2 and index < (len(instr_list)):
		(index, acc_val) = perform_instruction(index, acc_val, instr_list)
		index_history.append(index)
	print(acc_val)


	print('Part 2')
	new_list = get_non_looping(instr_list) 
	index_history = [0]
	index = 0
	acc_val = 0
	while index < (len(new_list)):
		(index, acc_val) = perform_instruction(index, acc_val, new_list)
		index_history.append(index)
	print(acc_val)

#this is awful
def get_non_looping(instr_list):
	for index in range(0, len(instr_list)):
		new_list = instr_list.copy()
		is_loop = True
		if new_list[index][0] == 'nop': 
			new_list[index] = ('jmp', new_list[index][1])
			is_loop = is_a_loop(new_list)
		elif new_list[index][0] == 'jmp': 
			new_list[index] = ('nop', new_list[index][1])
			is_loop = is_a_loop(new_list)
		if is_loop == False:
			#print('Change inst : ' + str(instr_list[index]) + ' at index ' + str(index))
			return new_list

def is_a_loop(input_list):
	index_history = [0]
	index = 0
	acc_val = 0
	while uniform_counts(index_history) == False and index < (len(input_list) - 1):
		(index, acc_val) = perform_instruction(index, acc_val, input_list)
		index_history.append(index)
	return uniform_counts(index_history)

def uniform_counts(in_list):
	return  len(in_list) % len(set(in_list))  == 0 and len(in_list) != len(set(in_list))

def perform_instruction(index, val, instr_list):
	if instr_list[index][0] == 'acc': return ((index + 1), (val + instr_list[index][1])) 
	if instr_list[index][0] == 'nop': return ((index + 1), val) 
	if instr_list[index][0] == 'jmp': return ((index + instr_list[index][1]), val) 
	print('fuck')

def get_input_list(fileName):
	file = open(fileName, "r")
	input_list = []
	for line in file:
		input_list.append((str(line.split()[0]), int(line.split()[1])))
	return input_list

if __name__ == "__main__":
    main()