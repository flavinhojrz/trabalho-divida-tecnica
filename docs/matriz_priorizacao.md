# Matriz de Priorização

## Critério adotado

A priorização foi realizada considerando três fatores:

* Impacto da dívida técnica;
* Esforço necessário para corrigi-la;
* Juros (custo recorrente de manter a dívida).

Como critério de ordenação foi utilizada a seguinte expressão:

> **Prioridade = Impacto + Juros − Esforço**

Esse critério privilegia itens de alto impacto e alto custo recorrente que possam ser corrigidos com menor esforço.

---

## Ordem de prioridade

| Ordem | ID  | Justificativa                                                     |
| ----: | --- | ----------------------------------------------------------------- |
|     1 | D6  | Corrige um erro grave de regra de negócio e possui baixo esforço. |
|     2 | D8  | Elimina inconsistências na regra de cálculo de descontos.         |
|     3 | D13 | Facilita testes e melhora a estrutura do projeto.                 |
|     4 | D14 | Reduz risco de regressões futuras.                                |
|     5 | D7  | Evita encerramento inesperado da aplicação.                       |
|     6 | D1  | Remove configuração sensível do código.                           |
|     7 | D2  | Reduz acoplamento entre componentes.                              |
|     8 | D4  | Elimina potencial comportamento inesperado.                       |
|     9 | D9  | Torna regra de estoque configurável.                              |
|    10 | D12 | Melhora arquitetura do sistema.                                   |
|    11 | D15 | Melhora documentação do projeto.                                  |
|    12 | D3  | Melhora legibilidade.                                             |
|    13 | D11 | Completa funcionalidade pendente.                                 |
|    14 | D10 | Remove código morto.                                              |
|    15 | D5  | Remove importação não utilizada.                                  |

---

## Matriz Impacto × Esforço

|                   | Esforço Baixo                 | Esforço Alto     |
| ----------------- | ----------------------------- | ---------------- |
| **Impacto Alto**  | D1, D6, D8, D13               | D2, D7, D12, D14 |
| **Impacto Baixo** | D3, D4, D5, D9, D10, D11, D15 | Nenhum           |
