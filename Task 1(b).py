def dfs_weather_forecast(current_weather, transitions, steps, path=None):
    if path is None:
        path = [current_weather]
    
    if steps == 0:
        print(" → ".join(path))
        return
    
    # DFS recursion
    for next_weather in transitions.get(current_weather, []):
        dfs_weather_forecast(next_weather, transitions, steps - 1, path + [next_weather])


# Weather transition graph
transitions = {
    "Sunny": ["Cloudy", "Sunny"],
    "Cloudy": ["Rainy", "Sunny"],
    "Rainy": ["Cloudy"]
}

# Example usage
start_weather = "Sunny"
steps = 3
print("Possible Weather Forecast Paths:")
dfs_weather_forecast(start_weather, transitions, steps)
