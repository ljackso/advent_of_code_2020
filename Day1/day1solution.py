
"""
Question 1)

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 927684. 

Question 2) 

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 292093004.
"""

def main():
	input_list = get_input_list("day1_Q1_input.txt")

	print("Question 1")
	(num_one, num_two) = check_for_two_val_sum(input_list, 2020)
	solution = num_one * num_two

	print((num_one, num_two))
	print(solution)

	print("Question 2")
	(num_one, num_two, num_three) = check_for_three_val_sum(input_list, 2020)
	solution = num_one * num_two * num_three

	print((num_one, num_two, num_three))
	print(solution)


def check_for_two_val_sum(list, value): #n^2
	for item_1 in list:
		for item_2 in list:
			if item_1 != item_2:
				if item_2 + item_1 == value:
					return (item_1, item_2)
	return (0,0)

def check_for_three_val_sum(list, value): #n^3
	for item_1 in list:
		for item_2 in list:
			for item_3 in list:
				if item_1 != item_2 and item_1 != item_3 and item_2 != item_3 :
					if item_2 + item_1 +item_3 == value:
						return (item_1, item_2, item_3)
	return (0,0,0)

def get_input_list(fileName):
	file = open(fileName, "r")

	input_list = []
	for line in file:
		input_list.append(int(line))

	return input_list


if __name__ == "__main__":
    main()

 