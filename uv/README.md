# Shopping Flow

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

```bash
cd shopping_flow
```

First, if you haven't already, install uv

```bash
pip install uv
```

Create virtual environment and activate it
```bash
uv venv
```

For windows
```bash
source ./.venv/Scripts/activate
```

initialize the uv venv
```bash
uv add -r requirements.txt
```

run the agent
```bash
chainlit run src/shopping_flow/main.py
```


