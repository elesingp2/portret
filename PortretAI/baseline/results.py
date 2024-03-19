import pandas as pd

# Предобработка текста
from preprocess.preprocess_v1 import preprocess_clusterization

# Векторизация
from embeddings.navec.embeddings_navec import w2v_vectorizer
from embeddings.openai.embeddings_openai import open_AI_embeddings

# Кластеризация
from sklearn.cluster import KMeans

# Метрики
from metrics.silhouette_score import evaluate_clustering

# Дополнительные утилиты
from utils.popular_words import find_important_words
from utils.save_to_file import save_to_file
from utils.clear_file import clear_file
from collections import defaultdict
from paths.clusters_file_path import clusters_path
from paths.compare_clusters_file_path import compare_clusters_path

# Саммаризация кластеризированного текста
from cluster_summarization.summarization_yandex import summarize_clusters_yandex_gpt
from cluster_summarization.summarization_gpt import summarize_clusters_gpt
from create_examples.create_examples_gpt import compare_comments

# Генерация репорта
from report_generation.report_generation_gpt import generate_overall_report

class TextClusterAnalysis:
    def __init__(self, comments_path):
        self.comments_path = comments_path
        self.comments = pd.read_csv(comments_path)
        self.vectorizer = open_AI_embeddings()
        self.k = 2 # Предполагаемое количество кластеров

    def preprocess_comments(self):
        self.preprocess=preprocess_clusterization()
        return [self.preprocess.preprocess_text_morph(comment) for comment in self.comments['text']]

    def vectorize_text(self, preprocessed_comments):
        #for comment in preprocessed_comments:
            #preprocessed_comments.append(filter(lambda x: x is not None, comment))
        #X = self.vectorizer.transform(preprocessed_comments.dropna())
        X = [self.vectorizer.transform(comment) for comment in preprocessed_comments]
        return X

    def cluster_comments(self, X_normalized):
        model = KMeans(n_clusters=self.k, random_state=42)
        #print(X_normalized)
        model.fit(X_normalized)
        return model.labels_
    
    def create_examples(self, clusters, cluster_summaries):
        clear_file(compare_clusters_path)
        for label in clusters:
            for cluster_id in cluster_summaries:
                if (cluster_id == label):
                    print(clusters[label], cluster_summaries[cluster_id])
                    compare_comments(label, cluster_summaries[cluster_id], clusters[label], compare_clusters_path)

    def analyze_clusters(self, labels, comments):
        clusters = defaultdict(list)
        #print(comments)
        for comment, label in zip(comments.text, labels):
            #print(label)
            clusters[label].append(comment)

        ### Сохранение класторов в static.txt ###
        clear_file(clusters_path)
        for label in clusters:
            save_to_file(label, clusters[label], clusters_path)

        return clusters

    def summarize_clusters(self, clusters):
        print(clusters)
        return summarize_clusters_gpt(clusters)

    def generate_report(self, cluster_summaries):
        return generate_overall_report(cluster_summaries)

    def run_analysis(self):
        preprocessed_comments = self.preprocess_comments()
        X_normalized = self.vectorize_text(preprocessed_comments)
        labels = self.cluster_comments(X_normalized)
        clusters = self.analyze_clusters(labels, self.comments)
        
        #important_words = find_important_words(preprocessed_comments, N=10)
        
        score = evaluate_clustering(X_normalized, labels)
        
        cluster_summaries = self.summarize_clusters(clusters)

        ### 10 наиболее подходящих под кластер комментариев ###
        self.create_examples(clusters, cluster_summaries)

        #Генерация финального отчета
        report = self.generate_report(cluster_summaries)
        
        # Модифицирован для возврата результатов вместо печати
        return {
            #'important_words': important_words,
            'score': score,
            'cluster_summaries': cluster_summaries,
            'report': report,
        } 