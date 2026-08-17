from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    messages: list[str]


def node(state: State):
    return {
        "messages": state["messages"] + ["Node executed"]
    }


builder = StateGraph(State)

builder.add_node("node", node)
builder.add_edge(START, "node")
builder.add_edge("node", END)

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


# Create checkpoints
graph.invoke({"messages": ["Hello"]}, config)


# Get checkpoint history
history = list(graph.get_state_history(config))

for i, checkpoint in enumerate(history):
    print(f"Checkpoint {i}: {checkpoint.values}")


# Go back to an old checkpoint
past_config = history[-1].config

# Update that old state
graph.update_state(
    past_config,
    {
        "messages": ["Different approach"]
    }
)

# Run again from that state
result = graph.invoke(None, past_config)

print("New result:", result)

"""
output will be : 
Checkpoint 0: {'messages': ['Hello', 'Node executed']}
Checkpoint 1: {'messages': ['Hello']}
Checkpoint 2: {}
New result: {'messages': ['Hello', 'Node executed']}
"""