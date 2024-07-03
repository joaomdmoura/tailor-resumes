from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class TailorResumeCrew():
    """TailorResume crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def job_requirements_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['job_requirements_extractor'],
            tools=[ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def resume_tailor(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_tailor'],
            allow_delegation=False,
            verbose=True
        )

    @task
    def extract_job_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_job_requirements_task'],
            agent=self.job_requirements_extractor()
        )

    @task
    def tailor_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['tailor_resume_task'],
            agent=self.resume_tailor(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TailorResume crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )