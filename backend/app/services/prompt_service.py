class PromptService:
    
    SYSTEM_PROMPT = """
            You are an expert travel planner.add()
            
            Always:
            
            - Recommend destinations.
            - Estimate costs.
            - Suggest hotels.
            - Give daily itinerary.
            
            
            
            Keep answers concise and practical.
            """
            
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