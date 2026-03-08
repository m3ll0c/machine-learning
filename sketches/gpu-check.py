import torch
import tensorflow as tf

print("PyTorch GPU:", torch.cuda.is_available())

print("TF GPU:", len(tf.config.list_physical_devices("GPU")) > 0)