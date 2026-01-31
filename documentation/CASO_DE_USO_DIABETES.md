# 🏥 CASO DE USO: Previsão de Diabetes

---

## 🎯 1. O QUE É O CASO DE USO?

### Definição:
```
Desenvolver um sistema de Machine Learning que consiga 
prever se uma pessoa tem diabetes ou não, baseado em 
dados de exames médicos e características pessoais.
```

### Contexto Real:

Imagine que você trabalha em uma clínica médica. Todos os dias chegam pacientes fazendo exames de rotina. O médico precisa avaliar se há risco de diabetes.

**Problema atual:**
- ❌ Diagnóstico depende apenas da experiência do médico
- ❌ Pode demorar para identificar padrões
- ❌ Alguns sinais sutis podem passar despercebidos

**Solução com ML:**
- ✅ Sistema auxilia o médico com uma predição rápida
- ✅ Identifica padrões em milhares de casos históricos
- ✅ Alerta precoce para casos de risco
- ✅ Médico toma decisão final, mas com apoio de dados

---

## 👥 2. QUEM USA ESTE SISTEMA?

### Usuários:
- 🩺 **Médicos** - Para triagem rápida
- 🏥 **Hospitais** - Para análise de risco em pacientes
- 📊 **Pesquisadores** - Para estudar fatores de risco
- 💊 **Planos de Saúde** - Para programas preventivos

### Benefícios:
- Diagnóstico mais rápido
- Redução de custos com tratamentos tardios
- Intervenção precoce
- Melhora na qualidade de vida dos pacientes

---

## 📊 3. AS FEATURES (Características de Entrada)

Features são as **informações que o modelo recebe** para fazer a predição. São os dados que você coleta do paciente.

### Lista Completa das 8 Features:

---

### Feature 1: Pregnancies (Gestações)
```
📋 Descrição: Número de vezes que a paciente esteve grávida
🔢 Tipo: Numérica (inteiro)
📈 Faixa: 0 a 17
💡 Por quê é importante?
   - Diabetes gestacional é fator de risco
   - Múltiplas gestações podem afetar metabolismo
   - Mudanças hormonais impactam glicose
```

**Exemplo:**
```
Paciente A: 0 gestações  (menor risco)
Paciente B: 3 gestações  (risco moderado)
Paciente C: 10 gestações (maior risco)
```

---

### Feature 2: Glucose (Glicose)
```
📋 Descrição: Concentração de glicose no plasma após 2h 
              de teste oral de tolerância à glicose
🔢 Tipo: Numérica (inteiro)
📈 Faixa: 0 a 199 mg/dL
💡 Por quê é importante?
   - Principal indicador de diabetes
   - Valores altos = resistência à insulina
   - Feature mais importante do modelo!
```

**Interpretação Médica:**
```
< 140 mg/dL   → Normal ✅
140-199 mg/dL → Pré-diabetes ⚠️
≥ 200 mg/dL   → Diabetes 🔴
```

**Exemplo:**
```
Paciente A: 85 mg/dL   (saudável)
Paciente B: 148 mg/dL  (limiar de risco)
Paciente C: 183 mg/dL  (alto risco)
```

---

### Feature 3: BloodPressure (Pressão Arterial)
```
📋 Descrição: Pressão arterial diastólica (mmHg)
🔢 Tipo: Numérica (inteiro)
📈 Faixa: 0 a 122 mmHg
💡 Por quê é importante?
   - Diabetes e hipertensão frequentemente coexistem
   - Pressão alta danifica vasos sanguíneos
   - Indicador de saúde cardiovascular
```

**Interpretação Médica:**
```
< 80 mmHg   → Normal ✅
80-89 mmHg  → Pré-hipertensão ⚠️
≥ 90 mmHg   → Hipertensão 🔴
```

**Exemplo:**
```
Paciente A: 66 mmHg  (normal)
Paciente B: 72 mmHg  (normal)
Paciente C: 92 mmHg  (hipertensão)
```

---

### Feature 4: SkinThickness (Espessura da Pele)
```
📋 Descrição: Espessura da dobra cutânea do tríceps (mm)
🔢 Tipo: Numérica (inteiro)
📈 Faixa: 0 a 99 mm
💡 Por quê é importante?
   - Indicador indireto de gordura corporal
   - Obesidade é fator de risco para diabetes
   - Relacionado com resistência à insulina
```

**Exemplo:**
```
Paciente A: 20 mm  (baixa)
Paciente B: 35 mm  (média)
Paciente C: 50 mm  (alta - maior risco)
```

---

### Feature 5: Insulin (Insulina)
```
📋 Descrição: Nível de insulina sérica em 2 horas (µU/ml)
🔢 Tipo: Numérica (inteiro)
📈 Faixa: 0 a 846 µU/ml
💡 Por quê é importante?
   - Insulina regula glicose no sangue
   - Valores anormais indicam resistência
   - Diabetes tipo 2 = corpo não usa insulina corretamente
```

**Interpretação:**
```
Valores muito baixos  → Pouca produção
Valores muito altos   → Resistência à insulina
```

