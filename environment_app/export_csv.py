import pandas as pd
from .models import Departamento, Hw, Ip, Modulo, Plataforma, Responsable, ResponsableSistema, Sistema, Submodulo, Sw

class DataFrameCreator:
    @staticmethod
    def create_dataframe(model):
        """
        Crea un DataFrame a partir de un modelo de Django.
        :param model: Clase del modelo de Django.
        :return: DataFrame con los datos del modelo.
        """
        return pd.DataFrame(list(model.objects.all().values()))