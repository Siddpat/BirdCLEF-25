# Bird Sound Classification for BirdCLEF'25

This repository contains the code and methodology developed during my remote research internship with Nanyang Technological University (NTU), Singapore. The project focuses on leveraging the HuBERT model to generate audio embeddings for bird sound classification as part of the BirdCLEF'25 challenge.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 📖 About The Project

# Competition Context

This competition is part of the ongoing efforts to enhance biodiversity monitoring in the El Silencio Natural Reserve, located in the lowlands of the Magdalena Valley of Colombia. This region is a biodiversity hotspot facing severe threats, with over 70% of its lowland rainforests replaced by pastures for cattle ranching.

El Silencio Natural Reserve protects 5,407 acres of tropical lowland forests and wetlands, home to diverse wildlife including 295 bird species, 34 amphibian species, 69 mammal species, 50 reptile species, and nearly 500 plant species. A significant portion of the reserve is undergoing ecological restoration after previously being used for extensive livestock farming.

# BirdCLEF+ 2025 Dataset Description
The BirdCLEF+ 2025 competition presents a multi-taxonomic bioacoustic challenge focused on identifying various species (birds, amphibians, mammals, and insects) from audio recordings made in El Silencio Natural Reserve, Colombia. This competition expands beyond previous BirdCLEF challenges by including multiple taxonomic groups rather than focusing solely on birds.

# Competition Overview
Our task is to develop machine learning models that can accurately identify 206 different species from their acoustic signatures in soundscape recordings. This competition uses a hidden test set for evaluation, with the actual test data being made available to your notebook only during submission scoring.

# Dataset Components
## 1. Training Data
The training dataset consists of:

Individual Species Recordings (train_audio/):

Short audio clips of individual species vocalizations

Sourced from three collections:

Xeno-canto.org (birds)

iNaturalist (various taxonomic groups)

Colombian Sound Archive (CSA) of the Humboldt Institute

All files resampled to 32 kHz and converted to OGG format

Filenames follow the pattern: [collection][file_id_in_collection].ogg

## 2. Metadata (train.csv):

primary_label: Species identifier code (eBird code for birds, iNaturalist taxon ID for non-birds)

secondary_labels: Additional species that may appear in the recording

latitude & longitude: Geographic coordinates of the recording

author: Name of the user who provided the recording

filename: Name of the associated audio file

rating: Quality rating (1-5 scale, with 0 indicating no rating available)

collection: Source collection (XC, iNat, or CSA)

## 3. Unlabeled Soundscapes (train_soundscapes/):

Unlabeled audio from the same general recording locations as the test data

Filenames follow the pattern: [site]_[date]_[local_time].ogg

These recordings do NOT overlap with the exact recording sites of the test data

Can be used for semi-supervised learning approaches



## 🚀 Methodology & My Contributions

My work was divided into three core stages, moving from raw data to trainable embeddings.

### 1. Audio Data Pre-processing

The initial stage focused on preparing the raw audio data from the HSN (Hawaii, Sand-network) dataset for training. This involved cleaning and standardizing the audio files to ensure consistency.

* **Augmentations:** Applied various augmentations to the raw audio to increase the diversity of the training data and improve model robustness.
* **Chunking:** Processed and split the augmented audio files into uniform **30-second intervals**, which is a standard input format for many audio processing models.

> **The code for this entire pre-processing pipeline can be found in [this file](load_unlabeled_audio.py).**

### 2. HuBERT Training Pipeline

I worked on the core training pipeline responsible for fine-tuning the HuBERT model on the prepared audio data. HuBERT (Hidden-Unit BERT) is a self-supervised model that learns powerful representations of audio directly from the raw waveform, making it ideal for this task.

> **The implementation of the HuBERT training pipeline is located in [this file](Hubertpipeline.ipynb).**

### 3. Embedding Generation

Using the trained pipeline, I processed the entire HSN dataset to generate high-quality audio embeddings. These embeddings capture the complex features of the bird calls and serve as the direct input for a downstream classification model.

* **Dataset:** HSN (Hawaii, Sand-network) from BirdCLEF'25.
* **Output:** A set of feature vectors (embeddings) ready for training a classifier like a simple Neural Network or a more advanced EAT (Efficient Audio Transformer) model.

> **The script used to generate the final embeddings is available here: [embedding_generation.py](generate_hubert_embeddings.py).**

---

## ✨ Key Technologies

* Python
* PyTorch
* Hugging Face Transformers (for HuBERT)
* Librosa and TorchAudio (for audio processing)
* Pandas & NumPy

This competition represents an important step in developing tools to monitor biodiversity in tropical ecosystems, with potential applications for conservation efforts worldwide.
