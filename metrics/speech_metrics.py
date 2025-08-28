from pystoi import stoi
import soundfile as sf
import numpy as np

def compute_stoi(ref_path, deg_path, fs=16000):
    ref, _ = sf.read(ref_path)
    deg, _ = sf.read(deg_path)
    return stoi(ref, deg, fs, extended=False)

def mos_placeholder():
    return "MOS требует субъективного тестирования, автоматизация частичная."
