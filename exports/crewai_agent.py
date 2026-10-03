from crewai import Agent

vector_index_pruning_engine = Agent(
    role="Vector Index Pruning Engine",
    goal="Deliver high-precision autonomous Vector Index Pruning Engine operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
