    if event.key == pygame.K_s and pause==False: #pause
                    son.stop()
                    pause=True
                if event.key == pygame.K_p and pause==True: # replay
                    son.play()

                if event.key == pygame.K_r and pause==True: # unpause
                    son.__repr__()

                if event.key == pygame.K_UP:
                    son.set_volume(son.get_volume()+0.1)
                if event.key == pygame.K_DOWN:
                    son.set_volume(son.get_volume()-0.1)
