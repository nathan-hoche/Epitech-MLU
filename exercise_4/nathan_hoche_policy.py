from agent import Agent


CurrentMove = "left"

def nathan_hoche_policy(agent: Agent) -> str:
    """
    Policy of the agent
    return "left", "right", or "none"
    """
    global CurrentMove

    # Move the agent if there is no known reward or if the current score is less than 20
    if (agent.known_rewards.sum() == 0):
        # If the agent is in the first postion, move right
        if (agent.position == 0):
            CurrentMove = "right"
        # If the agent is in the last postion, move left
        elif (agent.position == 7):
            CurrentMove = "left"
        return CurrentMove
    # Stay in the reward position if the agent knows the reward
    return "none"
