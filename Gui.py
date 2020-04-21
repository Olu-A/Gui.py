Gui.py

	self.name = gameGuy
	Self.rect = (0,0)
	self.image = pygame.image.load(img_file)
	self.strength = 1
	self.speed = 3
	self.intelligence = 2

'''
makes gameGuy character move u, down left, and right
input "w", "a", "s", "d"
return N/A
'''
	def move(self):
		if input(w):
			self.rect.y -= self.speed
		elif input(s):
			self.rect.y += self.speed
		elif input(a):
			self.rect.x -= self.speed
		elif input(d):
			self.rect.x += self.speed
'''
makes gameGuy attack and lose health based on random parameters
input N/A
output N/A
'''
	def fight(self, opponent):
		if(random.randrange(5)):
			self.health -= 1
			print("failure)
			return False
		else:
			print("success")
			return True
