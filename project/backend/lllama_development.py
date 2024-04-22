from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI

# Initialize the API and model
# Will need to develop better security protocols to keep api key hidden  
llama = LlamaAPI("LL-yIIoasP8fCMvQ4h5She54IEmLjurmEa5nUehOwlMyGQfsm7Rd5cvswJWfSuo1kPp")
model = ChatLlamaAPI(client=llama)

from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

template_messages = [
    SystemMessage(
        content="You are the Honeywell Industrial Management Chat Bot, designed to assist Honeywell engineers with industrial tasks, provide information on equipment status, and offer troubleshooting guidance. Your responses should be informative, precise, and aligned with Honeywell's standards for professional communication. Try not to be overly verbose"
        ),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]

prompt_template = ChatPromptTemplate.from_messages(template_messages)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = LLMChain(llm=model, prompt=prompt_template, memory=memory)

def get_llama_response(user_input):
    return chain.invoke(user_input)['text']