**Exemplo:**
```
Paciente A: 0 µU/ml    (pode ter dados faltantes)
Paciente B: 94 µU/ml   (normal)
Paciente C: 300 µU/ml  (resistência)
```

---

### Feature 6: BMI (Índice de Massa Corporal)
```
📋 Descrição: Peso (kg) / (Altura (m))²
🔢 Tipo: Numérica (decimal)
📈 Faixa: 0 a 67.1
💡 Por quê é importante?
   - Obesidade é principal fator de risco
   - IMC alto = maior chance de diabetes tipo 2
   - Relacionado com estilo de vida
```

**Interpretação Médica:**
```
< 18.5      → Abaixo do peso
18.5 - 24.9 → Peso normal ✅
25.0 - 29.9 → Sobrepeso ⚠️
≥ 30.0      → Obesidade 🔴
```

**Exemplo:**
```
Paciente A: 22.5  (peso normal)
Paciente B: 33.6  (obesidade - risco)
Paciente C: 43.1  (obesidade severa - alto risco)
```

---

### Feature 7: DiabetesPedigreeFunction (Função de Histórico Familiar)
```
📋 Descrição: Score que indica histórico familiar de diabetes
🔢 Tipo: Numérica (decimal)
📈 Faixa: 0.078 a 2.42
💡 Por quê é importante?
   - Genética tem papel importante
   - Histórico familiar aumenta risco
   - Combina idade e relação dos familiares com diabetes
```

**Como funciona:**
```
Valor baixo (0.1-0.3)  → Pouco histórico familiar
Valor médio (0.3-0.8)  → Histórico moderado
Valor alto (>0.8)      → Forte histórico familiar
```

**Exemplo:**
```
Paciente A: 0.127  (baixo histórico)
Paciente B: 0.627  (histórico moderado)
Paciente C: 1.500  (forte histórico - alto risco)
```

---

### Feature 8: Age (Idade)
```
📋 Descrição: Idade do paciente em anos
🔢 Tipo: Numérica (inteiro)
📈 Faixa: 21 a 81 anos
💡 Por quê é importante?
   - Risco aumenta com a idade
   - Diabetes tipo 2 mais comum após 45 anos
   - Metabolismo muda com envelhecimento
```

**Faixas de Risco:**
```
21-35 anos → Risco baixo
35-50 anos → Risco moderado ⚠️
> 50 anos  → Risco aumentado 🔴
```

**Exemplo:**
```
Paciente A: 25 anos  (jovem - menor risco)
Paciente B: 47 anos  (meia-idade - risco moderado)
Paciente C: 65 anos  (idoso - maior risco)
```

---

## 🎯 4. O TARGET (O que queremos prever)

### Target: Outcome (Resultado)

```
📋 Descrição: Indica se o paciente tem diabetes
🔢 Tipo: Categórica binária
📈 Valores possíveis: 
   - 0 = Não tem diabetes ✅
   - 1 = Tem diabetes 🔴
```

### Distribuição no Dataset:
```
Total de pacientes: 768

Sem Diabetes (0): 500 pacientes (65%)
Com Diabetes (1): 268 pacientes (35%)
```

**Este é um problema de CLASSIFICAÇÃO BINÁRIA**

---

## 📋 5. EXEMPLOS COMPLETOS DE PACIENTES

### Exemplo 1: Paciente COM Diabetes
```python
Features:
  Pregnancies:              6    (múltiplas gestações)
  Glucose:                  148  (alto! > 140)
  BloodPressure:            72   (normal)
  SkinThickness:            35   (médio)
  Insulin:                  0    (dado faltante)
  BMI:                      33.6 (obesidade)
  DiabetesPedigreeFunction: 0.627 (histórico familiar)
  Age:                      50   (idade de risco)
  
Target: 1 (TEM DIABETES) 🔴

🔍 Análise:
- Glicose elevada (principal indicador)
- Obesidade (IMC > 30)
- Histórico familiar presente
- Idade de risco
→ Modelo deve prever: 1
```

---

### Exemplo 2: Paciente SEM Diabetes
```python
Features:
  Pregnancies:              1    (poucas gestações)
  Glucose:                  85   (normal!)
  BloodPressure:            66   (normal)
  SkinThickness:            29   (normal)
  Insulin:                  0    (dado faltante)
  BMI:                      26.6 (levemente acima)
  DiabetesPedigreeFunction: 0.351 (baixo histórico)
  Age:                      31   (jovem)
  
Target: 0 (NÃO TEM DIABETES) ✅

🔍 Análise:
- Glicose normal (< 100)
- IMC apenas levemente elevado
- Jovem
- Sem forte histórico familiar
→ Modelo deve prever: 0
```

---

