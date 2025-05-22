#CÓDIGO DE LA CLASE "BOTÓN"
import pygame

class button: #DEFINIMOS LA CLASE  
    def __init__(self, texto, pos, tamaño, fuente, color_fondo, color_texto, color_hover=None, accion=None):
        #PARÁMETROS DE LA CLASE
        self.texto=texto
        self.pos=pos
        self.tamaño=tamaño
        self.fuente=fuente
        self.color_fondo=color_fondo
        self.color_texto=color_texto
        self.color_hover=color_hover or color_fondo
        self.accion=accion

        self.rect=pygame.Rect(pos,tamaño)#CREAMOS UN RECTÁNGULO INVISIBLE QUE REPRESENTA EL ÁREA DE CLICK DEL BOTÓN

        self.hovered=False #VARIABLE POR DEFECTO QUE INDICA QUE EL BOTÓN NO TIENE EL MOUSE ENCIMA

        self.superficie_texto=self.fuente.render(self.texto, True, self.color_texto) #CREAMOS UNA "IMAGEN" DEL TEXTO QUE QUEREMOS QUE TENGA EL BOTÓN
        self.texto_rect=self.superficie_texto.get_rect(center=self.rect.center) #OBTIENE EL CENTRO DE LA "IMAGEN" CREADA EN LA LÍNEA ANTERIOR Y HACE QUE EL TEXTO QUEDE CENTRADO DENTRO DEL BOTÓN

    #FUNCIÓN PARA HACER APARECER EL BOTÓN EN NUESTRA INTERFAZ
    def dibujar(self, superficie): #PARÁMETRO SUPERFICIE RECIBE UNA SUPERFICIE EN LA CUAL SE DIBUJARÁ EL BOTÓN
        color=self.color_hover if self.hovered else self.color_fondo #EL COLOR CAMBIA SI EL MOUSE ESTÁ ENCIMA DEL BOTÓN O NO
        pygame.draw.rect(superficie,color, self.rect, border_radius=8) #DIBUJA UN RECTÁNGULO DE BORDES REDONDEADOS (EL BOTÓN) SOBRE LA SUPERFICIE INDICADA
        superficie.blit(self.superficie_texto, self.texto_rect) #PEGA EL TEXTO ENCIMA DEL BOTÓN, TAMBIÉN EN ESA MISMA SUPERFICIE
    
    def actualizar(self, event_list): #FUNCIÓN QUE DETECTA SI EL MOUSE ESTÁ SOBRE EL BOTÓN Y SI EL BOTÓN FUE PRESIONADO
        pos_mouse=pygame.mouse.get_pos() #OBTIENE LAS CORDENADAS (x,y) DEL MOUSE
        self.hovered=self.rect.collidepoint(pos_mouse) #GUARDA TRUE O FALSE EN LA VARIABLE QUE DETERMINA SI EL MOUSE ESTÁ SOBRE EL BOTÓN O NO

        for evento in event_list: #SE RECORRE CADA EVENTO QUE OCURRE EN EL JUEGO
            if evento.type==pygame.MOUSEBUTTONDOWN and self.hovered: #EN CASO DE QUE EL EVENTO SEA EL CLICK DEL MOUSE Y ADEMÁS EL CLICK ESTÉ ENCIMA DEL BOTÓN, SE EJECUTARÁ LA ACCIÓN LIGADA AL BOTÓN
                if self.accion:
                    self.accion()