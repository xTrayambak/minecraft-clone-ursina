import pyglet
from pyglet.media import load, StaticSource, StreamingSource

pyglet.options["audio"] = ('openal', 'directsound', 'pulse', 'silent')



class AudioPlayer:
    def __init__(self):
        self.cache = {}
        
    def cacheExistsForSound(self, sound):
        try:
            return True, self.cache[sound]
        except KeyError:
            return False, None
        
    def load(self, path):
        source = None
        cacheExists, cachedSound = self.cacheExistsForSound(path)
        if cacheExists and cachedSound:
            source = cachedSound
        else:
            source = load(path, streaming=False)
        
        return source
        
    def play(self, _src):
        _src.play()
        
