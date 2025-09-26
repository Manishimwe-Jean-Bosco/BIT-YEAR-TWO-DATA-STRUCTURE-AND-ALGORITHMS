# -----------------------------
# STACK (LIFO - Last In First Out)
# -----------------------------

# 1. Practical (MoMo example)
stack = []
stack.extend(["step1", "step2", "step3"])   # push
print("Stack after pushing:", stack)

stack.pop()   # undo 1 (remove step3)
stack.pop()   # undo 2 (remove step2)
print("Remaining after undo 2:", stack)   # ["step1"]

# 2. Practical (Canvas example)
stack = ["LessonA", "LessonB", "LessonC"]
print("\nCanvas pushed:", stack)

stack.pop()   # undo last
print("Remaining after undo last:", stack)  # ["LessonA", "LessonB"]

# 3. Challenge: Reverse "LIFOORDER"
word = "LIFOORDER"
stack = []
for ch in word:      # push each letter
    stack.append(ch)

reversed_word = ""
while stack:         # pop all to reverse
    reversed_word += stack.pop()

print("\nReversed word:", reversed_word)  # "REDROOFIL"

# 4. Reflection
print("Stack gives last action first because it follows LIFO.\n")


# -----------------------------
# QUEUE (FIFO - First In First Out)
# -----------------------------
from collections import deque

# 5. Practical (Airtel clients)
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6"])
print("Queue of clients:", list(queue))

# serving in FIFO
queue.popleft()  # Client1
queue.popleft()  # Client2
third_served = queue.popleft()
print("Third served:", third_served)  # Client3

# 6. Practical (Nyabugogo buses)
queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5"])
queue.popleft()  # Bus1 leaves
queue.popleft()  # Bus2 leaves
print("\nFront bus after 2 leave:", queue[0])  # Bus3

# 7. Challenge: Queue system for RRA
queue = deque(["ClientA", "ClientB", "ClientC"])
print("\nRRA Queue:", list(queue))
serving_order = [queue.popleft() for _ in range(len(queue))]
print("Serving order will be:", serving_order)
print("Stack would fail because it serves last joined first (LIFO), unfair.\n")

# 8. Reflection
print("FIFO ensures discipline because first come = first served (fair order).")
