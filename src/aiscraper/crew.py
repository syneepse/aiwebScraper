from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, WebsiteSearchTool

from pydantic import BaseModel
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class CompanyDetails(BaseModel):
    Name: str
    Official_Website: str
    LinkedIn_URL: str
    Location: str
    Industry: str

embedder_config_ollama={
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",             
        }}
    
@CrewBase
class Aiscraper():
    """Aiscraper crew"""

    scrape_website_tool = WebsiteSearchTool(
        config=dict(
        # Keep default LLM (Google Gemini) by not specifying llm config
        embedder=dict(
            provider="ollama",
            config=dict(
                model="nomic-embed-text",
                # url="http://localhost:11434/api/embeddings"  # Default Ollama URL
            ),
        ),
    )
    )
    serper_dev_tool = SerperDevTool()

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            tools=[self.scrape_website_tool, self.serper_dev_tool] # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_pydantic=CompanyDetails
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Aiscraper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            
            max_rpm=6
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
