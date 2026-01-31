def print_tree(node, feature_names, spacing=""):
    """
    Imprime a árvore de forma legível
    """
    if node.is_leaf():
        print(spacing + "Predição:", "Diabetes" if node.value == 1 else "Sem Diabetes")
        return
    
    print(spacing + f"Se {feature_names[node.feature]} <= {node.threshold:.2f}:")
    print_tree(node.left, feature_names, spacing + "  ")
    
    print(spacing + f"Senão ({feature_names[node.feature]} > {node.threshold:.2f}):")
    print_tree(node.right, feature_names, spacing + "  ")

# Usar
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

print("🌳 ESTRUTURA DA ÁRVORE:\n")
print_tree(tree.root, feature_names)