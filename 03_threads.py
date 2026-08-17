from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    messages: list[str]


def node(state: State):
    return state


builder = StateGraph(State)

builder.add_node("chat", node)
builder.add_edge(START, "chat")
builder.add_edge("chat", END)

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


Prasad = {"configurable": {"thread_id": "Prasad"}}
Pratik = {"configurable": {"thread_id": "Pratik"}}


# Prasad
graph.invoke({"messages": ["Hi!"]}, Prasad)

# Pratik
graph.invoke({"messages": ["Hello!"]}, Pratik)


print("Prasad:", graph.get_state(Prasad).values)
print("Pratik:", graph.get_state(Pratik).values)

""" output will be :
Prasad: {'messages': ['Hi!']}
Pratik: {'messages': ['Hello!']}
"""