from fastapi import FastAPI
import uvicorn
import joblib 
from pydantic_types import InputPredict, OutputPredict  
import cloudpickle
app = FastAPI()

try:
    with open('./model.pkl', 'rb') as f:
        pipe = cloudpickle.load(f)
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    

@app.post("/predict", response_model=OutputPredict)
def predict(input_predict: InputPredict):
    probs = pipe.predict([[input_predict.Ingrese_la_carrera_que_estudia, input_predict.Ingrese_si_estudia_en_la_mañana_o_en_la_tarde, input_predict.Ingrese_la_ocupación_de_su_madre, input_predict.Lleva_el_pago_de_la_matricula_al_día, input_predict.Es_becario, input_predict.Que_edad_tiene, input_predict.Cual_es_número_de_créditos_matriculados_anuales_0_46, input_predict.Cuántas_evaluaciones_tiene_anualmente_0_72, input_predict.Cuántos_creditos_aprobados_anualmente_tiene_0_43, input_predict.Cual_es_la_nota_media_del_primer_año_de_estudio_0_20]])
    print(probs)
    return {'prediction': probs}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
