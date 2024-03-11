from openai import OpenAI
OPENAI_API_KE="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"


class open_AI_embeddings:

    def __init__(self):
        self.client=OpenAI(api_key=OPENAI_API_KE)
        self.model_name="text-embedding-3-small"
    def transform(self,line):
        print(line, "emb")
        return self.client.embeddings.create(input=line,model=self.model_name).data[0].embedding
  #1536 длинна