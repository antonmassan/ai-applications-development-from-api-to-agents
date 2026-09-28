from commons.models.conversation import Conversation
from commons.models.message import Message
from commons.models.role import Role
from t1_llm_api.base_client import AIClient


async def start(stream: bool, client: AIClient) -> None:
    """
    Start an interactive chat session with an AI client.

    This function runs a continuous loop that:
    1. Prompts the user for input
    2. Sends the conversation history to the AI
    3. Displays the AI's response
    4. Maintains conversation context

    The loop continues until the user types 'exit'.

    Args:
        stream (bool): If True, use streaming responses (real-time token display).
                      If False, use synchronous responses (complete response at once).
        client (AIClient): The AI client instance to use for generating responses.
    """

    conversation = Conversation()
    print("Type your question or 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Add user message to conversation
        user_message = Message(role=Role.USER, content=user_input)
        conversation.add_message(user_message)

        if stream == True:
            # Stream response from AI client
            print("AI: ", end="")
            assistant_response = await client.stream_response(conversation.messages)
        else:
            # Get complete response from AI client
            assistant_response = client.response(conversation.messages)
            print(f"AI: {assistant_response.content}")

        # Add assistant message to conversation
        conversation.add_message(assistant_response)

        


