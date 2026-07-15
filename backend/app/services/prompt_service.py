from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    BaseMessage
)

class PromptService:

    def __init__(self):

        self.template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    You are an expert travel planner.

                    Responsibilities:

                    - Recommend destinations
                    - Suggest hotels
                    - Estimate travel costs
                    - Create daily itineraries

                    Keep responses practical and concise.
                  """,
                ),

                MessagesPlaceholder("history"),

                (
                    "human",
                    "{input}",
                ),
            ]
        )
    
    
    def build_prompt(
        self,
        history: list[BaseMessage],
        user_input: str,
    ):
       
        
        return self.template.invoke({
             "history": history,
             "input": user_input,
        })                  