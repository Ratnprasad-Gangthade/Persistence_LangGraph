# Persistence in LangGraph

This repository is designed to help you understand the concept of persistence in LangGraph through practical, beginner-friendly examples.

The main purpose of this project is to show how a LangGraph workflow can remember its state, continue execution later, isolate user sessions, support human approvals, and even move backward in time to earlier checkpoints.

---

## Why this repository exists

In agentic workflows, a process is often not a single short execution. It may:

- continue across multiple calls,
- pause for user input,
- run for different users with different memory,
- recover after restart,
- inspect or restore previous states for debugging.

Without persistence, the workflow behaves like a temporary run and forgets everything after it ends.

This project demonstrates how LangGraph solves that problem through checkpointing and state persistence.

---

## Learning objectives

By studying this repository, you will understand:

- what persistence means in LangGraph,
- why checkpointers are important,
- how `thread_id` creates isolated user state,
- how to save state in memory and SQLite,
- how human approval can pause and resume a graph,
- how time-travel and state history work in LangGraph.

---

## Project structure

- [01_memorysaver.py](01_memorysaver.py) — simple in-memory persistence using `MemorySaver`
- [02_sqlite_persistence.py](02_sqlite_persistence.py) — durable persistence using SQLite
- [03_threads.py](03_threads.py) — separate memory for different users via `thread_id`
- [04_human_in_the_loop.py](04_human_in_the_loop.py) — pause and resume workflow for human approval
- [05_time_travel.py](05_time_travel.py) — checkpoint history and restore earlier state
- [requirements.txt](requirements.txt) — project dependencies

---

## Core concepts covered

### 1. Persistence
Persistence means storing the workflow state so it can be reused or resumed later.

It is essential when:

- the program continues after waiting for the user,
- the app restarts,
- multiple users use the same workflow,
- a workflow needs replay, debugging, or rollback.

### 2. Checkpointer
A checkpointer is the mechanism used by LangGraph to save state.

Examples used in this project:

- `MemorySaver` for temporary in-memory persistence
- `SqliteSaver` for durable database-based persistence

### 3. Thread-based memory
A `thread_id` separates one conversation or workflow run from another.

This is critical when multiple users interact with the same graph at the same time.

### 4. Human-in-the-loop
Some workflows require a person to approve or decide before continuing.

The project demonstrates this through `interrupt()` and `Command(resume=...)`.

### 5. Time travel
LangGraph can inspect previous states and restore them using checkpoint history.

This makes debugging and controlled rollback much easier.

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run the scripts one by one:

```bash
python 01_memorysaver.py
python 02_sqlite_persistence.py
python 03_threads.py
python 04_human_in_the_loop.py
python 05_time_travel.py
```

---

## What each example teaches

### [01_memorysaver.py](01_memorysaver.py)
This is the simplest introduction to persistence. It shows that state is stored between graph invocations using a shared `thread_id`.

### [02_sqlite_persistence.py](02_sqlite_persistence.py)
This example moves beyond memory and saves the workflow state in SQLite, making the data durable across process restarts.

### [03_threads.py](03_threads.py)
This demonstrates that different users or sessions can have independent state. The same graph can serve multiple conversations without mixing them.

### [04_human_in_the_loop.py](04_human_in_the_loop.py)
This introduces workflow interruption for human decisions, such as approval or rejection before continuing execution.

### [05_time_travel.py](05_time_travel.py)
This teaches checkpoint history and state restoration, allowing the workflow to revisit earlier states and debug or replay logic.

---

## Benefits of understanding persistence in LangGraph

Learning persistence is important because it helps you build:

- more reliable AI workflows,
- memory-aware agents,
- multi-user chat systems,
- approval-based automation,
- resume-safe long-running processes,
- debugging-friendly stateful applications.

In real-world agent systems, persistence is not optional—it is one of the foundations of a robust and production-ready workflow.

---

## Final takeaway

This repository is a practical study of persistence in LangGraph. It starts with a simple memory-based example and gradually introduces stronger concepts like SQLite storage, user-specific threads, human intervention, and time-travel state inspection.

The goal is to make the concept of persistent state simple, visual, and easy to understand through working code examples.

---

## Recommended next step

After going through the files in order, try building your own small LangGraph app that:

- remembers past messages,
- stores state in SQLite,
- supports user-specific threads,
- includes a human approval step.

This will help you turn the learning from this repository into real-world agent workflow skills.
