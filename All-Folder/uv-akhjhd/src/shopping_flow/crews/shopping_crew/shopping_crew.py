from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class ShoppingCrew:
    """Poem Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def shopping_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["shopping_agent"],
            tools=[SerperDevTool()],
            # verbose = True
        )

    @task
    def shopping_task(self) -> Task:
        return Task(
            config=self.tasks_config["shopping_task"],
            human_input=False
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            # verbose=True,
        )
