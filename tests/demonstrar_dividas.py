import subprocess
import sys
from pathlib import Path


def executar_programa(caminho_arquivo, entradas):
    return subprocess.run(
        [sys.executable, str(caminho_arquivo)],
        input=entradas,
        text=True,
        capture_output=True,
        timeout=10
    )


def demonstrar_venda_com_quantidade_negativa(caminho_arquivo):
    print("\n=== Caso 1: venda com quantidade negativa ===")

    entradas = "\n".join([
        "1",
        "Arroz",
        "10",
        "10",

        "2",
        "Arroz",
        "-5",

        "3",

        "0"
    ]) + "\n"

    resultado = executar_programa(caminho_arquivo, entradas)

    print(resultado.stdout)

    if "Venda realizada. Total: -50.0" in resultado.stdout:
        print("[EVIDÊNCIA] O sistema aceitou venda com total negativo.")

    if "Arroz - R$10.0 - qtd: 15" in resultado.stdout:
        print("[EVIDÊNCIA] O estoque aumentou após uma venda negativa.")


def demonstrar_entrada_invalida_no_preco(caminho_arquivo):
    print("\n=== Caso 2: entrada inválida no preço ===")

    entradas = "\n".join([
        "1",
        "ProdutoTeste",
        "abc"
    ]) + "\n"

    resultado = executar_programa(caminho_arquivo, entradas)

    print("Código de retorno:", resultado.returncode)

    if resultado.stderr:
        print("\nErro capturado:")
        print(resultado.stderr)

    if resultado.returncode != 0:
        print("[EVIDÊNCIA] O sistema encerrou com erro ao receber preço inválido.")


def main():
    if len(sys.argv) != 2:
        print("Uso:")
        print("python3 tests/demonstrar_dividas.py caminho/do/arquivo.py")
        sys.exit(1)

    caminho_arquivo = Path(sys.argv[1])

    if not caminho_arquivo.exists():
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        sys.exit(1)

    print(f"Analisando dívidas técnicas em: {caminho_arquivo}")

    demonstrar_venda_com_quantidade_negativa(caminho_arquivo)
    demonstrar_entrada_invalida_no_preco(caminho_arquivo)


if __name__ == "__main__":
    main()