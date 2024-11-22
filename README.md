# genai-oct2024

Generative AI focused interview problems

## Prerequisites
* Sign up on together.ai and obtain an API key
* clone this repository
  * `git clone https://github.com/Bclavelmythics/genai-interview.git`
* Use python 3.11 and install requirements
  * `pip3.11 install -r requirements.txt`
* If installing requirements fail run the following commands instead
     * `pip3.11 install streamlit`
     * `pip3.11 install langchain`
     * `pip3.11 install langchain_community`

## Demo Questions: Test Performance of the Completed Application
* How can I secure my databases?
* How can I enforce network protection for my hosts?
* Is there a tool I can use to scan my hosts for vulnerabilities?

## Problem 1: Create Vector database for RAG (Retrieval Augmented Generation) Functionality

* Modify the empty python file in `load` to chunk the provided documentation and embed the chunks into a chroma vector database. 
* Carefully Analyze the document in `docs`  to chunk it in a way that best captures important information from each section.
* Use the HuggingFaceEmbeddings model from Langchain.
  * https://python.langchain.com/docs/integrations/providers/huggingface/#huggingfaceembeddings

## Problem 2: Add RAG Functionality to Application
* To run application use `streamlit run app.py`
   * The script is functional prior to completion of this problem, however no vector database is loaded
* Modify the following section to load the database into the application
```python
def initialize_vectordb():
 if not VECTOR_DB_PATH:
     return None  

#TODO Create code to load and return vector database
```

* Modify the following section so that the application fetches context from the vector database
```python
def get_context(query, vectordb=None):
    if vectordb is None:
        return ""
    
    #TODO Create code for completing semantic search on vectordb 
``` 
* Modify the following section to give llm instructions for generating response. Analyze the Test Questions and the document chunked to help create prompt.
```python
if context:
     #TODO Once added chroma db, modify this prompt template 
     prompt = PromptTemplate(
         template="""

         """,
         input_variables=["context", "question"]
     )
```

## Bonus Problems

Attempt these only after completing problem 1 and 2 and if you have time.
* Modify the script so that the llm can maintain conversation history
* Modify the script so that the response is streamed out instead of pasted all at once

