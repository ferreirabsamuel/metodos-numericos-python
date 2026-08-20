# metodos-numericos-python
Implementações em Python de métodos de cálculo número: Regra de Simpson 1/3, Regra dos Trapézios e Derivação Numérica.

---

# Enunciado do Exercício
<img width="1270" height="427" alt="Captura de tela 2026-08-20 162002" src="https://github.com/user-attachments/assets/15382b8d-759a-41b2-a5e5-76d2be339d73" />

---

## Métodos de Cálculo Numérico em Python

Repositório dedicado a implementação em Python de métodos números afim de calcular a força do vento, onde a pressão varia ao longo da altura de uma passarela. O objetivo também consiste em encontrar a taxa de variação da pressão no ponto médio da torre. Vale destacar, que o passo (h) utilizado para a resolução deste desafio é 0.5, tendo em vista que a altura da passarela corresponde a 15 metros e a Regra de Simpson 1/3 exige que a quantidade de intervalos seja par para sua aplicação (considerando que cada metro de altura seja igual a um intervalo, por isso, foi preciso diminuir o passo e, consequentemente, espaçar o números de intervalos em um valor aplicável em todos os métodos.


---


## Métodos Implementados

### 1. Integração Numérica (Trapézios vs. Simpson 1/3):
**Regra dos Trapézios** Aproxima a área sob a curva acumulando a contribuição de 30 subintervalos.
**Regra de Simpson 1/3 Composta:** Aplica a interpolação por parábolas separando os pontos em índices pares e ímpares, alcançando o valor exato da integral da função cúbica.

### 2. Derivação Numérica
Cálculo da taxa de variação no ponto médio do domínio:
**Diferença Progressiva:** Utiliza os pontos z = 7.5 e z = 8.0.
**Diferença Regressiva:** Utiliza os pontos z = 7.0 e z = 7.5.
**Diferença Central:** Utiliza os pontos adjacentes z = 7.0 e z = 8.0 (maior ordem de precisão).


---


## Estrutura do Repositório

```text
├── derivacao.py      # Script com as 3 variações de Diferenças (Progressiva, Regressiva, Central)
├── trapezio.py       # Script com a Regra dos Trapézios Composta (n = 30)
├── simpson.py        # Script com a Regra de Simpson 1/3 Composta (n = 30)
└── README.md


