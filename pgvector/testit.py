import getpass
import os

# from dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

loader = TextLoader("./state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

# PGVector needs the connection string to the database.
CONNECTION_STRING = "postgresql+psycopg2://testuser:testpwd@localhost:5432/vectordb"

# # Alternatively, you can create it from environment variables.
# import os

# CONNECTION_STRING = PGVector.connection_string_from_db_params(
#     driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
#     host=os.environ.get("PGVECTOR_HOST", "localhost"),
#     port=int(os.environ.get("PGVECTOR_PORT", "5432")),
#     database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
#     user=os.environ.get("PGVECTOR_USER", "postgres"),
#     password=os.environ.get("PGVECTOR_PASSWORD", "postgres"),
# )

# The PGVector Module will try to create a table with the name of the collection.
# So, make sure that the collection name is unique and the user has the permission to create a table.

COLLECTION_NAME = "state_of_the_union_test"

db = PGVector.from_documents(
    embedding=embeddings,
    documents=docs,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
)
