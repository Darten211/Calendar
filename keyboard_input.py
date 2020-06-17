import pygame as pg

def key_handle(key, current_string, alt, shift):
    if key == pg.K_BACKSPACE:
        current_string = current_string[0:-1]
    elif key <= 127:
        if alt:
            if key == pg.K_a:
                if shift:
                    current_string += 'Ą'
                else:
                    current_string += 'ą'
            if key == pg.K_c:
                if shift:
                    current_string += 'Ć'
                else:
                    current_string += 'ć'
            if key == pg.K_e:
                if shift:
                    current_string += 'Ę'
                else:
                    current_string += 'ę'
            if key == pg.K_s:
                if shift:
                    current_string += 'Ś'
                else:
                    current_string += 'ś'
            if key == pg.K_l:
                if shift:
                    current_string += 'Ł'
                else:
                    current_string += 'ł'
            if key == pg.K_z:
                if shift:
                    current_string += 'Ż'
                else:
                    current_string += 'ż'
            if key == pg.K_x:
                if shift:
                    current_string += 'Ź'
                else:
                    current_string += 'ź'
            if key == pg.K_o:
                if shift:
                    current_string += 'Ó'
                else:
                    current_string += 'ó'
            if key == pg.K_n:
                if shift:
                    current_string += 'Ń'
                else:
                    current_string += 'ń'
        elif shift:
            if key == pg.K_1:
                current_string += '!'
            elif key == pg.K_2:
                current_string += '@'
            elif key == pg.K_3:
                current_string += '#'
            elif key == pg.K_4:
                current_string += '$'
            elif key == pg.K_5:
                current_string += '%'
            elif key == pg.K_6:
                current_string += '^'
            elif key == pg.K_7:
                current_string += '&'
            elif key == pg.K_8:
                current_string += '*'
            elif key == pg.K_9:
                current_string += '('
            elif key == pg.K_0:
                current_string += ')'
            elif key == pg.K_LEFTBRACKET:
                current_string += '{'
            elif key == pg.K_RIGHTBRACKET:
                current_string += '}'
            elif key == pg.K_SEMICOLON:
                current_string += ':'
            elif key == pg.K_SLASH:
                current_string += '?'
            elif key == pg.K_COMMA:
                current_string += '<'
            elif key == pg.K_PERIOD:
                current_string += '>'
            elif key == pg.K_MINUS:
                current_string += '_'
            elif key == pg.K_EQUALS:
                current_string += '+'
            else:
                current_string += chr(key).upper()   
        else:
            current_string += chr(key)

    return current_string