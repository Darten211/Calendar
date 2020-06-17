def blit_text(surface, text, pos, font, color, max_width, block_x, interline):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    x, y = pos

    no_lines = 1

    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()

            if x + word_width - block_x >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height * interline  # Start on new row.
                no_lines += 1
            surface.blit(word_surface, (x, y))
            x += word_width + space
    
    return no_lines