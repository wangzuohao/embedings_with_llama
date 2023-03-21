# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

# Please setup the env for OpenAI API key with the following command in Linux
# export OPENAI_API_KEY='sk-xxxxxxxxx'

# Loading from a directory ./src
documents = SimpleDirectoryReader('./src').load_data()

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
