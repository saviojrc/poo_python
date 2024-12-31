class AudioFile:
    
    def __init__(self, filename):
        self.ext = ''
        self.filename = filename
        if not filename.endswith(self.ext):
            raise Exception('Formato Inválido')

            