from collections import deque

def bfs_stock_prediction(start_price, steps):
    # Possible movements: Up (+1), Down (-1), Stable (0)
    moves = [1, -1, 0]
    
    # Queue for BFS (price, current_step)
    queue = deque([(start_price, 0)])
    
    predictions = []

    while queue:
        price, step = queue.popleft()
        
        if step == steps:
            predictions.append(price)
            continue
        
        for move in moves:
            next_price = price + move
            queue.append((next_price, step + 1))
    
    return predictions


# Example usage
start_price = 100
steps = 3
predicted_prices = bfs_stock_prediction(start_price, steps)

print("Predicted possible stock prices after", steps, "steps:")
print(predicted_prices)
