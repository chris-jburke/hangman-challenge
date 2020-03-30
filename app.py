import random
gallow_start =  """
 ___
|   |
|
|
|
|
- """
gallow_head = """
 ___
|   |
|   O
|
|
|
- """
gallow_neck = """
 ___
|   |
|   O
|   |
|
|
- """
gallow_left_arm = """
 ___
|   |
|   O
|  -|
|
|
- """
gallow_right_arm = """
 ___
|   |
|   O
|  -|-
|
|
- """
gallow_left_leg = """
 ___
|   |
|   O
|  -|-
|   /
|
- """
gallow_right_leg = """
 ___
|   |
|   O
|  -|-
|   /\\
|
- """
gallows=[gallow_start,gallow_head,gallow_neck,gallow_left_arm,gallow_right_arm, gallow_left_leg, gallow_right_leg]
word_list = ['apple', 'pear', 'oranges', 'pineapple', 'zebra', 'alligator', 'people', 'social', 'distance']
rand_num = random.randrange(0,len(word_list) - 1)
curr_word = word_list[rand_num]
curr_list = list(curr_word)
found_list = []
for i in range(0, len(curr_list)):
	found_list.append('_')
print(found_list)
hang_count = 0
index = 0
while(hang_count < len(gallows) and index < len(curr_list)):
	letter = input('Enter a letter\n')
	if(letter in curr_word and letter in curr_list):
		while(letter in curr_word and letter in curr_list):
			letter_index = curr_list.index(letter)
			found_list[letter_index] = letter
			index += 1
			curr_list[letter_index] = '_'
	else:
		print(gallows[hang_count])
		hang_count += 1
	print(found_list)
if(index == len(curr_list) and hang_count < len(gallows)):
	found_string = ''.join(map(str, found_list))
	print("You won! You found the string: " + found_string)




