"""Optional two-dimensional bus movement demonstration."""


def run_simulation() -> None:
    try:
        import pygame
    except ImportError as exc:
        raise RuntimeError("Install the optional dependency with: pip install pygame") from exc
    pygame.init()
    screen = pygame.display.set_mode((700, 260))
    pygame.display.set_caption("Bus between stops - self-study simulation")
    clock = pygame.time.Clock()
    x = 30
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x = 30 if x > 620 else x + 2
        screen.fill((245, 245, 245))
        pygame.draw.line(screen, (90, 90, 90), (20, 200), (680, 200), 4)
        pygame.draw.rect(screen, (40, 110, 190), (x, 145, 70, 40))
        pygame.draw.circle(screen, (25, 25, 25), (x + 16, 190), 8)
        pygame.draw.circle(screen, (25, 25, 25), (x + 55, 190), 8)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    run_simulation()
