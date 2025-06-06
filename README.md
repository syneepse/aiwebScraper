# Aiscraper Crew

Welcome to the Aiscraper Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv from here https://docs.astral.sh/uv/getting-started/installation/:

```bash
winget install --id=astral-sh.uv  -e
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
OR (if it says that "crewai" isn't recognized, you'll need to use UV directly)
```bash
uv run crewai install
```

Additionally, you will also need to configure an embedder, this project uses ollama for the same.

Install ollama through the link here - https://ollama.com/

and then pull the embedder using the following command : 

```bash
ollama pull nomic-embed-text
```

### Customizing

**Add your `MODEL`, `GEMINI_API_KEY` and `SERPER_API_KEY` into the `.env` file**



- Modify `src/aiscraper/config/agents.yaml` to define your agents
- Modify `src/aiscraper/config/tasks.yaml` to define your tasks
- Modify `src/aiscraper/crew.py` to add your own logic, tools and specific args
- Modify `src/aiscraper/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
(OR)
```bash
$ uv run crewai run
```

This command initializes the aiScraper Crew, assembling the agents and assigning them tasks as defined in your configuration.

Output extraction - 
refer the below code for extracting the output (visible in) - 
```python
def run():
    """
    Run the crew.
    """
    inputs = {
        'company_name': 'McKinsey & Company',
        # 'current_year': str(datetime.now().year)
    }
    
    try:
        run_output = Aiscraper().crew().kickoff(inputs=inputs)
        print(f"Crew run completed successfully. Output: {run_output}")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
```

## Understanding Your Crew

The aiScraper Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Aiscraper Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
