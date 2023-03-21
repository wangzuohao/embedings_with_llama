from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os
# Please setup the env for OpenAI API key
# export OPENAI_API_KEY='sk-xxxxxxxxx'
documents = SimpleDirectoryReader('./src').load_data()
index = GPTSimpleVectorIndex(documents)
index.save_to_disk('index.json')
