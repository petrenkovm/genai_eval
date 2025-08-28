import soundfile as sf
import numpy as np
from pathlib import Path

fs = 16000
duration = 2.0  # сек
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

# Чистый тон (A4 = 440 Гц)
tone = 0.5 * np.sin(2 * np.pi * 440 * t)

# Папка для сохранения
audio_dir = Path("data/audio")
audio_dir.mkdir(parents=True, exist_ok=True)

# Эталонный файл
sf.write(audio_dir / "reference.wav", tone, fs)

# "Сгенерированный" — с шумом
noise = tone + 0.05 * np.random.randn(len(t))
sf.write(audio_dir / "generated.wav", noise, fs)

print(f"Файлы сохранены в {audio_dir.resolve()}")
