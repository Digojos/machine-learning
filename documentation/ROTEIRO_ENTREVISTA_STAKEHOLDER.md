# 🗣️ Roteiro de Entrevista com Stakeholders Não-Técnicos

**Objetivo:** Levantar requisitos para projeto de Machine Learning em saúde  
**Duração:** 60-90 minutos  
**Data:** ____________  
**Entrevistado:** ____________  
**Cargo/Função:** ____________

---

## 🎯 Estratégia Geral de Comunicação

### Princípios:

- ❌ **NÃO use jargão técnico**: "features", "target", "overfitting"
- ✅ **USE termos clínicos**: "informações do paciente", "resultado esperado", "variáveis"
- ✅ **Faça analogias**: Compare com processos que eles já conhecem
- ✅ **Mostre exemplos visuais**: Tabelas, planilhas
- ✅ **Valide constantemente**: "Entendi corretamente que...?"

---

## 📋 PARTE 1: APRESENTAÇÃO E CONTEXTO (10 min)

### Abertura

```
"Olá Dr(a). [Nome], obrigado por disponibilizar seu tempo. 

Estou desenvolvendo uma ferramenta computacional para auxiliar no 
[OBJETIVO DO PROJETO]. Para isso, preciso entender melhor como vocês 
trabalham hoje e quais informações são mais relevantes para [DECISÃO CLÍNICA].

Vou fazer algumas perguntas sobre os dados dos pacientes e o processo 
de diagnóstico/tratamento. Pode ficar à vontade para usar termos 
médicos - vou anotar e pesquisar depois se precisar.

Tudo bem se eu gravar nossa conversa para não perder nenhum detalhe?"
```

**[ ] Permissão para gravar concedida**

---

## 📊 PARTE 2: ENTENDENDO O PROBLEMA (15 min)

### 2.1 Objetivo Clínico

#### Pergunta 1: Qual decisão clínica você precisa tomar neste caso?

```
Resposta:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Exemplos de resposta esperada:**
- Diagnosticar se o paciente tem a doença X
- Classificar a gravidade do caso (leve, moderado, grave)
- Prever se o paciente vai responder bem ao tratamento Y
- Identificar risco de complicação Z

---

#### Pergunta 2: Como vocês fazem essa avaliação hoje?

```
Processo atual:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

Tempo necessário: _______________

Taxa de acerto estimada: ___________%
```

---

#### Pergunta 3: Qual seria um resultado útil para vocês?

```
Resposta:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Marque o tipo de resultado esperado:**

- [ ] **Binário** (Sim/Não, Tem/Não tem, Alto Risco/Baixo Risco)
- [ ] **Multiclasse** (Leve/Moderado/Grave, Tipo A/B/C)
- [ ] **Contínuo** (Score de 0-100, Probabilidade)

**🎯 Tradução Técnica:**
```
TARGET (variável a prever): _______________________________
Tipo de problema: [ ] Classificação binária  [ ] Multiclasse  [ ] Regressão
```

---

## 📝 PARTE 3: IDENTIFICANDO AS INFORMAÇÕES (20 min)

### 3.1 Informações Disponíveis

#### Pergunta 4: Quais informações vocês coletam de cada paciente?

**Incentive a listar TUDO. Use o checklist abaixo:**

#### CHECKLIST DE INFORMAÇÕES DO PACIENTE

**DADOS DEMOGRÁFICOS:**
- [ ] Idade
- [ ] Sexo/Gênero
- [ ] Peso
- [ ] Altura
- [ ] IMC (calculado)
- [ ] Etnia/Raça
- [ ] Outro: _______________

**HISTÓRICO MÉDICO:**
- [ ] Doenças prévias
- [ ] Histórico familiar
- [ ] Cirurgias anteriores
- [ ] Alergias
- [ ] Medicações atuais
- [ ] Tempo de diagnóstico
- [ ] Outro: _______________

**EXAMES LABORATORIAIS:**
- [ ] Hemograma completo
- [ ] Glicemia
- [ ] Colesterol (LDL, HDL, Total)
- [ ] Triglicerídeos
- [ ] Ureia/Creatinina
- [ ] Enzimas hepáticas
- [ ] Outro: _______________

**SINAIS VITAIS:**
- [ ] Pressão arterial (sistólica/diastólica)
- [ ] Frequência cardíaca
- [ ] Temperatura
- [ ] Saturação de O2
- [ ] Frequência respiratória
- [ ] Outro: _______________

**SINTOMAS CLÍNICOS:**
- [ ] Dor (escala 0-10)
- [ ] Fadiga (sim/não ou escala)
- [ ] Febre (sim/não ou temperatura)
- [ ] Outro: _______________

