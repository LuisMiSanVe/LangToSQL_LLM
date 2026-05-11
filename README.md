> [See in spanish/Ver en español](https://github.com/LuisMiSanVe/LangToSQL_LLM/blob/main/README.es.md)

<img src="https://github.com/LuisMiSanVe/LuisMiSanVe/blob/main/Resources/LangToSQL/LangToSQLLLM_banner.png" style="width: 100%; height: auto;" alt="LangToSQL LLM Banner">

# 🤖 AI Model for PostgreSQL queries
[![image](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![image](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)](https://www.newtonsoft.com/json)
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-%23000040.svg?style=for-the-badge&logo=Hugging%20Face&logoColor=ffdf00)](https://huggingface.co/Komma-LuisMiSanVe)

>[!NOTE]
> Check out other versions of this program:
>- [WinForms](https://github.com/LuisMiSanVe/LangToSQL/tree/main)
>- [REST API](https://github.com/LuisMiSanVe/LangToSQL_API/tree/main) 
>- [ChatBot](https://github.com/LuisMiSanVe/LangToSQL_ChatBot/tree/main)
>- [NuGet](https://github.com/LuisMiSanVe/LangToSQL_NuGet/tree/main)
>- [Android](https://github.com/LuisMiSanVe/GeminiLiteSQL/tree/main)

The AI model has been trained for turning natural language to PostgreSQL queries.

## 📝 Technology Explanation
This model uses [Gwen Coder](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) as a base and then is fine tuned with [Spider](https://yale-lily.github.io/spider) datasets.

The `JSON` dataset file contains **Spider**'s `train_spider.json` as is the main dataset.

The model is exported to `GGUF` with [llama.cpp](https://github.com/ggml-org/llama.cpp) so it can be used by programs like [LM Studio](https://lmstudio.ai/).

## 🛠️ Setup
In order to execute the training script for your own, you first need to install [Python](https://www.python.org/) and run this command:
```
pip install transformers datasets peft accelerate bitsandbytes trl==1.0.0
```
Depending on the version, you may have to use this instead:
```
py -m pip install transformers datasets peft accelerate bitsandbytes trl==1.0.0
```

>[!IMPORTANT]
>Make sure the `TRL` library version is `1.0.0`, as is the only version supported by the trainer script.

## 📂 Files
This repository includes the trained LLM model's files (only in [HuggingFace](https://huggingface.co/Komma-LuisMiSanVe/LangToSQL) as the model is too big for Git LFS), its training script, the training dataset and a tester script to test the `.safetensors` model.

You can download the final `GGUF` in the [Releases](https://github.com/LuisMiSanVe/LangToSQL_LLM/releases).

## 🚀 Releases
The version will be released using these versioning policies:\
New major features and critical bug fixes will cause the immediate release of a new version, while other minor changes or fixes will wait one week since the time the change is introduced in the repository before being included in the new version, so that other potential changes can be added.
>[!NOTE]
>These potencial new changes will not increase the wait time for the new version beyond one week.

The version number will follow this format: \
\[Major Feature\].\[Minor Feature\].\[Bug Fixes\]

## 💻 Technologies Used
- Programming Language: [Python](https://www.python.org/)
- Libraries:
  - [transformers](https://pypi.org/project/transformers/)
  - [datasets](https://pypi.org/project/datasets/)
  - [peft](https://pypi.org/project/peft/)
  - [acceletare](https://pypi.org/project/accelerate/)
  - [bitsandbytes](https://pypi.org/project/bitsandbytes/)
  - [trl](https://pypi.org/project/trl/) (1.0.0)
- Other: 
  - [llama.cpp](https://github.com/ggml-org/llama.cpp)
  - [Gwen Coder](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
  - [Spider](https://yale-lily.github.io/spider)
- Recommended IDE: [VS Code](https://code.visualstudio.com/)
