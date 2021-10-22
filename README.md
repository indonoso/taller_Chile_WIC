# Taller Chile WIC por Plataforma Telar

## Estructura
El taller tiene cuatro partes. Si se quedan atrasadas en alguna no se preocupen, la carpeta con el número del paso tiene todo lo que debería tener como código al final de la etapa.

El archivo `dataset_ejemplo.csv` tiene los datos que usaremos y el archivo `visualization.ipynb` tiene un template básico para iniciar. No es necesario que lo usen si no quieren.

## Requerimientos

1. Habilitar una cuenta en [Google Cloud Platform](https://cloud.google.com/). Deben crear un proyecto con permisos de facturación, lo que significa que deben poner el número de una tarjeta de crédito. El servicio que usaremos tiene una capa gratuita así que seguro que no va a facturar con el uso que le den en el taller. Si no pueden realizar este paso solo no podrán ejecutar el último paso del taller, no se preocupen ;).
2. Tener instalado Jupyter notebook/lab o usar Colab
3. Instalar las siguientes librerías:
	```
	altair==4.1.0
	Flask==2.0.2
	gunicorn==20.1.0
	pandas==1.1.5
	```
4. Opcional:
   1. Instalar y configurar [`docker`](https://docs.docker.com/engine/install/)
   2. Instalar [`gcloud`](https://cloud.google.com/sdk/docs/install) y configurarlo
