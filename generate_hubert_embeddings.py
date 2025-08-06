import os
import torchaudio
import torch
import torchaudio.transforms as T
from load_unlabeled_audio import get_unlabeled_audio_data


AUDIO_DIR = "/path/to/unlabeled_audio"
EMBEDDING_DIR = "./hubert_embeddings"
os.makedirs(EMBEDDING_DIR, exist_ok=True)

# HuBERT Base model (pretrained SSL)
bundle = torchaudio.pipelines.HUBERT_BASE
model = bundle.get_model().eval()

resampler = T.Resample(orig_freq=48000, new_freq=16000)  
to_mono = T.DownmixMono()

def preprocess_waveform(waveform, sample_rate):
    if sample_rate != 16000:
        waveform = resampler(waveform)
    if waveform.shape[0] > 1:
        waveform = to_mono(waveform)
    return waveform

def generate_embeddings(audio_files):
    for item in audio_files:
        path = item["path"]
        try:
            waveform, sample_rate = torchaudio.load(path)
            waveform = preprocess_waveform(waveform, sample_rate)

            with torch.inference_mode():
                features, _ = model(waveform)

            embedding_path = os.path.join(EMBEDDING_DIR, item["filename"].replace(".ogg", ".pt"))
            torch.save(features, embedding_path)
            print(f"Saved: {embedding_path}")

        except Exception as e:
            print(f"Error processing {path}: {e}")

if __name__ == "__main__":
    audio_data = get_unlabeled_audio_data(AUDIO_DIR)
    print(f"Found {len(audio_data)} files. Generating HuBERT embeddings...")
    generate_embeddings(audio_data)
