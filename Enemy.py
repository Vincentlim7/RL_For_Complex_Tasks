import random
import math

class Enemy :

    def __init__(self, id: int):
        self.id = id
        self.symbol = "E"
        self.action_list = ["North", "South", "East", "West"]
        self.position = None
        
        
    def get_id(self):
        return self.id
    
    def get_symbole(self):
        return self.symbole
        
    def set_position(self, new_position: tuple):
        self.position = new_position
        
    def get_position(self):
        return self.position
        
    def next_action(self, agent_position: tuple, surroundings: list):
        """
        Return the next action of the enemy, as defined by Appendix A of the paper

        Args:
            agent_position (tuple): Current position of the agent
            surroundings (list): [description]

        Returns:
            String: Next action of the enemy
        """

        # The enemy will not move with a 20% chance
        if random.random() < 0.2:
            print("Enemy ", self.id, " at ", self.position, " : Stay")
            return "Stay"

        # Probability of moving in a direction [p_north, p_south, p_east_, p_west]
        prob_action_list = [0, 0, 0, 0]

        angle_list = self.compute_angles(agent_position)

        for i in range(len(surroundings)):
            # Ignore adjacent cells containing an obstacle
            if surroundings[i] == "0":
                continue
            w_angle = (180 - abs(angle_list[i])) / 180

            # Compute Manhattan distance
            dist = abs(agent_position[0] - self.position[0]) + abs(agent_position[1] - self.position[1])

            if dist <= 4:
                t_dist = 15 - dist
            elif dist <=15:
                t_dist = 9 - (dist / 2)
            else:
                t_dist = 1
            
            prob_action_list[i] = math.exp(0.33 * w_angle * t_dist)

        sum_proba = sum(prob_action_list)
        prob_action_list = [proba_i / sum_proba for proba_i in prob_action_list]
        sorted_prob_action_list = sort(prob_action_list)
        draw = random.random
        for i in range(len(sorted_prob_action_list)):
            if draw < sorted_prob_action_list[i]:
                return self.action_list[prob_action_list.index(sorted_prob_action_list[i])]
        
        print("XXXXX Should not happen XXXXX")


    def compute_angles(self, agent_position: tuple):
        """
        Compute the angle between the direction of each action A_i, and the direction
        from the enemy to the agent

        Args:
            agent_position (tuple): Current position of the agent

        Returns:
            Integer list: [a_north, a_south, a_east, a_west]
        """

        x = agent_position[0]
        y = agent_position[1]
        
        if agent_position[0] < self.position[0]: # Agent is above
            if agent_position[1] < self.position[1]: # Agent is in the top left corner
                return
            elif agent_position[1] == self.position[1]: # Agent is in the same column
                return [0, 180, 90, 90]
            elif agent_position[1] > self.position[1]: # Agent is in the top right corner
                return

        if agent_position[0] == self.position[0]: # Agent is on the same line
            if agent_position[1] < self.position[1]: # Agent is on the left
                return [90, 90, 180, 0]
            elif agent_position[1] == self.position[1]:
                print("XXXXX Agent and enemy in same cell, should not happen")
            else: # Agent on the right
                return [90, 90, 0, 180]

        elif agent_position[0] > self.position[0]: # Agent is below
            if agent_position[1] < self.position[1]: # Agent is in the bottom left corner
                return
            elif agent_position[1] == self.position[1]: # Agent is in the same column
                return [180, 0, 90, 90]
            elif agent_position[1] > self.position[1]: # Agent is in the bottom right corner
                return

