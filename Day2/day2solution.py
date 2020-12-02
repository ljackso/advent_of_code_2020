"""
--- Day 2: Password Philosophy ---
Question 1)
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was 500.

Question 2)

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

Your puzzle answer was 313.

"""

def main():
	input_list = get_input_list("day2_Q1_input.txt")
	
	valid_password_count_p1 = 0
	valid_password_count_p2 = 0

	for entry in input_list:
		letter = get_password_letter_requirement(entry)
		(min_app, max_app) = get_password_apperance_requirement(entry)
		password = get_password(entry)

		if is_password_valid_part_one(letter, min_app, max_app, password): valid_password_count_p1 += 1
		if is_password_valid_part_two(letter, min_app, max_app, password): valid_password_count_p2 += 1

	print('Number of valid passwords part 1 : ' + str(valid_password_count_p1))
	print('Number of valid passwords part 2 : ' + str(valid_password_count_p2))


def is_password_valid_part_two(letter, min, max, password):
	return (password[min-1] == letter) ^ (password[max-1] == letter)

def is_password_valid_part_one(letter, min, max, password):
	apperance = password.count(letter)
	return apperance >= min and apperance <= max 

def get_password_letter_requirement(entry):
	return entry.split()[1][0]

def get_password_apperance_requirement(entry):
	app_req = entry.split()[0].split('-')
	return (int(app_req[0]), int(app_req[1]))

def get_password(entry):
	return entry.split()[2]

def get_input_list(fileName):
	file = open(fileName, "r")

	input_list = []
	for line in file:
		input_list.append(str(line))

	return input_list

if __name__ == "__main__":
    main()
