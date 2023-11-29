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

To generate a command, use the `ais cmd` followed by your prompt. No escape is required for the prompt. For example:

```bash
ais cmd print the current user name
```

This will instruct the assistant to generate and execute the appropriate command based on your prompt.

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
