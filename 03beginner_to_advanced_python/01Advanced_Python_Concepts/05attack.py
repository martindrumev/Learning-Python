from enemy import Enemy

# You never want to put classes in your main code, cause it gets messy
enemy = Enemy(200, 60)
print("HP:", enemy.get_hp())
