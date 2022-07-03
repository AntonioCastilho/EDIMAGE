
from os import path
from PIL import Image, ImageEnhance


class EditorImagem():
    img = None
    img_formato = None
    img_local = None
    img_nome = None
    img_ext = None

    def restar():
        self.img = None
        self.img_formato = None
        self.img_local = None
        self.img_nome = None

    def carregar_img(self, imagem):
        try:
            self.img = Image.open(imagem)
            self.img_formato = self.img.format
            self.img_local = path.dirname(path.realpath(imagem))
            self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
            print('Image carregada')
            return True
        except:
            print('Falha ao carregar imagem.')
            return False

    def girar_img(self, sentido='horario', angulo=90):
        if (sentido == 'horario'):
            self.img = self.img.rotate(angulo * -1)
        elif (sentido == 'anti-horario'):
            self.img = self.img.rotate(angulo)

    def remover_cor(self):
        converter = ImageEnhance.Color(self.img)
        self.img = converter.enhance(0)

    def salvar(self, local, nome_imagem):
        loc = local + '/' + nome_imagem + self.img_ext
        self.img.save(loc, self.img_formato)
        self.restar()


ed = EditorImagem()
