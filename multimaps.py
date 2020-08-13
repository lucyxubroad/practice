# Question: Write a program that takes in a HashMap<String, Integer> and returns a HashMap<Integer,
# HashSet<String>> where the key gives the number of occurences of a word and the value gives the
# set of all words with that number of occurences

# Example:
# Input: {"to": 2, "be": 2, "or": 1, "not": 1, "that": 1, "is": 1, "the": 1, "question": 1}
# Output: {2: {"to", "be"}, 1: {"not", "that", "is", "the", "question"}}

# Step 1: Understand
#
# Input: {"a": 4, "hello": 1, "how": 32, "so": 4, "maybe": 4}
# Output: {4: {"a", "so", "maybe"}, 1: {"hello", 32: "how"}}
#
# Input: {}
# Output: {}
#
# Step 2: Match
# - Need a hashmap to keep track of the number values we've seen in the input
#
# Step 3: Plan
# Create a ans_hashmap that will be returned
# For each key in the hashmap
#   Get value associated with the key
#   If value exists in ans_hashmap,
#       Add key to ans_hashmap[value]
#   Else
#       Create new hashset, add key to hashset, add hashset to ans_hashmap[value]
# Return ans_hashmap

def map_to_collection(hashmap):
    count_to_word_hashmap = {}
    for key, value in hashmap.items():
        if value in count_to_word_hashmap:
            count_to_word_hashmap[value].add(key)
        else:
            word_set = set()
            word_set.add(key)
            count_to_word_hashmap[value] = word_set
    return count_to_word_hashmap

# Step 5: Review
# - With example input {"a": 4, "hello": 1, "how": 32, "so": 4, "maybe": 4},
#   initially, count_to_word_hashmap = {}.
#   - Look at "a", 4, sees that count_to_word_hashmap does not contain 4 so
#     creates a new word_set and adds "a" to it and set at count_to_word_hashmap[4]


if __name__ == "__main__":
    print(map_to_collection(
        {"a": 4, "hello": 1, "how": 32, "so": 4, "maybe": 4}))
    print("Expect: 1: [hello], 4: [am, so, maybe], 32: [how]")

    print(map_to_collection({}))
    print("Expect: empty")

    print(map_to_collection(
        {"a": 4, "hello": 4, "how": 4, "so": 4, "maybe": 4}))
    print("Expect: 4: [a, hello, how, so, maybe]")
