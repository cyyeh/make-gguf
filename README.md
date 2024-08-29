## Steps

0. install requirements: `poetry install`
1. run download_hf.py: `poetry run python download_hf.py --model_id <model_id>`
2. run convert_hf_to_gguf.py: `poetry run python convert_hf_to_gguf.py <model_dir> --outfile <outfile> --outtype <outtype>`

## References

- [將 Hugging Face 上的模型安裝到 OLlama](https://hackmd.io/@flagmaker/HkQHhlYyA?utm_source=preview-mode&utm_medium=rec)
- https://github.com/ggerganov/llama.cpp/discussions/2948
- https://github.com/ggerganov/llama.cpp/blob/master/convert_hf_to_gguf.py
- https://github.com/RUCKBReasoning/codes
