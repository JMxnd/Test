import pygame

pygame.init()

leftM = False

rightM = False

screenX = 1400
screenY = 700
screen = pygame.display.set_mode((screenX, screenY))

playerX = 500

while True:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit
		if event.type == pygame.FINGERDOWN:
			x = event.x * screenX
			y = event.y * screenY
			if left.collidepoint(x, y):
				leftM = True
			if right.collidepoint(x, y):
				rightM = True
		if event.type == pygame.FINGERUP:
			x = event.x * screenX
			y = event.y * screenY
			if left.collidepoint(x, y):
				leftM = False
			if right.collidepoint(x, y):
				rightM = False
				
	player = pygame.draw.rect(screen, (200, 0, 0), (playerX, 200, 100, 100))
	left = pygame.draw.rect(screen, (0, 200, 0), (0, 0, 100, 100))
	right = pygame.draw.rect(screen, (0, 200, 0), (1200, 0, 100, 100))
				
	if leftM:
			playerX = playerX - 5
			
	if rightM:
			playerX = playerX + 5
			
	pygame.display.flip()