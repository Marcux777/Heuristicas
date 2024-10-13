from GGA import GGA
import time as t
from concurrent.futures import ProcessPoolExecutor, as_completed


def create_data(Arquivo):
    caminho = f"/workspaces/Heuristicas/Heuristicas/BPP/BPPInstances/{Arquivo}"

    def read_instance(arquivo):
        with open(arquivo, "r") as file:
            lines = file.read()
        return lines

    itens = list(map(int, filter(None, read_instance(caminho).split("\n"))))
    tam, bin_size = itens[0], itens[1]
    itens.pop(0), itens.pop(0)
    data = {
        "weights": itens,
        "items": list(range(len(itens))),
        "bins": list(range(len(itens))),
        "bin_capacity": bin_size,
    }
    return data


def process_instance(Arquivo):
    start_time = t.time()
    data = create_data(Arquivo)
    gga = GGA(data)
    best_solution = gga.run()
    end_time = t.time()
    # Retornar também o nome do arquivo
    return Arquivo, best_solution, end_time - start_time


def main():
    # Lista de arquivos a serem processados
    # Adicione mais arquivos conforme necessário
    arquivos = [
        "Scholl/Scholl_2/N4W1B1R0.txt",
        "Scholl/Scholl_2/N4W1B1R1.txt",
        "Scholl/Scholl_2/N4W1B1R2.txt",
        "Scholl/Scholl_2/N4W1B1R3.txt",
        "Scholl/Scholl_2/N4W1B1R4.txt",
        "Scholl/Scholl_2/N4W1B1R5.txt"
    ]

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_instance, arquivo)
                   for arquivo in arquivos]

        for future in as_completed(futures):
            try:
                arquivo, best_solution, execute_time = future.result()
                print(f"\nMelhor solução encontrada para {arquivo}:")
                print("=" * 100)
                for i, container in enumerate(best_solution, 1):
                    print(f"Contêiner {i}: {container}")
                print("=" * 100)
                print("Quantidade de contêineres usados: ", len(best_solution))
                print("=" * 100)
                print("Tempo total de solução: {:.2f} segundos".format(
                    execute_time))
                print("=" * 100)
            except Exception as exc:
                print(f"{arquivo} gerou uma exceção: {exc}")


if __name__ == "__main__":
    main()
