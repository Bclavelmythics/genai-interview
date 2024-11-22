import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import Together
from langchain.chains import LLMChain
import os

# ============ USER CONFIG SECTION ============
# Set your vector database path here
VECTOR_DB_PATH = ""  # User should modify this

# Set your Together.ai API key here
TOGETHER_API_KEY = ""  # User should modify this
# =============================================

# Set the API key for Together.ai
os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY


def initialize_vectordb():
    if not VECTOR_DB_PATH:
        return None  
    
    #TODO Create code for loading vector database 
    

def get_context(query, vectordb=None):
    if vectordb is None:
        return ""
    
    #TODO Create code for completing semantic search on vectordb 
    

def main():
    st.title("OCI Security Services")
    
    vectordb = initialize_vectordb()
    
    if vectordb:
        st.info("Vector database loaded successfully! Using contextual responses.")
    else:
        st.info("No vector database configured. The assistant will provide general responses.")
    
    
    query = st.text_input("Enter your question about OCI security services:")
    
    if query:
        context = get_context(query, vectordb) if vectordb else ""
        
        
        if context:
            with st.expander("View Retrieved Context"):
                st.markdown(context)
        
        try:
            
            llm = Together(
                model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                max_tokens=500
            )
            
            
            if context:
                #TODO Once added chroma db, modify this prompt template 
                prompt = PromptTemplate(
                    template="""

                    """,
                    input_variables=["context", "question"]
                )
            else:
                prompt = PromptTemplate(
                    template="""
                    
                    Question: {question}

                    Answer:""",
                    input_variables=["question"]
                )
            
         
            chain = LLMChain(llm=llm, prompt=prompt)
            response = chain.run(
                context=context if context else "",
                question=query
            )
            
            
            st.markdown("### Answer")
            st.markdown(response)
            
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

if __name__ == "__main__":
    main()
