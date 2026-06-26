import subprocess
import sys
from pathlib import Path


def executar_programa(caminho_arquivo, entradas):
    resultado = subprocess.run(
        [sys.executable, str(caminho_arquivo)],
        input=entradas,
        text=True,
        capture_output=True,
        timeout=10
    )

    return resultado.returncode, resultado.stdout, resultado.stderr


def verificar_saida(saida, texto_esperado):
    if texto_esperado not in saida:
        raise AssertionError(
            f"\nTexto esperado não encontrado:\n"
            f"ESPERADO: {texto_esperado}\n\n"
            f"SAÍDA OBTIDA:\n{saida}"
        )


def test_fluxo_principal(caminho_arquivo):
    entradas = "\n".join([
        # Cadastrar Arroz
        "1",
        "Arroz",
        "10",
        "20",

        # Listar produtos
        "3",

        # Vender Arroz com estoque suficiente
        "2",
        "Arroz",
        "3",

        # Listar novamente para verificar baixa no estoque
        "3",

        # Tentar vender quantidade maior que o estoque
        "2",
        "Arroz",
        "999",

        # Tentar vender produto inexistente
        "2",
        "Feijao",
        "1",

        # Cadastrar Queijo para testar desconto
        "1",
        "Queijo",
        "60",
        "10",

        # Vender Queijo: 60 * 2 = 120, com 10% de desconto = 108
        "2",
        "Queijo",
        "2",

        # Cadastrar produto com estoque baixo
        "1",
        "Manteiga",
        "15",
        "3",

        # Emitir relatório de estoque baixo
        "4",

        # Testar senha admin correta
        "5",
        "1234",

        # Testar senha admin incorreta
        "5",
        "0000",

        # Sair
        "0"
    ]) + "\n"

    codigo_retorno, saida, erro = executar_programa(caminho_arquivo, entradas)

    if codigo_retorno != 0:
        raise AssertionError(
            f"O programa terminou com erro.\n"
            f"Código de retorno: {codigo_retorno}\n"
            f"Erro:\n{erro}\n"
            f"Saída:\n{saida}"
        )

    verificar_saida(saida, "Produto adicionado!")
    verificar_saida(saida, "Arroz - R$10.0 - qtd: 20")
    verificar_saida(saida, "Venda realizada. Total: 30.0")
    verificar_saida(saida, "Arroz - R$10.0 - qtd: 17")
    verificar_saida(saida, "Estoque insuficiente")
    verificar_saida(saida, "Produto nao encontrado")
    verificar_saida(saida, "Venda realizada. Total: 108.0")
    verificar_saida(saida, "Manteiga esta com estoque baixo (3)")
    verificar_saida(saida, "Acesso liberado")
    verificar_saida(saida, "Senha errada")


def main():
    if len(sys.argv) != 2:
        print("Uso:")
        print("python3 tests/test_regressao_cli.py caminho/do/arquivo.py")
        sys.exit(1)

    caminho_arquivo = Path(sys.argv[1])

    if not caminho_arquivo.exists():
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        sys.exit(1)

    print(f"Executando testes em: {caminho_arquivo}")

    test_fluxo_principal(caminho_arquivo)

    print("Todos os testes passaram!")


if __name__ == "__main__":
    main()