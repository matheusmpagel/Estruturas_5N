# Medindo o Efeito da Entrada no Desempenho

## 1. Objetivo

Este trabalho tem como objetivo comparar o desempenho de dois algoritmos
de ordenação: Insertion Sort e Merge Sort.

Os algoritmos serão testados utilizando dois tipos de entrada:
- listas aleatórias;
- listas já ordenadas.

A comparação busca observar como a organização dos dados de entrada
influencia o tempo de execução de cada algoritmo.

---

## 2. Algoritmos utilizados

### 2.1 Insertion Sort

O Insertion Sort é um algoritmo de ordenação que percorre a lista
gradualmente, inserindo cada elemento na posição correta em relação
aos elementos que já foram percorridos.

No código, o elemento atual é armazenado na variável `chave`.
Em seguida, os elementos maiores que essa chave são deslocados
uma posição para a direita até que seja encontrada a posição correta.

O algoritmo apresenta comportamento diferente dependendo da organização
da lista. Em uma lista já ordenada, poucos deslocamentos são necessários,
enquanto em uma lista aleatória podem ocorrer muitos deslocamentos.

---

### 2.2 Merge Sort

No Merge Sort, primeiramente, a lista é dividida em duas partes. Esse processo continua
recursivamente até que as partes tenham apenas um elemento. Depois,
as partes são combinadas novamente em ordem.

No código, a função `meSort` realiza a divisão da lista, enquanto
a função `juntar` combina as duas partes já ordenadas.

Diferentemente do Insertion Sort, o Merge Sort mantém um comportamento
mais estável independentemente de a entrada estar aleatória ou ordenada.

---

## 3. Geração das entradas

O arquivo `ListaRand.py` é responsável por gerar os dados utilizados
nos testes.

A função `listaRand()` gera uma lista com valores aleatórios.

Uma semente fixa (`seed = 42`) foi utilizada para que os testes possam
ser reproduzidos com os mesmos valores.

A função `listaOrd()` recebe uma lista aleatória e cria uma versão
ordenada dela. Dessa forma, a comparação entre os cenários utiliza
os mesmos valores, modificando apenas a ordem dos elementos.

---

## 4. Execução

Os arquivos `executadorInSort.py` e `executadorMeSort.py` executam os algoritmos
e medem o tempo utilizando `time.perf_counter()`.
