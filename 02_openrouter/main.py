# Simulating agent router logic with predefined agents
def route_message(agent_name, message):
    valid_agents = ["agent_1", "agent_2", "agent_3"]
    if agent_name in valid_agents:
        print(f"Routing to {agent_name}: {message}")
    else:
        print(f"Agent '{agent_name}' is not registered.")

if __name__ == "__main__":
    route_message("agent_1", "Hello from the router")
    route_message("agent_4", "Hello unknown agent")