**EXAMES DE IMAGEM:**
- [ ] Raio-X (laudos textuais)
- [ ] Tomografia (laudos)
- [ ] Ressonância (laudos)
- [ ] Ultrassom (laudos)
- [ ] Outro: _______________

---

#### Pergunta 5: Vocês já têm essas informações em algum sistema?

- [ ] Sim, em sistema eletrônico → Qual? _______________
- [ ] Sim, em planilhas (Excel/Google Sheets)
- [ ] Parcialmente (alguns em papel, alguns digitalizados)
- [ ] Não, tudo em papel

---

#### Pergunta 6: Dessas informações, quais vocês consideram mais importantes para tomar essa decisão?

```
Top 5 informações mais relevantes:

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
4. _________________________________________________________________
5. _________________________________________________________________
```

---

### 3.2 Mostre Exemplo Visual

**IMPORTANTE:** Mostre uma tabela exemplo e pergunte:

```
"As informações ficariam organizadas assim, cada linha é um paciente:"

┌─────┬──────┬────────┬──────────┬────────────┬──────────┐
│ ID  │ Idade│ Sexo   │ Glicose  │ Pressão    │ Resultado│
├─────┼──────┼────────┼──────────┼────────────┼──────────┤
│ 001 │  45  │   F    │   110    │   120/80   │   Não    │
│ 002 │  52  │   M    │   180    │   140/90   │   Sim    │
│ 003 │  38  │   F    │   95     │   110/70   │   Não    │
└─────┴──────┴────────┴──────────┴────────────┴──────────┘

"Faz sentido? Que outras colunas precisaríamos?"
```

**Feedback:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📋 PARTE 4: DICIONÁRIO DE DADOS (Detalhamento)

### Para CADA informação identificada, preencha:

---

### Variável 1: ___________________________

| Aspecto                  | Descrição                                    |
|--------------------------|----------------------------------------------|
| **Nome no sistema**      |                                              |
| **Tipo**                 | [ ] Numérico  [ ] Categórico  [ ] Texto      |
| **Unidade** (se numérico)|                                              |
| **Faixa de valores**     | Mínimo: _______ Máximo: _______             |
| **Valores normais**      |                                              |
| **Valores críticos**     |                                              |
| **Sempre disponível?**   | [ ] Sim  [ ] Não                            |
| **Se não, % faltante**   | _______%                                     |
| **Como preencher falta** |                                              |
| **Categorias** (se aplicável) |                                         |
| **Observações**          |                                              |

**Pergunta:** Como essa informação é registrada?
```
_________________________________________________________________
```

**Pergunta:** Qual a faixa de valores normais?
```
_________________________________________________________________
```

**Pergunta:** Essa informação está sempre disponível? Se não, com que frequência falta?
```
_________________________________________________________________
```

---

### Variável 2: ___________________________

| Aspecto                  | Descrição                                    |
|--------------------------|----------------------------------------------|
| **Nome no sistema**      |                                              |
| **Tipo**                 | [ ] Numérico  [ ] Categórico  [ ] Texto      |
| **Unidade** (se numérico)|                                              |
| **Faixa de valores**     | Mínimo: _______ Máximo: _______             |
| **Valores normais**      |                                              |
| **Valores críticos**     |                                              |
| **Sempre disponível?**   | [ ] Sim  [ ] Não                            |
| **Se não, % faltante**   | _______%                                     |
| **Como preencher falta** |                                              |
| **Categorias** (se aplicável) |                                         |
| **Observações**          |                                              |

---

**💡 REPETIR para TODAS as variáveis identificadas**

---

## 📊 PARTE 5: ENTENDENDO A AMOSTRA DE DADOS (15 min)

### 5.1 Tamanho e Disponibilidade

#### Pergunta 7: Quantos pacientes vocês já atenderam com esse perfil?

```
Total de pacientes: _______________
```

**🎯 Nota técnica:**
- Mínimo: 100-200 para modelo simples
- Ideal: 1000+

---

#### Pergunta 8: Desses pacientes, para quantos vocês têm todas essas informações completas?

```
Pacientes com dados completos: _______________
```

---

#### Pergunta 9: Esses dados já estão digitalizados/organizados?

- [ ] Sim, em sistema eletrônico
- [ ] Sim, em planilhas
- [ ] Parcialmente (alguns em papel)
- [ ] Não, tudo em papel

---

#### Pergunta 10: Há pacientes de diferentes períodos? Quando foram atendidos?

```
Período de coleta: ____________ a ____________
```

---

#### Pergunta 11: Esses pacientes são de uma única instituição ou várias?

```
Origem dos dados:
- [ ] Hospital: _______________________
- [ ] Clínica: ________________________
- [ ] Ambulatório: ____________________
- [ ] Múltiplas fontes
```

---

### 5.2 Distribuição do Resultado (TARGET)

