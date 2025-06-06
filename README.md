# Explaining Bias in Deep Face Recognition via Image Characteristics

This is the official repository of the paper entitled "Explaining Bias in Deep Face Recognition via Image Characteristics", 
published in: 2022 IEEE International Joint Conference on Biometrics (IJCB)
 
<br>
<div align="center">
 <img src="images/IJCB_logo-900x207.png"  width="750" alt="IJCB Logo"/> 
</div>
<br>

The original paper is available <a href="https://ieeexplore.ieee.org/abstract/document/10007937/" target="_blank">here</a>.

<br>
<div align="center">
 <img src="./images/overview.png"  width="750" alt="ROC curve Example"/> 
</div>
<br>

We provide a Pytorch toolbox for Face Recognition training and testing. 
It provides a training part with various SOTA Face Recognition backbones and heads and
an evaluation part that:
- Provides evaluations of the given model(s) in order to obtain metrics like ROC curves, AUCs, EERs, EERs@FAR1%, etc.
<br>
<div align="center">
 <img src="./images/ROC.png" height="250" width="250" alt="ROC curve Example"/> <img src="./images/EER.png" height="250" width="250" alt="EER graph Example"/>
</div>
<br>

- Provides metrics as FAR and FRR variation across multiple factors like sex and ethnicity and their combinations
<br>
<div align="center">
 <img src="images/net1.png"  height="130" width="420" alt="Table Example 1"/> <img src="images/net2.png"  height="130" width="420" alt="Table Example 2"/>
</div>
<br>

- Provides correlation between FAR/FRR and other sensitive/protected attributes in order to get meaningful explanations of what influences the trend of the cited metrics
<br>
<div align="center">
 <img src="images/corr.png"  width="750" alt="Correlation Example"/> 
</div>
<br>
- Provides Linear Regression modules in order to weight the given attributes accordingly to a given metric

## Dataset
 Here we provide two <a href="https://drive.google.com/drive/folders/1LNLOO157NPUOAfCWDtMxJpmDVkbn8eu4?usp=sharing" target="_blank">Datasets</a>
 (DiveFace, VGG-Face2 test set) annotated with a lot of attributes. Namely:
age, smile, moustache, beard, sideburns, mask, headWear, glasses, head_roll, head_yaw, head_pitch, eye_makeup, lip_makeup, forehead_occluded, eye_occluded, mouth_occluded, blur, exposure, noise

## Requirements
- Python >= 3.7
- PyTorch >= 1.10.0
- DeepFace == 0.0.72
- MatPlotLib == 3.5.2
- Scikit Learn == 1.0.1
- Scipy == 1.7.1
- Seaborn == 0.11.2

In order to install all the necessary prerequisites, you can simply execute the following command: \
`pip install -r requirements.txt`

## Model Training
See <a href="training/README.md" target="_blank">README</a> in <a href="training" target="_blank">training folder</a>

## Dataset Preprocessing and combined models training
See <a href="src/README.md" target="_blank">README</a> in <a href="src" target="_blank">src</a> folder

## Model Evaluation
See <a href="src/experiments/README.md" target="_blank">README</a> in <a href="src/experiments" target="_blank">src/experiments</a> folder


## Contributing
This code is provided for educational purposes and aims to facilitate reproduction of our results, and further research in this direction. We have done our best to document, refactor, and test the code before publication.

If you find any bugs or would like to contribute new models, training protocols, etc, please let us know.

Please feel free to file issues and pull requests on the repo and we will address them as we can.

## License

This code is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This software is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for details.

You should have received a copy of the GNU General Public License along with this source code. If not, go the following link: http://www.gnu.org/licenses/.



## Acknowledgements

This work is greatly inspired by <a href="https://github.com/JDAI-CV/FaceX-Zoo/" target="_blank">FaceX-Zoo</a>. We thank the authors a lot for their valuable efforts.

