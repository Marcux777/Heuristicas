from GGA import GGA
import time as t
from concurrent.futures import ThreadPoolExecutor, as_completed


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
    data = create_data(Arquivo)
    gga = GGA(data)
    best_solution = gga.run()
    return best_solution


if __name__ == "__main__":
    start_time = t.time()

    # Adicione mais arquivos conforme necessário
    arquivos = ["E_120_N_40_60/E_120_N_40_60_BF0000.bpp",
                "E_250_U_20_100/E_250_U_20_100_BF0000.bpp",
                "Randomly_Generated/BPP_1000_1000_0.2_0.8_9.txt"]

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(
            process_instance, arquivo): arquivo for arquivo in arquivos}

        for future in as_completed(futures):
            arquivo = futures[future]
            try:
                best_solution = future.result()
                print(f"\nMelhor solução encontrada para {arquivo}:")
                print("=" * 100)
                for i, container in enumerate(best_solution, 1):
                    print(f"Contêiner {i}: {container}")
                print("=" * 100)
                print("Quantidade de Contêiners usados: ", len(best_solution))
                print("=" * 100)
            except Exception as exc:
                print(f"{arquivo} gerou uma exceção: {exc}")

    end_time = t.time()
    print("Tempo total de solução: {:.2f} segundos".format(
        end_time - start_time))
    print("=" * 100)
