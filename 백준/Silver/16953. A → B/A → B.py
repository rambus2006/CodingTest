from collections import deque

def transform(A, B):
    # BFS initialization
    queue = deque([(A, 1)])  # (current_value, operation_count)
    visited = set([A])
    
    while queue:
        current, steps = queue.popleft()
        
        # Check if we reached B
        if current == B:
            return steps
        
        # Try multiplying by 2
        next_val = current * 2
        if next_val <= B and next_val not in visited:
            visited.add(next_val)
            queue.append((next_val, steps + 1))
        
        # Try appending '1'
        next_val = int(str(current) + '1')
        if next_val <= B and next_val not in visited:
            visited.add(next_val)
            queue.append((next_val, steps + 1))
    
    # If no solution is found
    return -1

# Input
A, B = map(int, input().split())

# Output
print(transform(A, B))
