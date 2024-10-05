
class Container:
    def __init__(self, capacity):
        self.elements = []  # Lista de elementos (tamanhos) dentro do container
        self.capacity = capacity  # Capacidade máxima do container
        self.used_space = 0  # Espaço já utilizado no container

    def add_element(self, element):
        if self.used_space + element <= self.capacity:
            self.elements.append(element)
            self.used_space += element
        else:
            raise Exception("Capacidade excedida no container!")

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.used_space -= element

    def is_full(self):
        return self.used_space >= self.capacity

    def remaining_space(self):
        return self.capacity - self.used_space

    def __repr__(self):
        return f"Container({self.elements}, usado: {self.used_space}/{self.capacity})"
