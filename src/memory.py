import chromadb

class Memory:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("chat_memory")

    def add(self, prompt: str, response: str):
        self.collection.add(
            documents=[response],
            metadatas=[{"prompt": prompt}],
            ids=[str(len(self.collection.get()['ids']))]
        )

    def recall(self, query: str):
        results = self.collection.query(query_texts=[query], n_results=2)
        return results
