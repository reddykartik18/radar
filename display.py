import sys
import sdl2
import sdl2.ext

class Display(object):
    def __init__(self, W, H):
        sdl2.ext.init()
        self.w, self.h = W, H
        self.window = sdl2.ext.Window("radar",
                                      size=(W, H),
                                      position=(-500, -500))
        self.window.show()
        self.surface = self.window.get_surface()

    def paint(self, img):
        # junk
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                sdl2.ext.quit()
                sys.exit(0)
        # draw
        surf = sdl2.ext.pixels3d(self.surface)
        surf[:, :, 0:3] = img.swapaxes(0,1)
        
        # window update
        self.window.refresh()

