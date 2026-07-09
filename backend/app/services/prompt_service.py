"""
Prompt Service using LangChain's ChatPromptTemplate
This makes our prompts maintainable and versionable
"""
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from typing import List, Dict
from app.core.config import settings

logger = logging.getLogger(__name__)
class PromptService:

    def __init__(self):
        """Initialize prompt templates """
        # Primary system prompt - Travel Planner
        self.travel_planner_prompt = ChatPromptTemplate([
            ("system", """You are expert travel planner AI assistant for Dubai and UAE.
             

            Your expertise includes:
            - Dubai tourism, attractions, and hidden gems
            - Luxury travel and budget options
            - Cultural considerations and local customs
            - Weather patterns and best visiting times
            - Dining, shopping, and entertainment options
            - Transportation and logistics
            - Safety and travel tips
             
            Response Guidelines:
            - Be specific and actionable
            - Provide practical tips (not just generic advice)
            - Consider the user's preferences and constraints
            - Offer alternatives when possible
            - Be enthusiastic and engaging
            - Acknowledge cultural sensitivities 
             
            Current Context:
            - You're helping a traveler plan their visit to Dubai
            - The user may be from any country
            - Adjust recommendations based on budget, duration, and interests
            - Include practical details like estimated costs, timing, and location info"""),

            MessagesPlaceholder(variable_name="history"),
            
            ("human", "{input}") 
        ])

        # Alternative prompt for testing (A/B testing ready)
        self.concise_planner_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a concise Dubai travel planner. 
            Keep responses under 100 words unless asked for details.
            Focus on must-see attractions and practical tips."""),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        
        # Default to the full planner
        self.active_template = self.travel_planner_prompt
        logger.info("PromptService initialized with travel planner template")
    
    # SYSTEM_PROMPT = """
    #         You are an expert travel planner.
            
    #         Always:
            
    #         - Recommend destinations.
    #         - Estimate costs.
    #         - Suggest hotels.
    #         - Give daily itinerary.
            
            
            
    #         Keep answers concise and practical.
    #         """
            
    def build_prompt(self, history: list['dict']) -> str:
        conversation = ""
        
        for message in history:
            conversation += (
                f"{message['role']}: {message['content']}\n"
            )
        return f"""
           {self.SYSTEM_PROMPT}

           Conversation:

          {conversation}

           Assistant:
     """       