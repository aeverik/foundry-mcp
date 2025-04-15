import os
import subprocess

def get_commands_and_subcommands(binary):
    try:
        result = subprocess.run([binary, "--help"], capture_output=True, text=True, check=True)
        output = result.stdout
        commands = []
        lines = output.splitlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith("-") and not line.startswith("Usage") and not line.startswith("Options"):
                commands.append(line)
        return commands
    except Exception as e:
        print(f"Error running {binary}: {e}")
        return []

def main():
    binaries = ["anvil", "forge", "cast", "chisel"]
    output_file = "reference/generated/OVERVIEW.md"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write("# Overview of Foundry Binaries\n\n")
        f.write("This document provides a comprehensive overview of the binaries provided by the Foundry project, their purposes, and how to obtain them. It also includes commands, subcommands, use cases, and examples for each binary.\n\n")
        f.write("## Foundry Binaries\n\n")

        for binary in binaries:
            f.write(f"### {binary.capitalize()}\n")
            f.write("\n")
            f.write(f"**Purpose**: {binary.capitalize()} is a tool for ...\n")  # Placeholder for purpose
            f.write("**Commands**:\n")
            commands = get_commands_and_subcommands(binary)
            if commands:
                for command in commands:
                    f.write(f"- `{command}`\n")
            f.write("**Use Cases**:\n")
            f.write("- Example use case 1\n")  # Placeholder for use cases
            f.write("- Example use case 2\n")
            f.write("\n")

        f.write("## How to Obtain Foundry Binaries\n\n")
        f.write("The Foundry binaries can be obtained by cloning the Foundry repository and building the project:\n\n")
        f.write("```bash\n")
        f.write("git clone https://github.com/foundry-rs/foundry.git\n")
        f.write("cd foundry\n")
        f.write("make build\n")
        f.write("```\n\n")
        f.write("This will generate the binaries in the `target` directory.\n")

if __name__ == "__main__":
    main()