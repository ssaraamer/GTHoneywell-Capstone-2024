from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)


# Initialize the API and model
llama = LlamaAPI("LL-yIIoasP8fCMvQ4h5She54IEmLjurmEa5nUehOwlMyGQfsm7Rd5cvswJWfSuo1kPp")
# For more information, reference the LangChain Documentation!
model = ChatLlamaAPI(client=llama)

# Predefined system message
system_message = SystemMessage(content="""
You are the Honeywell Industrial Management Chat Bot, designed to assist Honeywell engineers with industrial tasks, provide information on equipment status, and offer troubleshooting guidance. Your responses should be informative, precise, and aligned with Honeywell's standards for professional communication.
""")

# Main chat loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Check for exit condition
    if user_input.lower() == 'quit':
        # Terminal response, not visible to user
        print("Exiting chat...")
        break

    # Prepare the messages list with the system message and the new human message
    messages = [
        system_message,
        HumanMessage(content=user_input)
    ]
    
    # Invoke the model with the current set of messages
    response = model.invoke(messages)

    # Print the model's response
    print("Bot:", response.content)

# This loop will continue until the user types 'quit'