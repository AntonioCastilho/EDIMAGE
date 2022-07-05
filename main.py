from io import BytesIO
from os import terminal_size
from unicodedata import name
from editor import ed
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage  # Textura da imagem
from kivy.uix.image import Image  # Para exibir imagens
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition

Window.clearcolor = .92, .92, .92, 1

Builder.load_file('kvlang.kv')


class Geral():
    def mudar_tela(self, nome_tela, tipo_transicao='Slide', direcao='left'):
        if (tipo_transicao == 'Slide'):
            self.manager.transition = SlideTransition()
        else:
            self.manager.transition = NoTransition()
        self.manager.transition.direction = direcao
        self.manager.current = nome_tela


class TelaInicial(Screen, Geral):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_dropfile=self.soltou)

    def alterar_mensagem(self, texto):
        lb = self.ids.mensagem
        lb.text = texto

    def soltou(self, window, caminho_arquivo):
        ca = caminho_arquivo.decode('utf-8')
        if (ed.carregar_img(ca) == False):
            self.alterar_mensagem('[b]Imagem invalida[/b] tente de novo')
        else:
            tela_edicao = self.manager.get_screen('tela_edicao')
            tela_edicao.exibir_imagem()
            self.mudar_tela('tela_edicao')


class TelaEdicao(Screen, Geral):
    def exibir_imagem(self):
        area_imagem = self.ids.area_imagem
        area_imagem.clear_widgets()
        img_buffer = BytesIO()
        ed.img.save(img_buffer, format=ed.img_formato)
        img_buffer.seek(0)  # ponto de referencia inicial

        co = CoreImage(img_buffer, ext=ed.img_formato.lower())
        textura = co.texture
        img_buffer.close()

        img_buffer.close()

        img = Image()
        img.texture = textura
        area_imagem.add_widget(img)

    def bt_girar_anti_horario(self):
        ed.girar_img('anti_horario')
        self.exibir_imagem()

    def bt_girar_horario(self):
        ed.girar_img('horario')
        self.exibir_imagem()

    def bt_pb(self):
        ed.remover_cor()
        self.exibir_imagem()

    def bt_cancelar(self):
        tela_inicial = self.manager.get_screen('tela_inicial')
        tela_inicial.alterar_mensagem('[b]Arraste a imagem para cá')
        self.mudar_tela('tela_inicial', 'No')
        ed.resetar()


sm = ScreenManager()
sm.add_widget(TelaInicial(name='tela_inicial'))
sm.add_widget(TelaEdicao(name='tela_edicao'))


class Programa(App):
    title = 'Check-in'

    def build(self):
        return sm


if __name__ == '__main__':
    Programa().run()
