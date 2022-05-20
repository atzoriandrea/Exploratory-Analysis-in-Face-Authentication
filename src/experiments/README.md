# Scripts description

## plot_TSNE_distribution.py parameters description
### This script plots your data in order to obtain a menagerie-related overview for you data
 - `--jsonsf` : path to the json file containing all annotations for your dataset
 - `--results` : path to .npy file containing the results obtained by pairs comparison
 - `--csv` : path of the .csv file in which all image pairs are listed

## features_merge.py 
This file contains a library function that returns a Pandas Dataframe with image embeddings and protected attributes for each image
 