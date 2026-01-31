import numpy as np
from collections import Counter

class Node:
    """
    Representa um nó na árvore de decisão
    """
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature      # Índice da feature usada para dividir
        self.threshold = threshold  # Valor de corte
        self.left = left           # Subárvore esquerda
        self.right = right         # Subárvore direita
        self.value = value         # Valor para nó folha (classe predita)
    
    def is_leaf(self):
        """Verifica se é um nó folha"""
        return self.value is not None


class DecisionTree:
    """
    Árvore de Decisão para Classificação
    """
    def __init__(self, max_depth=10, min_samples_split=2, min_samples_leaf=1):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.root = None
    
    def fit(self, X, y):
        """
        Treina a árvore de decisão
        
        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Features de treino
        y : array-like, shape (n_samples,)
            Labels de treino
        """
        self.n_classes = len(np.unique(y))
        self.n_features = X.shape[1]
        self.root = self._grow_tree(X, y)
    
    def _grow_tree(self, X, y, depth=0):
        """
        Constrói a árvore recursivamente
        """
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))
        
        # Critérios de parada
        if (depth >= self.max_depth or 
            n_labels == 1 or 
            n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
        
        # Encontrar a melhor divisão
        best_feature, best_threshold = self._best_split(X, y)
        
        # Se não encontrou divisão válida
        if best_feature is None:
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
        
        # Dividir os dados
        left_indices = X[:, best_feature] <= best_threshold
        right_indices = X[:, best_feature] > best_threshold
        
        # Verificar min_samples_leaf
        if (np.sum(left_indices) < self.min_samples_leaf or 
            np.sum(right_indices) < self.min_samples_leaf):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
        
        # Criar subárvores recursivamente
        left = self._grow_tree(X[left_indices], y[left_indices], depth + 1)
        right = self._grow_tree(X[right_indices], y[right_indices], depth + 1)
        
        return Node(best_feature, best_threshold, left, right)
    
    def _best_split(self, X, y):
        """
        Encontra a melhor divisão usando ganho de informação
        """
        best_gain = -1
        best_feature = None
        best_threshold = None
        
        for feature_idx in range(self.n_features):
            X_column = X[:, feature_idx]
            thresholds = np.unique(X_column)
            
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_idx
                    best_threshold = threshold
        
        return best_feature, best_threshold
    
    def _information_gain(self, y, X_column, threshold):
        """
        Calcula o ganho de informação de uma divisão
        """
        # Entropia do pai
        parent_entropy = self._entropy(y)
        
        # Dividir
        left_indices = X_column <= threshold
        right_indices = X_column > threshold
        
        if np.sum(left_indices) == 0 or np.sum(right_indices) == 0:
            return 0
        
        # Calcular entropia ponderada dos filhos
        n = len(y)
        n_left, n_right = np.sum(left_indices), np.sum(right_indices)
        e_left, e_right = self._entropy(y[left_indices]), self._entropy(y[right_indices])
        child_entropy = (n_left / n) * e_left + (n_right / n) * e_right
        
        # Ganho de informação
        information_gain = parent_entropy - child_entropy
        return information_gain
    
    def _entropy(self, y):
        """
        Calcula a entropia
        """
        proportions = np.bincount(y) / len(y)
        entropy = -np.sum([p * np.log2(p) for p in proportions if p > 0])
        return entropy
    
    def _most_common_label(self, y):
        """
        Retorna a label mais comum
        """
        counter = Counter(y)
        return counter.most_common(1)[0][0]
    
    def predict(self, X):
        """
        Faz predições para novos dados
        
        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Dados para predição
        
        Returns:
        --------
        predictions : array, shape (n_samples,)
            Classes preditas
        """
        return np.array([self._traverse_tree(x, self.root) for x in X])
    
    def _traverse_tree(self, x, node):
        """
        Percorre a árvore para fazer uma predição
        """
        if node.is_leaf():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)
