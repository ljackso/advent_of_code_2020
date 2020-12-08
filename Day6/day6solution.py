

'''
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Your puzzle answer was 6947.

--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
'''


def main():
	input_list = get_input_list('day6_input.txt')

	groups_str_list = get_groups_str_list(input_list)
	sum_count_p1 = 0
	for group in groups_str_list:
		sum_count_p1 += count_unique_chars(group)

	print('Part 1 : ' + str(sum_count_p1))

	groups_list = get_groups_list(input_list)
	sum_count_p2 = 0
	for group in groups_list:
		sum_count_p2 += count_matching_chars(group)

	print('Part 2 : ' + str(sum_count_p2))

def count_matching_chars(group):
	group_str = ''.join(group)
	occurence_dict = dict((l, group_str.count(l)) for l in set(group_str))
	return len({k:v for (k,v) in occurence_dict.items() if v == len(group)})

def count_unique_chars(group_str):
	return len(set(group_str))

def get_groups_list(input_list):
	group_str = []
	groups = [[]]
	for line in input_list:
		if line == '\n': 
			groups.append(group_str)
			group_str = []
		else:
			group_str.append(line[:-1])
	return groups

def get_groups_str_list(input_list):
	group_str = ''
	groups = []
	for line in input_list:
		if line == '\n': 
			groups.append(group_str)
			group_str = ''
		else:
			group_str += (line[:-1])

	return groups

def get_input_list(fileName):
	file = open(fileName, "r")

	input_list = []
	for line in file:
		input_list.append(str(line))

	return input_list

if __name__ == "__main__":
    main()

