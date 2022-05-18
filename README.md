# Exploratory-Analysis-in-Face-Authentication
<hr>

This is a Pytorch toolbox for Face Recognition training and testing. 
It provides a training part with various SOTA Face Recognition backbones and heads and
an evaluation part that:
- Provides evaluations of the given model(s) in order to obtain metrics like ROC curves, AUCs, EERs, EERs@FAR1% etc.
- Provides metrics as FAR and FRR variation across multiple factors like sex and ethnicity and their combinations
- Provides correlation between FAR/FRR and other sensitive/protected attributes in order to get meaningful explanations of what influences the trend of the cited metrics
- Provides Linear Regression modules in order to weight the given attributes accordingly to a given metric
<hr>

## License
<hr>
This repository is published under GNU GENERAL PUBLIC LICENSE, Version 3
<hr>


## Acknowledgements
<hr>
This work is greatly inspired by [FaceX-Zoo] (https://github.com/JDAI-CV/FaceX-Zoo/). We thank the authors a lot for their valuable efforts.
<hr>