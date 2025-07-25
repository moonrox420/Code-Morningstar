# Models Directory

This directory is for storing GGUF model files for Code Morningstar.

## Getting Started

1. Download a compatible GGUF model file:
   - Visit: https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF
   - Download a .gguf file (recommended: codellama-7b-instruct.Q4_K_M.gguf)

2. Place the model file in this directory

3. Update your `.env` file to point to the model:
   ```
   LLM_MODEL_PATH=models/your-model-file.gguf
   ```

## Supported Models

- CodeLlama models (recommended for code generation)
- Llama 2 models
- Any GGUF format model compatible with llama-cpp-python

## Notes

- Model files are excluded from git due to their large size
- The application will run in mock mode if no model is found
- Smaller quantized models (Q4_K_M) provide good performance with reasonable resource usage