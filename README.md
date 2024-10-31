# genai-oct2024

Generative AI focused interview problems

## Prerequisites
* Sign up on together.ai and obtain an API key
* clone this repository `git clone https://github.com/Bclavelmythics/genai-interview.git`
* Use python 3.11 and install requirements
  * `pip3.11 install -r requirements.txt`

## Problem 1: Create Vector database for RAG (Retrieval Augmented Generation) Functionality

* Create a script to chunk the provided documentation and embed the chunks into a chroma vector database. 
* Chunk the document in a way that best caputres important information from each section.
* Use the HuggingFaceEmbeddings model from Langchain.
  * https://python.langchain.com/docs/integrations/providers/huggingface/#huggingfaceembeddings

## Problem 2: Add RAG Functionality to Application
* To run application use `streamlit run app.py`
   * The script is functional prior to completing this problem
* Add your vector database to the vectordb directory
* Modify provided script so that the llm utilizes context from the vector database that you created.
* Modify the prompt template that guides the llm in responding to the users input.


## Bonus Problem

Attempt this only after completing problem 1 and 2 and if you have time.
* Modify the script so that the llm can maintain conversation history.

