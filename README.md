# Repository for NLP Class Submission

## Changelog

- **January 31, 2025**: Added `findBigrams` to `ResidencyDay1` folder
- **February 2, 2025**: Added `translate_diff.py` for text translation and difference analysis

## Instructions

1. Clone the repository to your local machine:
    ```sh
    git clone <repository-url>
    ```
2. Open a terminal and navigate to the `ResidencyDay1` folder:
    ```sh
    cd <repository-folder>/ResidencyDay1
    ```
3.  **For Bigram Analysis:** Run the script for bigram analysis:
    ```sh
    python3 findBigram.py
    ```
4.  **For Translation and Difference Analysis:** Run the script for translation and difference analysis:
    ```sh
    # Install required library
    pip install googletrans==4.0.0rc1 deep-translator
    # Run the script
    python3 translate_diff.py
    ```