#### Pergunta 12: Desses pacientes, quantos tiveram cada resultado?

```
Distribuição:

Classe 0 (ex: Sem doença):   ______ pacientes (____%)
Classe 1 (ex: Com doença):   ______ pacientes (____%)
Classe 2 (se aplicável):     ______ pacientes (____%)
```

**💡 Nota:** Se uma classe < 20%: Dataset desbalanceado!

---

### 5.3 Qualidade dos Dados

#### Pergunta 13: Há informações que frequentemente estão faltando?

```
_________________________________________________________________
_________________________________________________________________
```

---

#### Pergunta 14: Há casos onde o diagnóstico/resultado foi incerto?

```
_________________________________________________________________
_________________________________________________________________
```

---

#### Pergunta 15: Os dados foram coletados por diferentes profissionais?

- [ ] Sim → Quais? _______________
- [ ] Não → Por quem? _______________

---

#### Pergunta 16: Houve mudanças nos protocolos de coleta ao longo do tempo?

```
_________________________________________________________________
_________________________________________________________________
```

---

#### Pergunta 17: Há pacientes duplicados ou registros inconsistentes?

```
_________________________________________________________________
_________________________________________________________________
```

---

## 🎯 PARTE 6: VALIDAÇÃO E EXPECTATIVAS (10 min)

### 6.1 Critérios de Sucesso

#### Pergunta 18: Qual seria uma taxa de acerto aceitável para essa ferramenta?

**Explique:** "Se de 100 casos, quantos a ferramenta precisa acertar para ser útil?"

```
Taxa de acerto mínima esperada: ______%
```

**Guia de interpretação:**
- 70-80%: Bom para triagem
- 80-90%: Bom para apoio à decisão
- 90%+: Excelente (mas difícil)

---

#### Pergunta 19: O que é mais importante?

**Explique a diferença:**
- **Sensibilidade**: Não deixar passar casos positivos (detectar quem TEM)
- **Especificidade**: Não gerar alarmes falsos (detectar quem NÃO TEM)

**Marque a prioridade:**

- [ ] **PRIORIZAR sensibilidade** (não deixar passar casos positivos)
- [ ] **PRIORIZAR especificidade** (evitar alarmes falsos)
- [ ] **BALANCEAR ambos**

**Justificativa:**
```
_________________________________________________________________
_________________________________________________________________
```

---

#### Pergunta 20: Qual tipo de erro seria mais problemático?

- [ ] **Falso Negativo**: Dizer que NÃO tem, mas tem (paciente não recebe tratamento)
- [ ] **Falso Positivo**: Dizer que TEM, mas não tem (alarme falso, tratamento desnecessário)

**Explicação:**
```
_________________________________________________________________
_________________________________________________________________
```

---

#### Pergunta 21: A ferramenta vai substituir a avaliação médica ou apenas auxiliar?

- [ ] **Apenas auxiliar** (médico sempre revisa)
- [ ] **Substituir em casos simples** (médico revisa apenas casos complexos)
- [ ] **Outro**: _______________

---

## ⚖️ PARTE 7: ASPECTOS ÉTICOS E LEGAIS (10 min)

### 7.1 Conformidade Ética

#### Pergunta 22: Os pacientes autorizaram o uso dos dados para pesquisa?

- [ ] Sim, há TCLE (Termo de Consentimento Livre e Esclarecido)
- [ ] Sim, autorização verbal
- [ ] Não, mas não contém dados identificáveis
- [ ] Não sei

**Detalhes:**
```
_________________________________________________________________
_________________________________________________________________
```

---

#### Pergunta 23: Os dados estão anonimizados?

- [ ] Sim, completamente (sem nomes, CPF, etc.)
- [ ] Parcialmente (códigos no lugar de nomes)
- [ ] Não, contém dados identificáveis

**O que foi removido/mascarado:**
```
_________________________________________________________________
```

---

#### Pergunta 24: Há aprovação de comitê de ética?

- [ ] Sim → Protocolo nº: _______________
- [ ] Em andamento
- [ ] Não aplicável
- [ ] Não sei

---

#### Pergunta 25: Posso ter acesso aos dados? Como será o processo?

**Requisitos:**
- [ ] Termo de confidencialidade
- [ ] Autorização formal
- [ ] Dados já desidentificados
- [ ] Outro: _______________

**Prazo de entrega:** _______________

---

#### Pergunta 26: Há restrições de uso ou compartilhamento?

```
_________________________________________________________________
_________________________________________________________________
```

---

## 🚀 PARTE 8: LOGÍSTICA E PRÓXIMOS PASSOS (10 min)

### 8.1 Entrega dos Dados

#### Pergunta 27: Como vou receber os dados?

