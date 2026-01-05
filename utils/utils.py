from pygame import font, surface

def draw_text(text:str, text_size:int, x:int, y:int, surface:surface):
    text_font = font.Font(None, text_size)
    text = text_font.render(text, True, (255,255,255))
    surface.blit(text, (x, y))