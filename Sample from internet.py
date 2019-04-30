class Tub(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("tub.bmp").convert_alpha()
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height - 100
    def movement(self):
        keys = pygame.key.get_pressed()
        dist = 5
        if keys [pygame.K_LEFT]:
            self.rect.x -= dist
        if keys [pygame.K_RIGHT]:
            self.rect.x += dist
    def hit(self, target):
        return self.rect.colliderect(target)

class Singlescoop_pink(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("singlescoop_pink.bmp").convert_alpha()
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-100) #random x position, minus 100 so image does not go off screen
        self.rect.y = -600 #start off screen so starting point to fall down is not visible
    def movement(self):
        self.rect.y += 5
        if self.rect.y > height:
            self.kill()


tub = Tub()
sspink = Singlescoop_pink()
sprites = pygame.sprite.RenderPlain(tub, sspink)
score = 0

def game_loop():

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()

        if tub.hit(sspink):
            sspink.kill()
            global score
            score += 1

        tub.movement()
        sspink.movement()
        screen.fill(white)
        t = f.render("Score = " + str(score), False, black)
        screen.blit(t, (0,0))
        sprites.update()
        sprites.draw(screen)
        display.update()
        clock.tick(60)

game_loop()