import pygame
import player, world, camera, items

FPS = 60
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 400

def world_to_screen_pos(world_x, world_y, camera_x, camera_y):
    return (world_x - camera_x + SCREEN_WIDTH // 2, -(world_y - camera_y - SCREEN_HEIGHT // 2))

def main():
    game_world = world.World()
    user_player = player.Player()
    game_world.add_object(user_player, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    game_camera = camera.Camera(user_player)

    test_object = items.Stick()
    game_world.add_object(test_object, 200, 200)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    user_player.toggle_move_up()
                elif event.key == pygame.K_d:
                    user_player.toggle_move_right()
                elif event.key == pygame.K_s:
                    user_player.toggle_move_down()
                elif event.key == pygame.K_a:
                    user_player.toggle_move_left()
                elif event.key == pygame.K_LSHIFT:
                    user_player.toggle_run()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    user_player.toggle_move_up()
                elif event.key == pygame.K_d:
                    user_player.toggle_move_right()
                elif event.key == pygame.K_s:
                    user_player.toggle_move_down()
                elif event.key == pygame.K_a:
                    user_player.toggle_move_left()
                elif event.key == pygame.K_LSHIFT:
                    user_player.toggle_run()
        
        user_player.movement_update()
        game_camera.update_position()

        screen.fill((0, 255, 0))

        for obj in game_world.objects:
            obj.draw(screen, *world_to_screen_pos(obj.x, obj.y, game_camera.x, game_camera.y))

        user_player.draw(screen, *world_to_screen_pos(user_player.x, user_player.y, game_camera.x, game_camera.y))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()