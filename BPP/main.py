from GGA import GGA
import time as t


def create_data(Arquivo):
    caminho = f"/workspaces/Heuristicas/Heuristicas/BPP/BPPInstances/{
        Arquivo}"

    def read_instance(arquivo):
        with open(arquivo, "r") as file:
            lines = file.read()

        return lines

    itens = list(map(int, filter(None, read_instance(caminho).split("\n"))))
    print(itens)
    tam, bin_size = itens[0], itens[1]
    itens.pop(0), itens.pop(0)
    data = {
        "weights": itens,
        "items": list(range(len(itens))),
        "bins": list(range(len(itens))),
        "bin_capacity": bin_size,
    }
    return data


start_time = t.time()

data = create_data("Scholl/Scholl_1/N4C3W4_T.txt")

gga = GGA(data)
best_solution = gga.run()

end_time = t.time()

print("\nMelhor solução encontrada na Grouping Genetic Algorithm:")
print("=" * 100)
for i, container in enumerate(best_solution, 1):
    print(f"Contêiner {i}: {container}")
print("=" * 100)

print("Quantidade de Contêiners usados: ", len(best_solution))
print("="*100)
print("Tempo de solução: {:.2f} segundos".format(end_time - start_time))
print("="*100)
