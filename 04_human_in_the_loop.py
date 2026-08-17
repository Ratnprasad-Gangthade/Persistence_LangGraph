from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt


class State(TypedDict):
    approved: bool


def review(state: State):
    decision = interrupt("Approve? Type approve or reject")

    return {
        "approved": decision == "approve"
    }


def send(state: State):
    if state["approved"]:
        print("Email sent!")
    else:
        print("Email rejected!")

    return state


builder = StateGraph(State)

builder.add_node("review", review)
builder.add_node("send", send)

builder.add_edge(START, "review")
builder.add_edge("review", "send")
builder.add_edge("send", END)

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


config = {
    "configurable": {
        "thread_id": "email-1"
    }
}


# Start the graph
graph.invoke(
    {"approved": False},
    config
)


# Resume after human decision
graph.invoke(
    Command(resume="approve"),
    config
)              # output: Email sent!


"""
graph.invoke(
    Command(resume="reject"),
    config
)             # output: Email rejected! 
"""

