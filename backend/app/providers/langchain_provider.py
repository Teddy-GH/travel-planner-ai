"""
LangChain Provider - Wraps Gemini with LangChain's standardized interface
This is the key integration point that makes our app enterprise-ready
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import BaseMessage, SystemMessage, HumanMessage, AIMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict, AsyncIterator, Optional 
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class LangChainProvider:

    """
     Provider using LangChain's unified interface.
    
    Benefits:
    - Standardized message format (SystemMessage, HumanMessage, AIMessage)
    - Easy to swap LLM providers (OpenAI, Anthropic, etc.)
    - Built-in streaming, batching, and async support
    - Production-ready error handling
    
    """

    def __init__(self):
        """Initialize the langchain provider with Google gemini """
        logger.info(f"Initializing Langcahin provider with model: {settings.model_name}")

        self.llm = ChatGoogleGenerativeAI(
            model=settings.model_name,
            google_api_key=settings.gemini_api_key,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            convert_system_message_to_human=True,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()] if settings.debug else [],
        )

        logger.info("Langchain provider initialized successfully")

    def _convert_to_langchain_messages(self, messages: List[Dict[str, str]]) -> List[BaseMessage]:
        """
        Convert our message format to LangChain's format
        
        Our format: [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
        LangChain format: [SystemMessage(content="..."), HumanMessage(content="...")]
        """
        langchain_messages = []

        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")    
            
            if role == "system":
                langchain_messages.append(SystemMessage(content=content))
            elif role == "assistant":
                langchain_messages.append(AIMessage(content=content))  
            elif role == "user":
                langchain_messages.append(HumanMessage(content=content))
            else:
                logger.warning(f"Unknown role '{role}', treating as human message")
                langchain_messages.append(HumanMessage(content=content))

        return langchain_messages              

    def _convert_from_langchain(self, response: BaseMessage) -> str:
        """Extract content from LangChain response"""
        return response.content

    async def generate_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate a complete responses, API endpoints that don't need streaming

        Use case: Quick responses, API endpoints that don't need streaming
        """ 

        try:
            logger.debug(f"Generating response for {len(messages)} messages")

            langchain_messages = self._convert_to_langchain_message(messages)
            response = await self.llm.ainvoke(langchain_messages)

            return self.convert_from_langchain(response)
        
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            raise RuntimeError(f"LLM generation failed: {str(e)}")
        

    async def stream_response(self, messages: List[DIct[str, str]]) -> AsyncIterator[str]:
        """
        Stream response token by token
        Use case: Real-time chat, better user experience
        """ 
        try:
            logger.info(f"Streaming response for {len(messasges)} messages")

            langchain_messages = self._convert_to_langchain_messages(messages)

            # Use astream for async streaming
            async for chunk in self.llm.astream(langchain_messages):
                # Chunk is a message with content
                if chunk.content:
                        yield chunk.content  
        except Exception as e:
            logger.error(f"Error streaming response: {str(e)}")
            yield f"Error: {str(e)}"   


    async def batch_generate(self, messages_list: List[List[Dict[str, str]]]) -> List[str]:
        
        """
        Generate responses for multiple conversations in parallel
        
        Use case: Batch processing, multi-user scenarios  
        """

        try:
                langchain_messages_list = [
                    self._convert_to_langchain_messages(messages)
                    for messages in messages_list
                ]

                responses = await self.llm.abatch(langchain_messages_list)
                return [self._convert_from_langchain(r) for r in responses]
        except Exception as e:
                logger.error(f"Error in batch generation: [str(e)]")
                raise RuntimeError(f"Batch generation failed: {str(e)}")
                
        


