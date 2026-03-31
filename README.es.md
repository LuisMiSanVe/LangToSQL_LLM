> [Ver en ingles/See in english](https://github.com/LuisMiSanVe/LangToSQL_LLM/blob/main/README.md)

<img src="https://github.com/LuisMiSanVe/LuisMiSanVe/blob/main/Resources/LangToSQL/LangToSQLLLM_banner.png" style="width: 100%; height: auto;" alt="LangToSQL LLM Banner">

# 🤖 Modelo de IA para sentencias PostgreSQL
[![image](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![image](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)](https://www.newtonsoft.com/json)
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-%23000040.svg?style=for-the-badge&logo=Hugging%20Face&logoColor=ffdf00)](https://huggingface.co/Komma-LuisMiSanVe)

>[!NOTE]
> Dale un vistazo a las otras versiones del programa:
>- [WinForms](https://github.com/LuisMiSanVe/LangToSQL/tree/main)
>- [REST API](https://github.com/LuisMiSanVe/LangToSQL_API/tree/main) 
>- [ChatBot](https://github.com/LuisMiSanVe/LangToSQL_ChatBot/tree/main)
>- [NuGet](https://github.com/LuisMiSanVe/LangToSQL_NuGet/tree/main)
>- [Android](https://github.com/LuisMiSanVe/GeminiLiteSQL/tree/main)

El modelo de IA ha sido entrenado para convertir lenguaje natural a sentencias de PostgreSQL.

## 📝 Explicación de Tecnología
El modelo usa [DeepSeek Coder](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base) de base y refinado con los datasets de [Spider](https://yale-lily.github.io/spider).

El dataset en archivo `JSON` contiene `train_spider.json` de **Spider**, ya que es el dataset principal.

El modelo se puede exportar a `GGUF` con [llama.cpp](https://github.com/ggml-org/llama.cpp) para que puedas usarlo en programas como [LM Studio](https://lmstudio.ai/).

## 🛠️ Instalación
Para ejecutar el script de entrenamiento por tu cuenta, primero necesitas instalar [Python](https://www.python.org/) y ejecuta este comando:
```
pip install transformers datasets peft accelerate bitsandbytes trl
```
Dependiendo en la versión, es posible que necesites usar este en su lugar:
```
py -m pip install transformers datasets peft accelerate bitsandbytes trl
```

## 📂 Archivos
Este repositorio incluye los archivos del modelo LLM entrenado (solo en [HuggingFace](https://huggingface.co/Komma-LuisMiSanVe/LangToSQL) ya que el modelo es demasiado grande para Git LFS), su script de entrenamiento y el dataset para entrenar.

Puedes descargar el `GGUF` final desde los [Lanzamientos](https://github.com/LuisMiSanVe/LangToSQL_LLM/releases).

## 🚀 Lanzamientos
Una versión será lanzada solo cuando se cumplan los siguientes puntos:\
Nuevas funciones importantes y arreglos de fallos criticos causarán la salida inmediata de una nueva versión, mientras que otros cambios/arreglos menores deberán esperar una semana desde que se incluyeron en el repositorio antes de ser incluidos en la nueva versión, para que otros posibles cambios puedan ser añadidos tambien.
>[!NOTE]
>Estos posibles nuevos cambios no alargarán la espera de la salida de la nueva versión a más de una semana.

El número de la versión seguirá este formato: \
\[Añadido Importante\].\[Añadido Menor\].\[Arreglos de Errores\]

## 💻 Tecnologías usadas
- Lenguaje de programación: [Python](https://www.python.org/)
- Librerías:
  - [transformers](https://pypi.org/project/transformers/)
  - [datasets](https://pypi.org/project/datasets/)
  - [peft](https://pypi.org/project/peft/)
  - [acceletare](https://pypi.org/project/accelerate/)
  - [bitsandbytes](https://pypi.org/project/bitsandbytes/)
  - [trl](https://pypi.org/project/trl/)
- Otros:
  - [llama.cpp](https://lmstudio.ai/)
  - [DeepSeek Coder](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base)
  - [Spider](https://yale-lily.github.io/spider)
- IDE Recomendado: [VS Code](https://code.visualstudio.com/)
