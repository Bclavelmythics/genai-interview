# genai-oct2024

Generative AI focused interview problems

## Prerequisites
* Sign up on together.ai and obtain an API key
* Within VScode, set up a remote tunnel into the workstation
   * We will provide the host, ssh key and user


## Problem 1: Create Vector database for RAG (Retrieval Augmented Generation) Functionality

* Modify the function `create_vector_db()` in `load/load_document.py` to chunk the provided documentation and embed the chunks into a chroma vector database. 
* Carefully Analyze the document in `docs`  to chunk it in a way that best captures important information from each section.
* Use the HuggingFaceEmbeddings model from Langchain.
  * https://python.langchain.com/docs/integrations/providers/huggingface/#huggingfaceembeddings

## Problem 2: Add RAG Functionality to Application (app.py)
* To run application use `streamlit run app.py`
   * The script is functional prior to completion of this problem, however no vector database is loaded
* Add in path to db and Together API key into "User Config Section of file"
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
  * Questions to test performance of Completed Application 
    * How can I secure my databases?
    * How can I enforce network protection for my hosts?
    * Is there a tool I can use to scan my hosts for vulnerabilities?

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
  * By default the application will print out the entire response once generated. Try to modify it so that it streams out one character at a time.

