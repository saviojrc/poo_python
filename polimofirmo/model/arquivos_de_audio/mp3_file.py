from polimofirmo.model.arquivos_de_audio.audio_file import AudioFile

class MP3File(AudioFile):

    def __init__(self, filename):
        super().__init__(filename)
        self.ext = 'mp3'


    def play(self):
        print('tocando aquivo mp3')