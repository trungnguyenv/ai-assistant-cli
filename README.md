# ai-assistant-cli

## Overview

`ai-assistant-cli` is an open-source Python-based command line interface that simplifies the generation and execution of
commands directly from the terminal. This cross-platform tool is designed to enhance productivity and streamline command
execution.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

### Step 1: Install Poetry

`ai-assistant-cli` uses Poetry as its package manager. To install Poetry, follow the instructions on
the [official Poetry website](https://python-poetry.org/docs/).

### Step 2: Clone the Repository

Clone the `ai-assistant-cli` repository to your local machine.

```bash
git clone https://github.com/your-username/ai-assistant-cli.git
cd ai-assistant-cli
```

### Step 3: Install Dependencies

Within the cloned directory, run the following commands to install the required dependencies and build the project:

```bash
poetry install
poetry build
```

### Step 4: Install the CLI Tool

Finally, install the `ai-assistant-cli` package using pip:

```bash
pip3 install dist/ais-0.1.0-py3-none-any.whl --force-reinstall
```

## Usage

### Setting up the OpenAI API Key

Before using `ai-assistant-cli`, you need to have an OpenAI API key. After obtaining the API key, run the following
command to set it up:

```bash
ais auth set-key
```

This command will securely store your API key in your operating system's respective keychain.

### Generating Commands

#### Step 1: Enter the Prompt

To use this feature, start by typing `ais cmd` followed by your natural language prompt. For example:

```bash
ais cmd list all files in the current directory
```

#### Step 2: Review the Suggested Command

The AI will process your input and return a suggested command line instruction. This command is displayed in green for
visibility. For instance, you might see:

```bash
The suggested command is: ls -l
```

#### Step 3: Choose an Action

After reviewing the suggested command, you have three options:

- **Execute (E):** If you are satisfied with the suggestion and want to execute the command, press `E`.
- **Adjust (A):** If the command needs modification, press `A` to adjust it. You'll then be prompted to enter your
  adjustment, and the AI will generate a new suggestion based on your input.
- **Cancel (C):** If you decide not to proceed, press `C` to cancel.

#### Step 4: Executing or Adjusting the Command

- **Execute:** If you choose to execute, the command will run in your terminal. Output or errors from the command
  execution will be displayed.
- **Adjust:** If you choose to adjust, you'll be asked to provide further details or corrections. The AI will process
  your adjustments and provide a new command suggestion.

### Example Usage Scenario

1. **Input Prompt:** `ais cmd create a new Python virtual environment`

2. **AI Suggestion:** `The suggested command is: python3 -m venv myenv`

3. **User Action:** Suppose the user wants to adjust the command to specify a different folder name, they would
   choose `Adjust (A)` and enter the new folder name.

4. **Revised Suggestion:** Based on the user's input, the AI might then suggest `python3 -m venv newenv`.

5. **Execution:** The user can then execute the revised command by choosing `Execute (E)`.

## Contributing

Contributions to `ai-assistant-cli` are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more
information on how to get involved.

## License

`ai-assistant-cli` is licensed under the GNU General Public License v3.0. See the [LICENSE.md](LICENSE.md) file for more
details.

## Support

For support, questions, or feedback, please open an issue in
the [GitHub issue tracker](https://github.com/your-username/ai-assistant-cli/issues).

## Acknowledgements

Special thanks to all contributors and supporters of the `ai-assistant-cli` project.
