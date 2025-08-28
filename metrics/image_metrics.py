import subprocess

def compute_fid(real_path, fake_path):
    """Ожидается путь к папкам с изображениями"""
    cmd = ["pytorch-fid", real_path, fake_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip().split()[-1])

# IS можно реализовать через PyTorch и Inception-v3
