# Inventário da Dívida Técnica

Este documento registra os itens de dívida técnica identificados no sistema original de controle de estoque e vendas.

| ID | Localização | Descrição do problema | Tipo de dívida | Evidência |
|---|---|---|---|---|
| D1 | `SENHA_ADMIN` | A senha de administrador está fixa no código como `"1234"`. Isso dificulta alteração segura e expõe uma informação sensível diretamente no código-fonte. | Configuração / Segurança | Análise direta do código |
| D2 | variável global `produtos` | A lista de produtos é uma variável global acessada e modificada diretamente por várias funções. Isso aumenta o acoplamento e dificulta testes. | Arquitetura / Design | Análise direta do código |
| D3 | função `add` | O nome da função é pouco descritivo. O nome `add` não deixa claro que a função cadastra produtos no estoque. | Código | Análise direta do código |
| D4 | função `add(n, p, q, hist=[])` | A função usa uma lista mutável como valor padrão do parâmetro `hist`. Isso pode gerar comportamento inesperado entre chamadas diferentes. | Código / Robustez | Análise direta do código |
| D5 | `import datetime` | A biblioteca `datetime` é importada, mas não é utilizada em nenhuma parte do código. | Código morto | Análise direta do código |
| D6 | função `vender` | O sistema não valida se a quantidade vendida é maior que zero. Com isso, aceita venda negativa, gera total negativo e aumenta o estoque indevidamente. | Robustez | Demonstrado por `tests/demonstrar_dividas.py` |
| D7 | função `menu` | O sistema não trata entradas inválidas ao converter preço para `float` e quantidade para `int`. Ao receber um valor inválido, o programa encerra com erro. | Robustez | Demonstrado por `tests/demonstrar_dividas.py` |
| D8 | funções `vender` e `calcular_total` | Existem duas regras diferentes de desconto: `vender` usa desconto de 10% acima de 100, enquanto `calcular_total` usa desconto de 15% acima de 200. Isso pode gerar resultados inconsistentes. | Código / Regra de negócio | Análise direta do código |
| D9 | função `relatorio_estoque_baixo` | O limite de estoque baixo está fixo no código como `5`, dificultando alteração futura da regra. | Configuração | Análise direta do código |
| D10 | função `exportar` comentada | Existe código antigo comentado que não é mais usado. Isso polui o arquivo e dificulta a leitura. | Código morto | Análise direta do código |
| D11 | função `relatorio_vendas` | A função está incompleta, contendo apenas um `TODO` e `pass`. | Marcador / Código incompleto | Análise direta do código |
| D12 | função `menu` | A função mistura interface de usuário, entrada de dados, validação e chamadas de regra de negócio. | Arquitetura / Design | Análise direta do código |
| D13 | chamada direta de `menu()` | O programa executa o menu automaticamente ao importar o arquivo, dificultando testes automatizados das funções. | Testes / Design | Análise direta do código |
| D14 | projeto geral | O projeto original não possui testes automatizados. | Testes | Análise da estrutura original |
| D15 | projeto geral | O projeto original não possui documentação explicando como executar, testar ou manter o sistema. | Documentação | Análise da estrutura original |