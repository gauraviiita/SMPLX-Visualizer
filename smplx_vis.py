import smplx
import torch
import numpy as np
import trimesh
import pyrender


model_path = "/media/local/robtic_arms/SMPL_FK/models"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = smplx.create(
    model_path,
    model_type="smplx",
    gender="neutral",
    use_pca=False,
    num_pca_comps=0,
    ext="npz",
    create_global_orient=True,
    create_body_pose=True,
    create_betas=True,
    create_left_hand_pose=True,
    create_right_hand_pose=True
).to(device)

print("Model loaded successfully!")

data = np.load("/media/local/robtic_arms/SMPL_FK/models/smplx/SMPLX_NEUTRAL.npz")
print(data["shapedirs"].shape)

print("Model expects", model.num_betas, "betas")

betas = torch.zeros(1, model.num_betas).to(device)
output = model(
    betas=betas,
    global_orient=torch.zeros(1, 3).to(device),
    body_pose=torch.zeros(1, 63).to(device),
    left_hand_pose=torch.zeros(1, 45).to(device),
    right_hand_pose=torch.zeros(1, 45).to(device)
)

vertices = output.vertices.detach().cpu().numpy().squeeze()
mesh = trimesh.Trimesh(vertices, model.faces, process=False)
scene = pyrender.Scene()
scene.add(pyrender.Mesh.from_trimesh(mesh))
pyrender.Viewer(scene, use_raymond_lighting=True)
