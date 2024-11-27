import pygame

sound = 'ex21.mp3'

pygame.init()
pygame.mixer.music.load(sound)
pygame.mixer.music.play()
input()
pygame.event.wait()