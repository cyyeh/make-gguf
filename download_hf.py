from huggingface_hub import snapshot_download


# use argparse to get model_id from command line
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model_id", type=str, required=True)
args = parser.parse_args()

snapshot_download(
    repo_id=args.model_id,
    local_dir=f"models/{args.model_id}",
    local_dir_use_symlinks=False,
    revision="main"
)
