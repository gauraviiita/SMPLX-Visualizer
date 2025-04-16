# SMPLX-Visualizer

## Requirements

```
pip install git+https://github.com/vchoutas/smplx.git

pip install numpy==1.26.4

pip install chumpy pyrender trimesh matplotlib

if you have GPU + CUDA 11.8

conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

```

Download the SMPLX Neutral model 2020

[SMPL-X](https://smpl-x.is.tue.mpg.de/download.php)

SMPL-X 2020
The neutral SMPL-X model with the FLAME 2020 expression blendshapes:

[Link](https://download.is.tue.mpg.de/download.php?domain=smplx&sfile=SMPLX_NEUTRAL_2020.npz)


Run the code 
```
python smplx_vis.py 
```
![Screenshot from 2025-04-16 12-33-44](https://github.com/user-attachments/assets/f8e5d445-d6a1-4d15-8b8f-ff2b93459702)


