import subprocess
import sys

# Define the arguments to pass
config_file = "/home/matan/Projects/monocon-pytorch/outputs/2024_27_Aug_00_30/config.yaml"
checkpoint_file = "/home/matan/Projects/monocon-pytorch/outputs/2024_27_Aug_00_30/checkpoints/epoch_200.pth"
gpu_id = 0  # Index of GPU to use
evaluate = True  # Set to True to evaluate
visualize = False  # Set to True to visualize
save_dir = "/home/matan/Projects/monocon-pytorch/outputs_eval/debug_01"  # Path to save visualized results

# Use sys.executable to dynamically find the Python interpreter
command = [
    sys.executable, "/home/matan/Projects/monocon-pytorch/test.py",  # Specify the Python interpreter and script
    "--config_file", config_file,
    "--checkpoint_file", checkpoint_file,
    "--gpu_id", str(gpu_id)
]

# Add optional arguments based on the user's settings
if evaluate:
    command.append("--evaluate")
if visualize:
    command.append("--visualize")
    command.extend(["--save_dir", save_dir])

# Execute the script with arguments
subprocess.run(command)
