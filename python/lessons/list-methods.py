# Insert
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]

front_display_list.insert(0, 'Pineapple')
# print(front_display_list)

# Pop
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]

data_science_topics.pop()
data_science_topics.pop(3)
# print(data_science_topics)

# Range
number_list = range(9)
zero_to_seven = range(8)
# print(list(zero_to_seven))

range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)
# print(list(range_diff_five))

# length
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

long_list_len = len(long_list)

big_range_length = len(big_range)
# print(big_range_length)

# slicing lists
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
middle = suitcase[2:4]

last_two_elements = suitcase[-2:]
slice_off_last_three = suitcase[:-3]
# print(slice_off_last_three)

# counting
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count('Jake')
# print(jake_votes)