"""
Exemplo: Classificação de Diabetes usando Árvore de Decisão
Dataset: Pima Indians Diabetes Database
"""
import sys
sys.path.append('..')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from src.models import DecisionTree
from src.utils import evaluate_model, plot_confusion_matrix


def main():
    # Carregar dados
    print("📁 Carregando dados de diabetes...")
    df = pd.read_csv('../data/diabetes.csv')
    
    # Separar features e target
    X = df.drop('Outcome', axis=1).values
    y = df['Outcome'].values
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Treino: {X_train.shape}, Teste: {X_test.shape}")
    
    # Treinar o modelo
    print("\n🌲 Treinando Árvore de Decisão...")
    tree = DecisionTree(max_depth=5, min_samples_split=10, min_samples_leaf=5)
    tree.fit(X_train, y_train)
    
    # Fazer predições
    print("\n🔮 Fazendo predições...")
    y_pred_train = tree.predict(X_train)
    y_pred_test = tree.predict(X_test)
    
    # Avaliar
    evaluate_model(y_train, y_pred_train, 'Treino')
    evaluate_model(y_test, y_pred_test, 'Teste')
    
    print(f"\n📈 Relatório de Classificação (Teste):")
    print(classification_report(y_test, y_pred_test, 
                              target_names=['Sem Diabetes', 'Com Diabetes']))
    
    # Matriz de confusão
    plot_confusion_matrix(
        y_test, y_pred_test,
        class_names=['Sem Diabetes', 'Com Diabetes'],
        save_path='../outputs/diabetes_confusion_matrix.png'
    )


if __name__ == '__main__':
    main()
