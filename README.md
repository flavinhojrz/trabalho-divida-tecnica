# Trabalho Unidade III — Dívida Técnica

Repositório destinado ao trabalho da Unidade III da disciplina **DIM0501 — Boas Práticas de Programação**.

## Tema

Identificação, classificação e priorização de dívida técnica em um sistema de controle de estoque e vendas.

## Objetivo

O objetivo deste trabalho é analisar um sistema legado simples, identificar os principais itens de dívida técnica, classificá-los, priorizá-los e realizar a quitação demonstrativa dos itens considerados mais importantes.

O foco do trabalho não é reescrever o sistema do zero, mas sim compreender os problemas existentes no código, avaliar o impacto de cada dívida e decidir quais itens devem ser corrigidos primeiro.

## Sistema analisado

O sistema analisado é um **Sistema de Controle de Estoque e Vendas** desenvolvido em Python.

Funcionalidades principais do sistema original:

* Cadastro de produtos;
* Registro de vendas;
* Baixa automática no estoque;
* Cálculo do valor total de uma venda;
* Aplicação de desconto em determinadas vendas;
* Listagem de produtos cadastrados;
* Relatório de produtos com estoque baixo.

## Linguagem escolhida

A linguagem escolhida para o desenvolvimento do trabalho foi:

**Python**

## Estrutura do repositório

```text
.
├── codigo/
│   └── estoque_original.py
├── README.md
└── Trabalho_Unidade3_Divida_Tecnica.docx.pdf
```

## Como executar o sistema

Para executar o sistema original, utilize o comando:

```bash
python3 codigo/estoque_original.py
```

ou, dependendo da configuração do ambiente:

```bash
python codigo/estoque_original.py
```

