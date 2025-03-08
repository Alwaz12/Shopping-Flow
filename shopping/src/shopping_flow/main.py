import chainlit as cl
import asyncio
import os
import google.generativeai as genai
from crewai.flow import Flow, start
from shopping_flow.crews.shopping_crew.shopping_crew import ShoppingCrew

# Load the API key from an environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

# Initialize Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")  # Correct model usage

# Model settings
settings = {
    "temperature": 0.7,
    "max_output_tokens": 500,
    "top_p": 1,
}

class ShoppingFlow(Flow):
    @start()
    def find_best_products(self, product_prompt):
        """Calls CrewAI to find the best product recommendations."""
        return ShoppingCrew().crew().kickoff(inputs={"product": product_prompt})

@cl.on_chat_start
def start_chat():
    """Initialize session with conversation history."""
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )
    cl.user_session.set("flow", ShoppingFlow())  # Store the shopping flow instance


@cl.on_message
async def main(message: cl.Message):
    """Handles incoming messages and generates responses."""
    message_history = cl.user_session.get("message_history")
    flow = cl.user_session.get("flow")

    # Save user message to history
    message_history.append({"role": "user", "content": message.content})

    # Show processing indicator
    thinking_msg = cl.Message(content="Processing your request...")
    await thinking_msg.send()

    # Step 1: Try CrewAI for product recommendations
    crew_output = await asyncio.to_thread(flow.find_best_products, message.content)

    # Step 2: If CrewAI output is valid, use it; otherwise, use Gemini
    if crew_output:
        response_text = getattr(crew_output, "text", str(crew_output))  # Extract text safely
    else:
        gemini_response = await asyncio.to_thread(model.generate_content, message_history, **settings)
        response_text = gemini_response.text.strip()

    # Ensure Markdown formatting
    formatted_result = response_text.replace("\\n", "\n")

    # Save response to conversation history
    message_history.append({"role": "assistant", "content": formatted_result})

    # Remove processing message and send final response
    await thinking_msg.remove()
    await cl.Message(content=formatted_result).send()


def plot():
    """Visualize the CrewAI workflow."""
    ShoppingFlow().plot()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "plot":
        plot()
    else:
        print("To use the UI, run with: chainlit run main.py")