### Exemplo 3: Paciente COM Diabetes (Caso Severo)
```python
Features:
  Pregnancies:              8    (muitas gestações)
  Glucose:                  183  (muito alto!)
  BloodPressure:            64   (normal)
  SkinThickness:            0    (dado faltante)
  Insulin:                  0    (dado faltante)
  BMI:                      23.3 (normal)
  DiabetesPedigreeFunction: 0.672 (histórico presente)
  Age:                      32   (relativamente jovem)
  
Target: 1 (TEM DIABETES) 🔴

🔍 Análise:
- Glicose MUITO elevada (183!)
- Apesar de IMC normal e idade jovem
- Histórico familiar + gestações
→ Glicose é fator decisivo aqui
```

---

## 🎯 6. COMO O MODELO USA ISSO?

### Fluxo Completo:

```
1. ENTRADA (Features de um novo paciente)
   ↓
   [6, 148, 72, 35, 0, 33.6, 0.627, 50]
   
2. MODELO TREINADO analisa
   ↓
   "Glicose = 148 é > 140? SIM → risco"
   "BMI = 33.6 é > 30? SIM → risco"
   "Idade = 50 é > 45? SIM → risco"
   "Histórico = 0.627 é alto? MODERADO"
   
3. DECISÃO da Árvore
   ↓
   Seguindo os nós:
   - Se Glucose > 127.5 → Direita
   - Se BMI > 29.9 → Direita
   - Se Age > 28.5 → Direita
   
4. SAÍDA (Predição)
   ↓
   Predição: 1 (TEM DIABETES)
   Confiança: Alta
```

---

## 📊 7. VISUALIZAÇÃO DO DATASET

```
┌───────────┬─────────┬──────────┬──────────┬─────────┬──────┬─────────┬─────┬─────────┐
│Pregnancies│ Glucose │   BP     │   Skin   │ Insulin │ BMI  │ Pedigree│ Age │ Outcome │
├───────────┼─────────┼──────────┼──────────┼─────────┼──────┼─────────┼─────┼─────────┤
│     6     │   148   │    72    │    35    │    0    │ 33.6 │  0.627  │  50 │    1    │
│     1     │    85   │    66    │    29    │    0    │ 26.6 │  0.351  │  31 │    0    │
│     8     │   183   │    64    │     0    │    0    │ 23.3 │  0.672  │  32 │    1    │
│     1     │    89   │    66    │    23    │   94    │ 28.1 │  0.167  │  21 │    0    │
│     0     │   137   │    40    │    35    │  168    │ 43.1 │  2.288  │  33 │    1    │
│    ...    │   ...   │   ...    │   ...    │   ...   │ ...  │   ...   │ ... │   ...   │
└───────────┴─────────┴──────────┴──────────┴─────────┴──────┴─────────┴─────┴─────────┘
   ↑                                  ↑                                            ↑
   └──────────────────────────────────┴────────────────────────────────────────────┘
              FEATURES (X)                                                    TARGET (y)
           O que o modelo VÊ                                          O que o modelo APRENDE
```

---

## ✅ 8. RESUMO EXECUTIVO

### Caso de Uso:
```
Prever diabetes em pacientes usando dados médicos históricos
```

### Features (8 variáveis de entrada):
```
1. Pregnancies              → Número de gestações
2. Glucose                  → Glicose no sangue (MAIS IMPORTANTE!)
3. BloodPressure            → Pressão arterial
4. SkinThickness            → Espessura da pele
5. Insulin                  → Nível de insulina
6. BMI                      → Índice de massa corporal
7. DiabetesPedigreeFunction → Histórico familiar
8. Age                      → Idade
```

### Target (1 variável de saída):
```
Outcome → 0 (Sem diabetes) ou 1 (Com diabetes)
```

### Objetivo do Modelo:
```
Aprender padrões nos dados históricos de 768 pacientes
para prever corretamente o diagnóstico de NOVOS pacientes
```

---

## 🔗 9. REFERÊNCIAS

### Dataset Original:
- **Nome**: Pima Indians Diabetes Database
- **Fonte**: National Institute of Diabetes and Digestive and Kidney Diseases
- **URL**: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

### Informações Médicas:
- **Diabetes Tipo 2**: Doença metabólica caracterizada por hiperglicemia
- **Fatores de Risco**: Obesidade, sedentarismo, histórico familiar, idade
- **Diagnóstico**: Glicemia de jejum, teste oral de tolerância à glicose

---

## 📚 10. PRÓXIMOS PASSOS

Agora que você entende completamente o caso de uso, você pode:

1. ✅ **Implementar a árvore de decisão** - Criar o algoritmo do zero
2. ✅ **Treinar o modelo** - Usar os dados para aprender padrões
3. ✅ **Avaliar performance** - Medir acurácia, precisão, recall
4. ✅ **Interpretar resultados** - Entender as decisões do modelo
5. ✅ **Visualizar a árvore** - Ver as regras criadas
6. ✅ **Fazer predições** - Usar em novos pacientes

---

## 📞 CONTATO E SUPORTE

Este documento foi criado como material educacional para o projeto de Machine Learning de Árvore de Decisão.

**Autor**: Copilot AI  
**Data**: 2026-01-31  
**Versão**: 1.0  

---

**Bons estudos! 🚀📊🏥**