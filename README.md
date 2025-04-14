# BirdCLEF-25
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

## 4. Taxonomy Information (taxonomy.csv):

Data on the different species

Includes iNaturalist taxon ID and class name (Aves, Amphibia, Mammalia, Insecta)

Location Information (recording_location.txt):

High-level information about El Silencio Natural Reserve

## 5. Test Data
The test dataset (test_soundscapes/) consists of:

Approximately 700 one-minute recordings in OGG format (32 kHz)

Filenames are randomized with the pattern soundscape_xxxxxx.ogg

These recordings are used for scoring your model's performance

Not all species from the training data appear in the test data

# Submission Format
The sample submission file (sample_submission.csv) includes:

row_id: Identifier in the format soundscape_[soundscape_id]_[end_time]

Example: Segment 00:15-00:20 of soundscape_12345.ogg has row ID soundscape_12345_20

[species_id]: 206 columns, one for each species

We must predict the probability (0-1) of each species' presence in each 5-second segment

# Technical Considerations
The audio files are sampled at 32 kHz, meaning each second of audio contains 32,000 samples

The test predictions are made on 5-second segments of the 1-minute test recordings

The submitted notebook must complete inference within the competition time limits

GPU notebook submissions are disabled (or limited to 1 minute runtime)

CPU notebooks have a maximum runtime of 90 minutes

This competition represents an important step in developing tools to monitor biodiversity in tropical ecosystems, with potential applications for conservation efforts worldwide.
