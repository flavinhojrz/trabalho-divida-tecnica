# 5. Roadmap de Quitação

Com base na matriz de priorização, foi elaborado um plano de quitação considerando o tempo disponível para manutenção do sistema e o impacto de cada item identificado.

## Pagar agora

### D6 – Falta de validação da quantidade vendida

Foi escolhido como prioridade máxima por representar um erro de regra de negócio. O sistema aceita vendas com quantidade negativa, gerando valores negativos e aumentando indevidamente o estoque.

**Critério de pronto**

* impedir vendas com quantidade menor ou igual a zero;
* impedir geração de valores negativos;
* impedir aumento do estoque durante uma venda.

---

### D7 – Falta de tratamento de entradas inválidas

Foi escolhido por comprometer diretamente a robustez da aplicação. Atualmente, qualquer entrada inválida para preço ou quantidade encerra o programa com uma exceção não tratada.

**Critério de pronto**

* tratar entradas inválidas utilizando tratamento de exceções;
* exibir mensagem de erro ao usuário;
* manter a aplicação em execução após o erro.

---

## Pagar depois

Os itens abaixo possuem impacto relevante, porém demandam maior tempo de implementação ou alterações estruturais.

* D8 – Unificar a regra de cálculo de descontos.
* D2 – Eliminar o uso da variável global `produtos`.
* D12 – Separar interface e regras de negócio.
* D13 – Alterar a inicialização do programa utilizando `if __name__ == "__main__":`.
* D14 – Desenvolver uma suíte completa de testes automatizados.

---

## Aceitar conscientemente

Os itens abaixo foram identificados como dívida técnica, porém apresentam baixo impacto imediato quando comparados às prioridades definidas para esta atividade.

* D1 – Senha fixa no código.
* D3 – Nome pouco descritivo da função `add`.
* D4 – Uso de parâmetro mutável como valor padrão.
* D5 – Importação não utilizada.
* D9 – Valor fixo para estoque baixo.
* D10 – Código comentado.
* D11 – Função `relatorio_vendas` não implementada.
* D15 – Documentação original limitada.

Esses itens permanecem registrados para futuras refatorações, mas não foram selecionados para quitação nesta etapa devido ao custo-benefício das correções prioritárias.