**Formato:**
- [ ] CSV (Excel separado por vírgulas)
- [ ] XLSX (Excel)
- [ ] Banco de dados → Qual? _______________
- [ ] Outro: _______________

**Via de entrega:**
- [ ] E-mail
- [ ] Link para download (Google Drive, OneDrive, etc.)
- [ ] Acesso direto ao sistema
- [ ] Outro: _______________

**Prazo:** _______________

---

### 8.2 Comunicação

#### Pergunta 28: Quem mais preciso conversar?

```
Outros profissionais da equipe:

Nome: _________________________ Função: _________________________
Nome: _________________________ Função: _________________________
Nome: _________________________ Função: _________________________
```

---

#### Pergunta 29: Como prefere receber os resultados?

- [ ] Relatório técnico (PDF)
- [ ] Apresentação (PowerPoint)
- [ ] Sistema/dashboard interativo
- [ ] Reunião presencial
- [ ] Outro: _______________

---

#### Pergunta 30: Podemos agendar um próximo encontro para eu mostrar os primeiros resultados?

**Data proposta:** _______________
**Formato:** [ ] Presencial  [ ] Online

---

## ✅ CHECKLIST FINAL

Antes de encerrar, confirme que tem:

- [ ] **OBJETIVO CLÍNICO** claro e documentado
- [ ] **LISTA COMPLETA** de informações (features)
- [ ] **DETALHAMENTO** de cada variável (tipo, faixa, unidade)
- [ ] **TARGET** bem definido (binário/multiclasse)
- [ ] **TAMANHO** da amostra (número de pacientes)
- [ ] **DISTRIBUIÇÃO** das classes (balanceado?)
- [ ] **FORMATO** dos dados (como vai receber)
- [ ] **QUALIDADE** esperada (missing values, erros)
- [ ] **CRITÉRIOS** de sucesso (acurácia mínima)
- [ ] **PRIORIDADES** (sensibilidade vs especificidade)
- [ ] **ASPECTOS ÉTICOS** (aprovação, anonimização)
- [ ] **PRÓXIMOS PASSOS** agendados

---

## 📋 RESUMO EXECUTIVO

Preencher após a entrevista:

### Objetivo do Projeto
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

### Target (O que vamos prever)
```
Nome da variável: _______________________
Tipo: [ ] Binário  [ ] Multiclasse
Classes: _______________________________
```

### Features Principais (Top 5)
```
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
4. _________________________________________________________________
5. _________________________________________________________________
```

### Tamanho da Amostra
```
Total de pacientes: _______________
Com dados completos: _______________
Período: ____________ a ____________
```

### Requisitos de Performance
```
Acurácia mínima: ______%
Sensibilidade mínima: ______%
Prioridade: [ ] Sensibilidade  [ ] Especificidade  [ ] Balanceado
```

### Aspectos Éticos
```
TCLE: [ ] Sim  [ ] Não
Dados anonimizados: [ ] Sim  [ ] Não
Comitê de ética: [ ] Aprovado  [ ] Em andamento  [ ] N/A
```

### Próximos Passos
```
1. Receber dados até: _______________
2. Análise exploratória: _______________
3. Primeira apresentação: _______________
```

---

## 💡 FRASES ÚTEIS DURANTE A ENTREVISTA

Use estas frases para facilitar a comunicação:

- "Deixa eu ver se entendi corretamente..."
- "Você poderia me dar um exemplo disso?"
- "Como isso funciona na prática?"
- "E se [situação X] acontecer?"
- "Isso é sempre assim ou pode variar?"
- "Entendi. E qual a frequência disso?"
- "Há alguma exceção ou caso especial?"

---

## ⚠️ RED FLAGS (Sinais de Alerta)

Fique atento se ouvir:

- ⚠️ "Temos poucos dados, mas achamos que dá..."
- ⚠️ "Não sabemos exatamente quantos casos temos..."
- ⚠️ "Os dados estão meio bagunçados..."
- ⚠️ "Não tem aprovação de ética, mas não tem problema..."
- ⚠️ "Queremos 99% de acerto..."
- ⚠️ "Os dados têm muitas inconsistências..."
- ⚠️ "Não podemos dar acesso aos dados agora..."

**Se ouvir alguma dessas frases, investigue mais profundamente!**

---

## 📝 OBSERVAÇÕES ADICIONAIS

Use este espaço para anotações extras:

```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## 📧 INFORMAÇÕES DE CONTATO

**Entrevistado:**
- Nome: _______________________
- E-mail: _______________________
- Telefone: _______________________
- Instituição: _______________________

**Entrevistador:**
- Nome: _______________________
- E-mail: _______________________
- Data da entrevista: _______________________

---

**Documento gerado em:** {{ data atual }}  
**Versão:** 1.0  
**Status:** [ ] Rascunho  [ ] Revisado  [ ] Aprovado
