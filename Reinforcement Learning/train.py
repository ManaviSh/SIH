import random
import json
import argparse
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from agent import car
from environment import Environment
import numpy as np

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, default='car', help='Which agent to use')
    parser.add_argument('--learning_rate', type=float, default=0.001, help='How quickly the algorithm tries to learn')
    parser.add_argument('--discount', type=float, default=0.97, help='Discount for estimated future action')
    parser.add_argument('--iterations', type=int, default=20000, help='Iteration count')
    FLAGS, unparsed = parser.parse_known_args()

    # call agent
    agent = car(learning_rate=FLAGS.learning_rate, discount=FLAGS.discount, iterations=FLAGS.iterations)


    # setup simulation
    road = Environment()
    road.reset()
    total_reward = 0 # Score keeping
    last_total = 0

    # main loop
    for step in range(FLAGS.iterations):
        old_state = road.rpm # Store current state
        action = agent.get_next_action(old_state) # Query agent for the next action
        new_state, reward = road.take_action(action) # Take action, get new state and reward
        agent.update(old_state, new_state, action, reward) # Let the agent update internals

        total_reward += reward # Keep score
        if step % 1000 == 0: # Print out metadata every 250th iteration
            performance = (total_reward - last_total) / 1000.0
            print(json.dumps({'step': step, 'performance': performance, 'total_reward': total_reward}))
            last_total = total_reward

        time.sleep(0.0001) # Avoid spamming stdout too fast!
    print("Training finished.\n")
    print("Final Q-table", agent.q_table)
    '''
    policy = np.zeros(6)
    for i in range(6):
        policy[i]=np.argmax(agent.q_table[i:])
    print(policy)
    '''

if __name__ == "__main__":
    main()