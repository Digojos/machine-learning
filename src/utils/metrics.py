import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(y_true, y_pred, dataset_name='Teste'):
    """
    Avalia o modelo e retorna métricas
    
    Parameters:
    -----------
    y_true : array-like
        Labels verdadeiros
    y_pred : array-like
        Predições do modelo
    dataset_name : str
        Nome do dataset (para display)
    
    Returns:
    --------
    dict : Dicionário com métricas
    """
    accuracy = accuracy_score(y_true, y_pred)
    
    print(f"\n📊 RESULTADOS ({dataset_name}):")
    print(f"Acurácia: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    return {
        'accuracy': accuracy,
        'confusion_matrix': confusion_matrix(y_true, y_pred)
    }


def plot_confusion_matrix(y_true, y_pred, class_names, save_path=None):
    """
    Plota matriz de confusão
    
    Parameters:
    -----------
    y_true : array-like
        Labels verdadeiros
    y_pred : array-like
        Predições do modelo
    class_names : list
        Nomes das classes
    save_path : str, optional
        Caminho para salvar a imagem
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names,
                yticklabels=class_names)
    plt.ylabel('Real')
    plt.xlabel('Predito')
    plt.title('Matriz de Confusão')
    
    if save_path:
        plt.savefig(save_path)
    plt.show()
