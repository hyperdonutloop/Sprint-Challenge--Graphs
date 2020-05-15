from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# Write an algorithm that picks a random unexplored direction from the player's current room, 
# travels and logs that direction, 
# then loops TRY RECURSIVE SOLUTION
# This should cause your player to walk a DFT. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

# UPER 

# step 1 -  I need to record a traversal path, and the paths I've already taken
# step 2 - Need to get the current room I am in, including the exits
# Step 3 - traverse, starting at current room
# Step 4 - go to each room, record it as visited, then bakctrack somehow? Reverse direction
# Step 5 - function should keep running until all rooms have been visited

traversal_path = []
reverse_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

def graph_traversal(starting_room, visited=set()):
    # records all directions/paths
    path_taken = []

    # get all possible exits in current_room
    # for every direction in the room that the player is currently in
    # player.current_room.get_exits()

    for direction in player.current_room.get_exits():
        # player travels to room in direction of exit
        # player.current_room.travel  -- THIS IS NOT WORKING

        player.travel(direction)
        # check if new room has been visited
        if player.current_room.id not in visited:
            # room has not been visited
            # then we need to mark it as visited
            visited.add(player.current_room.id)
            # add new direction to path_taken
            #path_taken.append[direction] - some error here??
            path_taken.append(direction)
            # RECURSE with new current_room and add to path_taken
            #  (this starts the function again with the room that you are currently in)
            path_taken = path_taken + graph_traversal(player.current_room.id, visited)
            #backtrack and then go to different room
            # reverse direction with whatever direction I am currently going
            # player.travel.reverse_direction
            player.travel(reverse_direction[direction])
            # add backtrack to path_taken to keep track of steps
            path_taken.append(reverse_direction[direction])
        else: 
            # this would mean the room is already visited backtrack and go to a different room
            player.travel(reverse_direction[direction])
        
    return path_taken

traversal_path = graph_traversal(player.current_room.id)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
