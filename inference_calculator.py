# inference_calculator.py

# This script is a simple LLM inference calculator
# It estimates latency, memory usage, and cost based on inputs

# Predefined data for model and hardware characteristics
MODEL_INFO = {
    '7B': {'memory': 16, 'latency': 1.0, 'cost_per_million_tokens': 0.002},
    '13B': {'memory': 28, 'latency': 2.0, 'cost_per_million_tokens': 0.004},
    'GPT-4': {'memory': 45, 'latency': 3.5, 'cost_per_million_tokens': 0.06}
}

HARDWARE_INFO = {
    'A100': {'memory': 40, 'cost_per_hour': 2.5},
    'T4': {'memory': 16, 'cost_per_hour': 0.35},
    'RTX 4090': {'memory': 24, 'cost_per_hour': 0.0},  # Assume local, no cost
    'CPU': {'memory': 8, 'cost_per_hour': 0.0}         # Simplified CPU config
}

# Function to calculate latency, memory, cost per request, and compatibility
def calculate_inference(model_size, tokens, batch_size, hardware_type, deployment_mode):
    model = MODEL_INFO.get(model_size)
    hardware = HARDWARE_INFO.get(hardware_type)

    if not model or not hardware:
        return "Invalid model or hardware type."

    # Total memory needed = base model memory + some extra for batch
    memory_usage = model['memory'] + (batch_size * 0.2)
    hardware_memory = hardware['memory']
    compatible = memory_usage <= hardware_memory

    # Latency increases with tokens and batch
    latency = model['latency'] * (tokens / 1000) * (batch_size / 8)

    # Cost per request (in $)
    token_cost = (tokens / 1_000_000) * model['cost_per_million_tokens']
    if deployment_mode == 'cloud':
        time_in_hours = latency / 3600
        infra_cost = time_in_hours * hardware['cost_per_hour']
    else:
        infra_cost = 0

    total_cost = token_cost + infra_cost

    # Return all values in a simple dictionary
    return {
        'Latency (s)': round(latency, 3),
        'Memory Usage (GB)': round(memory_usage, 2),
        'Cost per Request ($)': round(total_cost, 5),
        'Hardware Compatible': compatible
    }

# Simple test runner
if __name__ == "__main__":
    print("LLM Inference Calculator\n")

    # Get user inputs
    model = input("Enter model size (7B / 13B / GPT-4): ")
    tokens = int(input("Enter number of tokens (e.g. 500): "))
    batch = int(input("Enter batch size (e.g. 8): "))
    hardware = input("Enter hardware type (A100 / T4 / RTX 4090 / CPU): ")
    deploy = input("Deployment mode (local / cloud): ")

    # Run the calculator
    result = calculate_inference(model, tokens, batch, hardware, deploy)

    # Print results
    if isinstance(result, dict):
        print("\n--- Inference Estimation ---")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("Error:", result)
