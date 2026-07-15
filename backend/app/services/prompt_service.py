from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
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
    
    
    def convert_history(
        self,
        history: list[dict],
    ):
        
        messages = []
        
        for item in history:
            
            if item["role"] == "user":
                
                messages.append(
                    HumanMessage(
                        content=item["content"]
                    )
                )
            else:
                
                messages.append(
                    AIMessage(
                        content=item["content"]
                    )
                )
                
        return messages
    
    def build_prompt(
        self,
        history: list[dict],
        user_input: str,
    ):
        history_messages = self.convert_history(history)
        
        return self.template.invoke({
             "history": history_messages,
             "input": user_input,
        })                  