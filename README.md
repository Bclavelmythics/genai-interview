# genai-oct2024

Generative AI focused interview problems

## Prerequisites
* Sign up on together.ai and obtain a API key
* Use python 3.11 and install requirements (pip install -r requirements.txt)

## Problem 1 

Create a script to chunk the provided documentation and embed the chunks into a chroma vector database. 
Chunk the document in a way that best caputres important information from each section.
Use the HuggingFaceEmbeddings model from Langchain.
https://python.langchain.com/docs/integrations/providers/huggingface/#huggingfaceendpoint 

## Problem 2
* Add your vector database to the vectordb directory
* Modify provided script so that the llm utilizes context from the vector database that you created.
* Modify the prompt template that guides the llm in responding to the users input.


## Bonus Problem

Attempt this only after completing problem 1 and 2 and if you have time.
* Modify the script so that the llm can maintain conversation history.

