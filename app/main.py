from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI()

def main():
    print("Hello from travel-planner-ai!")
    
    while True:
        question = input("\nYou:")
        
        if question.lower() == "exit":
            break
        
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=question
        )
        
        print("\nAssistant:")
        print(response.output_text)


if __name__ == "__main__":
    main()
