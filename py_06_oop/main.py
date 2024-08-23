# Maqsad: Eng yaxshi strategiyani tuzish
from cs import Counter, Terror


p1 = Counter("Adam", "USP")
p2 = Terror("John", "AK-47")
p3 = Counter("Kevin", "Glock")

print(type(p3))

print(p1.name, p1.health, p1.weapon)
print(p2.name, p2.health, p2.weapon)
print(p3.name, p3.health, p3.weapon)

p1.salomlash()
p2.plant()
p1.defuse()

p1.shoot(p2)
p1.shoot(p3)
p1.shoot(p3)

print(p1.name, p1.health)
print(p2.name, p2.health)
print(p3.name, p3.health)

del p3
# NameError: name 'p3' is not defined.
# print(p3.name, p3.health)
