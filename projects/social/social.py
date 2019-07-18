import random

from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(numUsers):
            self.addUser(user)

        # Create friendships
        friendship_combinations = []
        ## make all possible friendship combintations
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                # if userID != friendID:
                friendship_combinations.append((userID, friendID))
        # print(friendship_combinations)
    
        ## shuffle the friendship combinations
        random.shuffle(friendship_combinations)
        # print(friendship_combinations)
        ## take the N number of friendships
        totalFriendships = avgFriendships * numUsers
        friendships_to_make = friendship_combinations[:( totalFriendships // 2 )]

        for friendship in friendships_to_make:
            first_friend = friendship[0]
            second_friend = friendship[1]
            self.addFriendship(first_friend, second_friend)

        # avgFriendships = totalFriendships / numUsers
        # avgFriendships * numusers = totalFriendships

    # Stretch - Decrease runtime to linear rather than quadratic
    def populateGraphLinear(self, numUsers, avgFriendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for user in range(numUsers):
            self.addUser(user)

        totalFriendships = avgFriendships * numUsers
        friendships_created = 0
        collisions = 0
        
        while friendships_created < totalFriendships:
        # create friendships
            
        # choose two random user ids
            first_friend = random.randint(1, numUsers)
            second_friend = random.randint(1, numUsers)
        # try to make them friends
            maybe_friendship = self.addFriendship(first_friend, second_friend)
        # if that works, increment a friendship counter
            if maybe_friendship == True:
                friendships_created += 1
        # if not increment a collision counter
            else:
                collisions += 1



    # @staticmethod
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Create and empty Queue
        q = Queue()
        # Create an empty visited dictionary
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Add a Path to the starting vertex to the queue
        path = [userID]
        q.enqueue(path)
        # While the queue is not empty...
        while q.size():
            # Dequeue the first PATH
            path = q.dequeue()
            # grab the last vertex fo the path
            v = path[-1]
            # if it has not been visited...
            if v not in visited:
                # mark it as visited (add it to the visited dictionary)
                visited[v] = path # then enqueue paths to each of its neighbors in the queue
                for friend in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print(sg.users)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print('**********************************')
    print(connections)
    print(len(connections) - 1)

    total_steps = 0
    for user_id in connections:
        total_steps += len(connections[user_id])
    
    print('average length of social path: ', total_steps/len(connections))

    sg.populateGraphLinear(10, 2)


