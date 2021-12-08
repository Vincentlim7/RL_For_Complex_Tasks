import random
from Agent import Agent
from Enemy import Enemy
class Environment :

    def __init__(self):

        self.length_grid = 25
        self.grid = []

        self.obstacle_positions_list = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0,5), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (1,0), (1,24), (2,0), (2,3), (2,4), (2,8 ), (2,9 ), (2,11 ), (2,12 ), (2,13 ),
            (2,15 ), (2,16 ), (2,20), (2,21 ), (2,24 ), (3,0 ), (3,2 ), (3,3 ), (3,4 ), (3,8 ), (3,9 ), (3,11 ), (3,13 ), (3,15 ), (3,16 ), (3,20 ), (3,21 ), (3,22 ), (3,24 ), (4,0 ), (4,2 ),
            (4,3 ), (4,4 ), (4,20 ), (4,21 ), (4,22 ), (4,24 ), (5,0 ), (5,24), (8,2 ), (8,3 ), (8,8 ), (8,9 ), (8,10 ), (8,11 ), (8,13 ), (8,14 ), (8,15 ), (8,16 ), (8,21 ), (8,22 ), (9,2 ),
            (9,3 ), (9,8 ), (9,9 ), (9,10 ), (9,14 ), (9,15 ), (9,16 ), (9,21 ), (9,22 ), (10,8 ), (10,9 ), (10,15 ), (10,16), (11,2 ), (11,3 ), (11,8 ), (11,16 ), (11,21 ), (11,22 ), (12,2 ),
            (12,12 ), (12,22 ), (13,2 ), (13,3 ), (13,8 ), (13,16 ), (13,21 ), (13,22 ), (14,8 ), (14,9 ), (14,15 ), (14,16 ), (15,2 ), (15,3 ), (15,8 ), (15,9), (15,10 ), (15,14 ), (15,15 ),
            (15,16 ), (15,21 ), (15,22 ), (16,2 ), (16,3 ), (16,8 ), (16,9 ), (16,10 ), (16,11 ), (16,13 ), (16,14 ), (16,15 ), (16,16 ), (16,21 ), (16,22 ), (19,0 ), (19,24), (20,0 ), (20,2 ),
            (20,3 ), (20,4 ), (20,20 ), (20,21 ), (20,22 ), (20,24 ), (21,0 ), (21,2 ), (21,3 ), (21,4 ), (21,8 ), (21,9 ), (21,11 ), (21,13 ), (21,15 ), (21,16 ), (21,20 ), (21,21 ), (21,22 ),
            (21,24), (22, 0), (22, 3), (22, 4), (22, 8), (22, 9), (22, 11), (22, 12), (22, 13), (22, 15), (22, 16), (22, 20 ), (22, 21), (22, 24 ), (23,0 ), (23,24), (24, 0), (24, 1), (24, 2),
            (24, 3), (24, 4), (24, 5), (24, 19), (24, 20), (24, 21), (24, 22), (24, 23), (24, 24)]

        self.number_of_enemies = 1
        self.enemies_list = []
        # self.enemy_positions_list = [(1, 12), (6, 6), (6, 12), (6, 18)]
        self.enemy_positions_list = [(17, 15)]
        self.number_of_foods = 15
        self.food_location = []
        self.food_symbol = "$"

        self.agent = Agent()

    def initialize_grid(self):
        self.grid = []

        # Create empty 25*25 grid
        for i in range(self.length_grid):
            self.grid.append([])
            for j in range(self.length_grid):
                self.grid[i].append(" ")

        # Add agent
        self.grid[18][12] = self.agent.get_symbol()
        self.agent.set_position((18, 12))

        # Add enemies
        for id in range(self.number_of_enemies):
            self.enemies_list.append(Enemy(id+1))

        for i in range(self.number_of_enemies):
            pos = self.enemy_positions_list[i]
            self.enemies_list[i].set_position(pos)
            self.grid[pos[0]][pos[1]] = self.enemies_list[i].get_symbol()

        # Add obstacles
        for o in self.obstacle_positions_list:
            self.grid[o[0]][o[1]] = 'O'

        # Add food
        empty_cells = self.get_list_empty_cells()
        for i in range (self.number_of_foods):
            pos = empty_cells.pop(random.randrange(len(empty_cells)))
            self.food_location.append(pos)
            self.grid[pos[0]][pos[1]] = self.food_symbol

    def get_list_empty_cells(self):
        """
        Compute the list of empty cells

        Returns:
            List<Tuple>: List of empty cells coordinates
        """
        empty_cells = []
        for i in range(len(self.grid[0])):
            for j in range(len(self.grid[1])):
                if self.grid[i][j] == " ":
                    empty_cells.append((i,j))
        return empty_cells

    def move(self, action: str, individual):
        
        if type(individual) == Enemy and action == "Stay":
            return

        elif type(individual) == Agent:
            individual.set_energy(individual.get_energy() - 1)
        
        pos_x, pos_y = individual.get_position()
        if action == "North":
            if pos_x == 0 or self.grid[pos_x - 1][pos_y] == "O":
                print("Mouvement impossible : Obstacle présent ou sortie de grille")
            else:
                self.grid[pos_x][pos_y] = " "
                individual.set_position((pos_x - 1, pos_y))
                self.grid[pos_x -1][pos_y] = individual.get_symbol()
        elif action == "South":
            if pos_x == 24 or self.grid[pos_x + 1][pos_y] == "O":
                print("Mouvement impossible : Obstacle présent ou sortie de grille")
            else:
                self.grid[pos_x][pos_y] = " "
                individual.set_position((pos_x + 1, pos_y))
                self.grid[pos_x + 1][pos_y] = individual.get_symbol()
        elif action == "East":
            if pos_y == 24 or self.grid[pos_x][pos_y + 1] == "O":
                print("Mouvement impossible : Obstacle présent ou sortie de grille")
            else:
                self.grid[pos_x][pos_y] = " "
                individual.set_position((pos_x, pos_y + 1))
                self.grid[pos_x][pos_y + 1] = individual.get_symbol()
        elif action == "West":
            if pos_y == 0 or self.grid[pos_x][pos_y - 1] == "O":
                print("Mouvement impossible : Obstacle présent ou sortie de grille")
            else:
                self.grid[pos_x][pos_y] = " "
                individual.set_position((pos_x, pos_y - 1))
                self.grid[pos_x][pos_y - 1] = individual.get_symbol()
        else:
            print("XXXXX ERROR MOVE() XXXXXX")

    def run(self):
        self.initialize_grid()
        action_list = self.agent.get_action_list()
        print("Deplacement avec les touches ZQSD, C pour quitter")
        while(True):
            print("----------------------------")
            print('\n'.join(''.join(str(x) for x in row) for row in self.grid))
            action = input("Enter a name: ")
            if(action == "c"):
                break
            elif(action == "z"):
                self.move(action_list[0], self.agent)
            elif(action == "s"):
                self.move(action_list[1], self.agent)
            elif(action == "d"):
                self.move(action_list[2], self.agent)
            elif(action == "q"):
                self.move(action_list[3], self.agent)

            for enemy in self.enemies_list:
                action = enemy.next_action(self.agent.get_position(), self.get_surroundings(enemy))
                self.move(action, enemy)


    def get_surroundings(self, enemy: Enemy):
        """
        Compute the observation of the enemy on its 4 adjacent cells

        Args:
            enemy (Enemy): the enemy whose surrounding we are computing

        Returns:
            List<String>: Content of adjacent cells in following order : North, South, East, West
        """
        pos_x, pos_y = enemy.get_position()
        if pos_x == 0:
            north = "O"
        else:
            north = self.grid[pos_x - 1][pos_y]
        if pos_x == 24:
            south = "O"
        else:
            south = self.grid[pos_x + 1][pos_y]
        if pos_y == 24:
            east = "O"
        else:
            east = self.grid[pos_x][pos_y + 1]
        if pos_y == 0:
            west = "O"
        else:
            west = self.grid[pos_x][pos_y - 1]

        return [north, south, east, west]

if __name__ == "__main__":

    env = Environment()
    env.run()