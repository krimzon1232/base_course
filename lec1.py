def full_energy(m, h, v, g=9.8):
    return m * g * h + 0.5 * m * v**2


print(full_energy(2, 10, 3))   

def full_energy_default(h, v, m=1.0, g=9.8):
    return m * g * h + 0.5 * m * v**2


print(full_energy_default(5, 4))          
print(full_energy_default(5, 4, m=3))     


def full_energy_dict(p):
    m = p.get("m", 1.0)
    h = p.get("h", 0.0)
    v = p.get("v", 0.0)
    g = p.get("g", 9.8)
    return m * g * h + 0.5 * m * v**2

data = {"m": 3, "h": 12, "v": 5}
print(full_energy_dict(data))
