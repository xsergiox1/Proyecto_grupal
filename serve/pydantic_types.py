from pydantic import BaseModel


class InputPredict(BaseModel):
    Ingrese_la_carrera_que_estudia: int
    Ingrese_si_estudia_en_la_mañana_o_en_la_tarde: int
    Ingrese_la_ocupación_de_su_madre: int
    Lleva_el_pago_de_la_matricula_al_día: int
    Es_becario: int
    Que_edad_tiene: int
    Cual_es_número_de_créditos_matriculados_anuales_0_46: int
    Cuántas_evaluaciones_tiene_anualmente_0_72: int
    Cuántos_creditos_aprobados_anualmente_tiene_0_43: int
    Cual_es_la_nota_media_del_primer_año_de_estudio_0_20: float


class OutputPredict(BaseModel):
    prediction: int   #####

# 0 = No_Drop_out
# 1= Drop_Out


