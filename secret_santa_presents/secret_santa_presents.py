

# secret santa friends and presents
import random

def allocate_presents(friends, presents):
    """
    Randomly allocates presents to friends.
    Assumes that the number of friends and presents are equal.
    """
    if len(friends) != len(presents):
        raise ValueError("The number of friends and presents must be equal.")

    # Shuffle the presents list
    random.shuffle(presents)

    # Assign presents to friends
    allocations = {friends[i]: presents[i] for i in range(len(friends))}
    
    return allocations

# Example usage
friends = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
funny_presents = ['Rubber Chicken', 'Whoopie Cushion', 'Ugly Sweater', 'Novelty Mug', 'Funny Hat', 'Toilet Golf Game']

allocations = allocate_presents(friends, funny_presents)
for friend, present in allocations.items():
    print(f"{friend} gets a {present}")
