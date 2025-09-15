import chromadb
try:
    import chromadb
    chroma_available = True
except ImportError:
    chroma_available = False


class Memory:
    def __init__(self):
        if chroma_available:
            self.client = chromadb.Client()
            self.collection = self.client.create_collection("chat_memory")
            self.mode = "chroma"
        else:
            self.logs = []
            self.mode = "simple"

    def add(self, prompt: str, response: str):
        if self.mode == "chroma":
            existing_ids = self.collection.get()['ids']
            new_id = str(len(existing_ids)) if existing_ids else "0"
            self.collection.add(
                documents=[response],
                metadatas=[{"prompt": prompt}],
                ids=[new_id]
            )
        else:
            self.logs.append({"query": prompt, "response": response})

    def recall(self, query: str):
        if self.mode == "chroma":
            results = self.collection.query(query_texts=[query], n_results=2)
            return results
        else:
            return {"documents": self.logs[-3:]} if self.logs else {"documents": []}
