from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    count: int


def node(state: State):
    return {"count": state["count"] + 1}


builder = StateGraph(State)

builder.add_node("node", node)

# START → node → END
builder.add_edge(START, "node")
builder.add_edge("node", END)


memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


# First execution
result1 = graph.invoke({"count": 0}, config)
print(result1)

# Second execution
result2 = graph.invoke({"count": 1}, config)
print(result2)  

"""
output should be :
{'count': 1}
{'count': 2} 
"""