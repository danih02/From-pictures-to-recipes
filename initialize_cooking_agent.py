#from langchain.tools import DuckDuckGoSearchResults
#search = DuckDuckGoSearchResults()
def cooking_agent(llm):
    """Initialize the cooking agent with a search tool."""
    # Initialize the Tavily search tool
    # This tool will be used to search for recipes based on user queries
    # It is assumed that the llm is already defined and configured
    from langchain.tools.tavily_search import TavilySearchResults
    from langgraph.prebuilt import create_react_agent

    # Create a search tool instance
    search = TavilySearchResults()
    tools = [search]
    agent_executor = create_react_agent(llm, tools, prompt = "Du bist ein hilfreicher Assistent, der das Web nach Rezepten durchsucht und die Rezepte rauszieht. "
                                        "Du antwortest auf die Frage des Benutzers, indem du eine Liste von Rezepten zurückgibst, die den Zutaten entsprechen, die der Benutzer angibt. "
                                        "Wenn du keine Rezepte findest, sag dem Benutzer, dass du keine gefunden hast. "
                                        "Wichtig: Deine Antwort muss: 1. Die Zutatenliste, 2. Die Zubereitungsschritte und 3. die Links zu den Rezepten enthalten.")
    return agent_executor