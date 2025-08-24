from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective

import json

import sk_fiestas.utils as utl


def bienvenida_sk():
    bienvenida = utl.get_mensaje_sk('inicio_juego')
    instruccion = utl.get_mensaje_sk('ins_inicial')
    speech_text = f'{bienvenida} {instruccion}'

    return speech_text, get_directiva_apl(titulo=bienvenida, texto=instruccion, token='launchToken')



def conf_directiva_apl(file, token, datasources):
    try:
        with open(f'sk_fiestas/{file}', 'r') as apl_file:
            return RenderDocumentDirective(
                token=token,
                document= json.load(apl_file),
                datasources=datasources
            )
    except:
        return None


def get_directiva_apl(tipo='', titulo='', texto='', token=''):
    datasources = { 'preguntaData': {'text': titulo, 'subtext': texto}}
    file = 'JuegosFiesta.json'
        
    return conf_directiva_apl(file, token, datasources)