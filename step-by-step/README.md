# Learn Pygame by example.

https://www.patternsgameprog.com/series/discover-python-and-patterns/


9. Pygame
  - [empty window](begin.py)
  - [support closing](begin-close.py)
  - [rectangle](rectangle.py)
  
EXTRA.  uv
  - What is uv (and venv) ?
    - Before this, what is standard library, and 3rd party library?


10. Keyboard
  - [move with keyboard](keyboard-test.py)


11. Class
  - [Make this a class](class-game.py)


13. Sprites

Definition:  "A Sprite is an object that contains a Surface (the image) and a Rect (the position and size)."

- self.image (The Surface): This is the visual part—the actual pixels, colors, and shapes.

- self.rect (The Rectangle): This is the mathematical part. It defines where the image sits on the screen and how big it is.


- Sprite Group
  - Normally, you’d have to write `screen.blit(sprite.image, sprite.rect)` for every single object. 
  - The Group knows to look for the attributes `.image` and `.rect` automatically. 
  - If your Sprite doesn't have those exact names, the Group will throw an error!

```python
all_sprites = pygame.sprite.Group()

player = Box("red", 100, 100)
enemy = Box("blue", 200, 200)
all_sprites.add(player, enemy)

# LOOP
all_sprites.update()        # MAGIC: Calls update() on every sprite in the group

screen.fill("white")        # White blank screen
all_sprites.draw(screen)    # MAGIC: Draws every sprite's 'image' at its 'rect' position

pygame.display.flip()

```





## Or, supplementary docs

python3 -m pygame.examples.aliens

https://www.geeksforgeeks.org/python/pygame-tutorial/

https://pygame.readthedocs.io/en/latest/1_intro/intro.html

