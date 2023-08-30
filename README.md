# Spotify Playlist Continuation with PMI Methodology

## Overview

This project aims to offer an approach to automatic playlist continuation using the Pointwise Mutual Information (PMI) algorithm. While many current solutions use more complex machine learning algorithms, like neural networks or gradient boosting, this project shows that a simpler statistical model can perform competitively.

## Features

- Efficient playlist continuation recommendations
- Competitively high scores on standard metrics (R Precision, NCDG, Clicks)
- Works with a large dataset of 1,000,000 Spotify playlists created from 2010-2017

## Setup

1. Clone the repository to your local machine.
2. Download spotify data from competition website
3. Look at million.ipynb and model_evaluation.ipynb to execute the PMI algorithm on the dataset.

## Research Findings

Our method remains competitive among solutions that employ higher-level methodologies. We achieved a placement of 38th out of 4,699 submissions in the public competition.

Despite limitations like not considering playlist titles and genre information, our method proves to be a strong, valid playlist continuation process.

The methodology and findings are documented comprehensively in the accompanying LaTeX paper.

## References

For more information, please consult our [paper](https://drive.google.com/drive/folders/1_teHtBJQ01X_kNjjwCgSSAUv6lRNdAoi).
