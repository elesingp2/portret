from openai import OpenAI
from keys.llm_keys import OPENAI_API_KEY


class open_AI_embeddings:

    def __init__(self):
        self.client=OpenAI(api_key=OPENAI_API_KEY)
        self.model_name="text-embedding-3-small"
    def transform(self,line):
        print(line, "emb")
        return self.client.embeddings.create(input=line,model=self.model_name).data[0].embedding
  #1536 длинна