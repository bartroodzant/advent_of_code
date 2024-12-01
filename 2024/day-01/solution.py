from collections import Counter

# Initialize left and right lists
left_list = []
right_list = []
answer_1 = 0
answer_2 = 0

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # The split function splits the string on whitespace, which splits the left and right lists into 2 separate values
        split_string = line.split()
        left_list.append(int(split_string[0]))
        right_list.append(int(split_string[1]))

# Sort both lists
left_list.sort()
right_list.sort()

# I used the Counter library to create a hashmap of right list which creates a key-value pair of the number and how many
# times it occurs in the list
counted_right_list = Counter(right_list)

# Loop through both lists using the zip function
# I have built in a check to check which number is bigger to make the math easier
for left_number, right_number in zip(left_list, right_list):
    # Code for answer 1
    if left_number <= right_number:
        answer_1 += right_number - left_number
    else:
        answer_1 += left_number - right_number

    # Code for answer 2
    if counted_right_list[left_number]:
        answer_2 += left_number * counted_right_list[left_number]

print(counted_right_list)
print("Answer 1:", answer_1)
print("Answer 2:", answer_2)