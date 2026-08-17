import sqlite3
from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver


class State(TypedDict):
    message: str


def node(state: State):
    return {"message": state["message"] + " Hello!"}


builder = StateGraph(State)

builder.add_node("node", node)

# START → node → END
builder.add_edge(START, "node")
builder.add_edge("node", END)


conn = sqlite3.connect(
    "memory.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(conn)

graph = builder.compile(
    checkpointer=checkpointer
)


config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


result = graph.invoke(
    {"message": "Hi"},
    config
)

print(result)

"""
output will be :
{'message': 'Hi Hello!'}"""