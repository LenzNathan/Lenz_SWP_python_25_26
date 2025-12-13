import pytest


class LivingBeing:
    def __init__(self, name):
        self.name = name
        self.metabolism_value = 0

    def absorb(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.metabolism_value += amount / 4  # Can only absorb a quarter of the amount (basic lifeforms)
        print(f"{self.name} collects {amount / 4} useful elements from the environment for metabolism.")
        return amount / 4

    def expulse(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        if amount / 4 <= self.metabolism_value:
            self.metabolism_value -= amount / 4
            print(f"{self.name} releases {amount / 4} waste elements back into the environment.")
            return amount / 4
        else:
            print(f"{self.name} does not have enough molecules to expulse.")
            raise ValueError("Not enough molecules to expulse.")

    def __str__(self):
        return f"LivingBeing {self.name}, metabolism_value={self.metabolism_value}"


class Animal(LivingBeing):
    def __init__(self, name):
        super().__init__(name)
        self.waste_level = 0

    def absorb(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.metabolism_value += amount / 2  # Animals can absorb half of the amount
        print(f"The Animal {self.name} ate food and gained {amount / 2} energy.")
        return amount / 2

    def hunt(self, energy):
        if energy < 0:
            raise ValueError("Energy must be positive.")
        if energy <= self.metabolism_value:
            self.metabolism_value -= energy
            self.waste_level += energy
            print(f"The Animal {self.name} hunted and used {energy} energy.")
            return energy
        else:
            print(f"The Animal {self.name} does not have enough energy to hunt.")
            raise ValueError("Not enough energy to hunt.")

    def expulse(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        if self.metabolism_value - amount / 8 < 0:
            print(f"The Animal {self.name} has too little energy to get rid of waste.")
            raise ValueError("Not enough energy to get rid of waste.")
        if amount / 2 <= self.waste_level:
            self.waste_level -= amount / 2  # Animals get rid of waste faster
            self.metabolism_value -= amount / 8  # Expulsing waste costs some energy
            self.waste_level += amount / 8  # energy used to expulse creates some waste
            print(f"The Animal {self.name} left {amount / 2} waste behind.")
            return amount / 2
        else:
            print(f"The Animal {self.name} does not have that much waste to get rid of.")
            raise ValueError("Not enough waste to get rid of.")

    def __str__(self):
        return f"Animal {self.name}, metabolism_value={self.metabolism_value}, waste_level={self.waste_level}"


class Human(Animal):
    def __init__(self, name):
        super().__init__(name)

    def absorb(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.metabolism_value += amount  # Humans can absorb the full amount
        print(f"The Human {self.name} managed to bake and eat a frozen pizza, it gained {amount} energy.")
        return amount

    def hunt(self, energy):
        if energy < 0:
            raise ValueError("Energy must be positive.")
        if energy / 5 < self.metabolism_value:
            self.metabolism_value -= energy / 5  # Humans use less energy to hunt (they go to the fridge)
            self.waste_level += energy / 5
            print(
                f"The Human {self.name} managed to go to the fridge and used {energy / 5} "
                f"energy because the fridge was {energy} meters away.")
            return energy / 5
        else:
            print(
                f"The Human {self.name} does not have enough will power to go to a fridge "
                f"which is {energy} meters away.")
            raise ValueError("Not enough energy to go to the fridge.")

    def expulse(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        if self.metabolism_value - amount / 15 < 0:
            print(f"The Human {self.name} is too tired to go to the bathroom.")
            raise ValueError("Not enough energy to go to the bathroom.")
        if amount <= self.waste_level:
            self.waste_level -= amount  # Humans get rid of the full amount
            self.metabolism_value -= amount / 15  # Expulsing waste costs some energy
            self.waste_level += amount / 15  # energy used to expulse creates some waste
            print(f"The Human {self.name} went to the bathroom and left {amount} waste behind.")
            return amount
        else:
            print(f"The Human {self.name} does not have that much waste to get rid of.")
            raise ValueError("Not enough waste to get rid of.")

    def __str__(self):
        return f"Human {self.name}, metabolism_value={self.metabolism_value}, waste_level={self.waste_level}"


def test_living_being():
    btbc = LivingBeing("Bob the Brain Cell")
    with pytest.raises(ValueError): btbc.expulse(1)
    with pytest.raises(ValueError):  btbc.absorb(-1)
    with pytest.raises(ValueError):  btbc.expulse(-1)
    print(btbc)
    assert btbc.absorb(4) == 1
    print(btbc)
    assert btbc.absorb(20) == 5
    print(btbc)
    assert btbc.expulse(4) == 1
    print(btbc)
    assert btbc.expulse(20) == 5
    print(btbc)
    with pytest.raises(ValueError):  btbc.expulse(1)

def test_animal():
    gep = Animal("Gepard")
    with pytest.raises(ValueError): gep.hunt(1)
    with pytest.raises(ValueError): gep.absorb(-1)
    with pytest.raises(ValueError): gep.hunt(-1)
    with pytest.raises(ValueError): gep.expulse(-1)
    assert gep.absorb(10) == 5
    print(gep)
    assert gep.hunt(4) == 4
    print(gep)
    assert gep.expulse(8) == 4
    print(gep)
    with pytest.raises(ValueError): gep.expulse(2)
    with pytest.raises(ValueError): gep.expulse(4)

def test_human():
    bob = Human("Bob")
    with pytest.raises(ValueError): bob.hunt(100)
    with pytest.raises(ValueError): bob.absorb(-1)
    with pytest.raises(ValueError): bob.hunt(-1)
    with pytest.raises(ValueError): bob.expulse(-1)
    assert bob.absorb(20) == 20
    print(bob)
    assert bob.hunt(10) == 2
    print(bob)
    assert bob.expulse(2) == 2
    print(bob)
    with pytest.raises(ValueError): bob.expulse(5)
