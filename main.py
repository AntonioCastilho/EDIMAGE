
from os import path
from PIL import Image, ImageEnhance


class EditorImagem():
    img = None
    img_formato = None
    img_local = None
    img_nome = None

    def restar():
        self.img = None
        self.img_formato = None
        self.img_local = None
        self.img_nome = None

    def carregar_img(self, imagem):
        try:
            self.img = Image.open(imagem)
            self.img_formato = self.img
            print('Image carregada')
            return True
        except:
            print('Falha ao carregar imagem.')
            return False

    def girar_img(self):
        pass

    def remover_cor(self):
        pass
