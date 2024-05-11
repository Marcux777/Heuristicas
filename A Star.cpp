#include <bits/stdc++.h>

using namespace std;
struct Node
{
    int id;     // Identificador único do nó
    int gScore; // Custo real para chegar ao nó
    int hScore; // Heurística de custo estimado para o objetivo
    int fScore; // Custo total (gScore + hScore)
    int parent; // ID do nó pai
};

// Classe para implementar o algoritmo A*
class AStar
{
public:
    // Construtor para inicializar o algoritmo
    AStar(const vector<vector<pair<int, int>>> &graph, int start, int goal)
    {
        this->graph = graph;
        this->start = start;
        this->goal = goal;
    }

    // Função principal para encontrar o caminho mínimo
    vector<int> findPath()
    {
        // Lista de nós abertos (fronteira)
        priority_queue<pair<int, Node *>, vector<pair<int, Node *>>, greater<pair<int, Node *>>> open;

        // Mapa para armazenar os nós visitados
        unordered_map<int, Node *> closed;

        // Cria o nó inicial e adiciona à lista aberta
        Node *current = new Node{start, 0, estimate(start), estimate(start) + 0, -1};
        open.push({current->fScore, current});

        // Loop principal da busca
        while (!open.empty())
        {
            // Remove o nó com menor custo total da lista aberta
            current = open.top().second;
            open.pop();

            // Verifica se o nó atual é o objetivo
            if (current->id == goal)
            {
                // Reconstrói o caminho e retorna
                return reconstructPath(current);
            }

            // Marca o nó atual como visitado
            closed[current->id] = current;

            // Expande os vizinhos do nó atual
            for (const pair<int, int> &neighbor : graph[current->id])
            {
                // Ignora os vizinhos já visitados
                if (closed.count(neighbor.first) > 0)
                    continue;

                // Cria o nó vizinho
                Node *neighborNode = new Node{neighbor.first, current->gScore + neighbor.second, estimate(neighbor.first), current->gScore + neighbor.second + estimate(neighbor.first), current->id};

                // Verifica se o caminho para o vizinho é melhor
                if (open.count(neighbor.first) == 0 || neighborNode->fScore < open.top().second->fScore)
                {
                    // Atualiza o custo e a pai do vizinho
                    neighborNode->gScore = current->gScore + neighbor.second;
                    neighborNode->fScore = neighborNode->gScore + estimate(neighbor.first);
                    neighborNode->parent = current->id;

                    // Adiciona o vizinho à lista aberta
                    open.push({neighborNode->fScore, neighborNode});
                }
            }

            delete current;
        }

        // Nenhum caminho encontrado
        return {};
    }

private:
    // Função para estimar o custo heurístico para o objetivo
    int estimate(int node)
    {
        // Exemplo de heurística: distância Manhattan
        int dx = abs(node % 10 - goal % 10);
        int dy = abs(node / 10 - goal / 10);
        return dx + dy;
    }

    // Função para reconstruir o caminho a partir do nó final
    vector<int> reconstructPath(Node *node)
    {
        vector<int> path;

        while (node != nullptr)
        {
            path.push_back(node->id);
            node = closed[node->parent];
        }

        reverse(path.begin(), path.end());
        return path;
    }

    // Variáveis membro da classe
    const vector<vector<pair<int, int>>> &graph;
    int start;
    int goal;
};

int main()
{
    vector<vector<pair<int, int>>> graph = {{3, 4, 2}, {2, 1, 3}, {1, 2, 10}, {2, 3, 5}};
    AStar astar(graph, 0, 5);
    vector<int> path = astar.findPath();
    for (int node : path)
        cout << node << " ";
    cout << endl;
    return 0;
}