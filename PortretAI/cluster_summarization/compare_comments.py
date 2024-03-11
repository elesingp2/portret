from prompt_library.system_prompt_for_comments import system_prompt_for_comments
from utils.save_to_file import save_to_file
from utils.clear_file import clear_file
from paths import compare_clusters_file_path

from openai import OpenAI
from keys.llm_keys import OPENAI_API_KEY

def compare_comments(label, cluster_summary, cluster_text, compare_clusters_path):
        client = OpenAI(api_key=OPENAI_API_KEY)
        cluster_text = "".join(cluster_text[:100])  # Ограничиваем количество комментариев для суммаризации

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt_for_comments
                },
                {
                    "role": "user",
                    "content": "Суммаризация кластеров: " + cluster_summary + "Кластеры: " + cluster_text
                }
            ],
            temperature=0.5,
            max_tokens=300,
            top_p=1
        )
        
        if response.choices:
            summary = response.choices[0].message.content  # Corrected access to message content
        else:
            summary = "Summary not available."

        save_to_file(label, summary, compare_clusters_path)
