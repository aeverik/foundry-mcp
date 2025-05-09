# foundry-mcp
An MCP server for [foundry](https://github.com/foundry-rs/foundry)

The server provides MCP tools for all binaries in the foundry project, fully encompassing each command and subcommand those binaries provide. 

## How this project is created

This project is generated by GitHub Copilot in Agent Mode.

### Step 1: Cloning Reference Repositories
The agent begins by cloning the following repositories into submodules under the `reference` directory:
- [Foundry](https://github.com/foundry-rs/foundry): Provides the core binaries and tools.
- [Foundry Book](https://github.com/foundry-rs/book): Offers documentation and examples for Foundry.
- [UV MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/git): Serves as a reference implementation for MCP servers.

### Step 2: Generating an Overview
With the reference repositories as context, the agent determines the binaries provided by Foundry, their purposes, and how to obtain them. A comprehensive `OVERVIEW.md` is generated, describing these findings. This document includes:
- A list of Foundry binaries.
- Commands and subcommands for each binary, generated using a script for accuracy.
- Use cases and examples.

### Step 3: Creating a Skeleton MCP Server
The agent creates a Python-based skeleton MCP server in the root directory of this workspace. The skeleton includes:
- A build script.
- Starting entry points to the binaries.
- Documentation for setup and usage, including:
  - Top-level `.py` docstrings for setup and usage.
  - Inline docstrings for each function, providing a description of their functionality.

### Step 4: Iterative Development
The agent iterates through the following steps:
1. Ensures the base project builds and executes successfully.
2. Verifies that every Foundry binary is represented accurately in the skeleton.
3. Adds MCP tools for each binary, command, and subcommand.
4. Tests each tool immediately after it is produced, ensuring functionality before proceeding to the next tool. This iterative testing approach allows the agent to quickly improve the tool generation process and minimize errors.

### Note on Script Usage
Whenever possible, the agent prefers using scripts to automate tasks such as generating command lists or overviews. This ensures accuracy, comprehensiveness, and consistency across the project. Scripts like `parse_foundry_commands.py` are used to extract detailed information directly from the binaries, reducing the likelihood of errors and omissions.

### Step 5: Leveraging MCP Features
The MCP server is designed to utilize key MCP features, including:
- **Tools**: Exposing Foundry commands as executable tools.
- **Resources**: Providing access to Foundry documentation and examples.
- **Prompts**: Offering predefined templates for common tasks.
- **Transports**: Supporting both stdio and SSE for communication.

### Step 6: Testing and Validation
Each tool and feature is rigorously tested using the MCP Inspector and other debugging tools. The server is validated against the MCP specification to ensure compliance.

### Supreme Rule: Avoid Committing Directly to `main`

**IMPORTANT**: The agent must always verify its current branch before executing any task. If the agent is on the `main` branch, it must immediately check out to a new branch before proceeding. This ensures that no changes are ever committed directly to the `main` branch.

### Checking the Current Branch

The agent must always verify its current branch before executing any task. To do this, the agent should use the `git` MCP server instead of the command line. This ensures consistency and avoids unnecessary reliance on external tools.

#### Steps to Check the Current Branch:
1. Use the `git` MCP server to retrieve the current branch name.
2. If the current branch is `main`, the agent must:
   - Create a new branch with a descriptive name.
   - Switch to the new branch.
3. Proceed with the task only after switching to the new branch.

This process ensures that no changes are ever committed directly to the `main` branch, maintaining a clean and auditable git history.

#### Steps to Follow:
1. **Check Current Branch**: Before executing any task, the agent must run a command to determine the current branch.
2. **Create a New Branch if on `main`**: If the current branch is `main`, the agent must:
   - Create a new branch with a descriptive name.
   - Switch to the new branch.
3. **Proceed with Task**: Only after switching to a new branch should the agent proceed with executing the task.

This rule is critical to maintaining a clean and auditable git history. Violating this rule can lead to confusion and potential loss of traceability.

### Git Commit Logging for Generations

In order to build a knowledge base, allow for audits, and preserve the generation process, the agent will use git commits to log its generations. The following process will be followed for each prompt execution:

1. **Branch Creation**: A new git branch will be created for each prompt execution automatically.
2. **Commit Message**: The commit message will include:
   - The user prompt from the Copilot chat.
   - A full list of context used.
   - Output in the GitHub Copilot chat.
   - An explanation of the changes and the reasoning behind them.
3. **User Approval for Merge**: After proposing changes, the agent will ask the user for permission to merge the branch into the main branch. The agent will not ask for permission to create the branch or commit changes.
4. **Revisions**: If the user rejects the changes, the agent will revise them in the current side branch and create a new commit. This process will continue until the user accepts the changes.
5. **Merge**: Once the user accepts the changes, the branch will be merged into the main branch.

This process ensures transparency, traceability, and a robust audit trail for all changes made by the agent.

## Additional Resources
- [MCP Documentation](https://modelcontextprotocol.io/docs/concepts/architecture): Learn more about the Model Context Protocol.
- [Foundry Documentation](https://github.com/foundry-rs/book): Explore Foundry's capabilities and examples.
- [UV MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/git): Reference implementation for MCP servers.