# Classificação da Dívida Técnica

Esta tabela classifica os itens de dívida técnica identificados no sistema original.

A escala utilizada vai de 1 a 5:

- **Esforço:** dificuldade estimada para quitar a dívida.
- **Impacto:** efeito da dívida sobre manutenção, risco de falha ou evolução do sistema.
- **Juros:** custo recorrente de manter a dívida no sistema.

| ID | Resumo da dívida | Esforço | Impacto | Juros | Justificativa |
|---|---|---:|---:|---:|---|
| D1 | Senha de administrador fixa no código | 2 | 4 | 3 | Expõe uma configuração sensível e dificulta alteração segura, mas a correção é simples. |
| D2 | Lista global `produtos` | 4 | 4 | 4 | Aumenta acoplamento e dificulta testes, mas remover completamente exigiria reorganizar várias funções. |
| D3 | Nome pouco descritivo da função `add` | 1 | 2 | 2 | Afeta legibilidade, mas é simples de corrigir e não causa falha direta. |
| D4 | Parâmetro mutável padrão `hist=[]` | 2 | 3 | 3 | Pode causar comportamento inesperado caso o histórico seja usado no futuro. |
| D5 | Importação `datetime` não utilizada | 1 | 1 | 1 | Polui pouco o código e tem baixo impacto. |
| D6 | Venda aceita quantidade negativa | 2 | 5 | 5 | Causa erro grave de regra de negócio: gera total negativo e aumenta o estoque indevidamente. |
| D7 | Entrada inválida derruba o programa | 3 | 5 | 4 | O sistema encerra com erro ao receber preço ou quantidade inválida, prejudicando robustez. |
| D8 | Regras de desconto inconsistentes | 2 | 5 | 5 | Pode gerar totais diferentes para a mesma venda e dificulta evolução da regra de negócio. |
| D9 | Limite de estoque baixo fixo no código | 1 | 3 | 2 | Dificulta mudança futura da regra, mas é simples de extrair para constante. |
| D10 | Código antigo comentado | 1 | 2 | 1 | Afeta limpeza e leitura do arquivo, mas não altera comportamento. |
| D11 | Função `relatorio_vendas` incompleta | 2 | 3 | 2 | Indica funcionalidade planejada mas não implementada, podendo confundir manutenção. |
| D12 | Função `menu` mistura responsabilidades | 4 | 4 | 4 | Mistura interface, entrada de dados e regras de negócio, dificultando testes e evolução. |
| D13 | Chamada direta de `menu()` ao importar arquivo | 1 | 4 | 4 | Dificulta testes automatizados das funções, mas pode ser corrigido facilmente com `if __name__ == "__main__"`. |
| D14 | Ausência de testes automatizados no projeto original | 3 | 5 | 5 | Aumenta risco de regressão e dificulta refatorações seguras. |
| D15 | Ausência de documentação original | 2 | 3 | 3 | Dificulta execução e manutenção por novos desenvolvedores. |