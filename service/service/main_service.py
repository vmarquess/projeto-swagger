import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
# import numpy as np


class BinaryService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):

        """"
        Carrega o serviço a ser usado
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        response_predicts = self.toBinary(texts['textoMensagem'])

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as conversões em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['binary result'] = response_predicts

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {"listaBinario": json.loads(df_response.to_json(orient='records', force_ascii=False))}

        return response

    def toBinary(self, texts):

        output = []

        for text in texts:

            ascii_list = []
            response = []

            for i in text:
                # ord retorna o valor ASCII correspondente
                ascii_list.append(ord(i))
            for i in ascii_list:
                response.append(int(bin(i)[2:]))
            output.append(response)

        return output
