from langchain.embeddings import HuggingFaceEmbeddings


def create_vector_db(file_path: str, persist_directory: str):
    #TODO Add code to chunk and embed document
    return 

def main():
    # Set up paths
    input_file = "../docs/oci_security.md"
    
    persist_dir = "../vectordb/oci_security_db"
    
    # Create vector database
    vectordb = create_vector_db(input_file, persist_dir)
    
    print(f"Successfully created vector database at {persist_dir}")
    
    

if __name__ == "__main__":
    main()