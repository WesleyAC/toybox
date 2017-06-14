import pygame

class Viewer(object):
    def __init__(self, models, width=800, height=600):
        self.width = width
        self.height = height
        self.models = models

        self.screen = None

        self.background = (10,10,50)
        self.nodeColor = (255,255,255)
        self.edgeColor = (200,200,200)
        self.nodeRadius = 4

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Model Viewer')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display()
            pygame.display.flip()

    def display(self):
        self.screen.fill(self.background)
        for model in self.models:
            for edge in model.edges:
                print(edge)
                pygame.draw.aaline(self.screen, self.edgeColor, (model.nodes[edge[0]][0], model.nodes[edge[0]][1]), (model.nodes[edge[1]][0], model.nodes[edge[1]][1]))
