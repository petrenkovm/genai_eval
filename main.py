import argparse
import yaml
import sys

# Импортируем функции метрик
from metrics.text_metrics import compute_bleu, compute_rouge
from metrics.image_metrics import compute_fid
from metrics.speech_metrics import compute_stoi, mos_placeholder

def main():
    # --- 1. Аргументы командной строки ---
    parser = argparse.ArgumentParser(description="GenAI Evaluation Script")
    parser.add_argument("--config", type=str, default="config.yaml", help="Путь к config.yaml")
    parser.add_argument("--task", type=str, choices=["text", "image", "speech"], required=True, help="Тип задачи")
    args = parser.parse_args()

    # --- 2. Читаем конфиг в UTF-8 ---
    try:
        with open(args.config, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        sys.exit(f"[ОШИБКА] Файл конфигурации {args.config} не найден.")
    except yaml.YAMLError as e:
        sys.exit(f"[ОШИБКА] Ошибка чтения YAML: {e}")

    # --- 3. Логика выбора задачи ---
    if args.task == "text":
        refs = config.get("references", [])
        cands = config.get("candidates", [])
        if not refs or not cands:
            sys.exit("[ОШИБКА] В config.yaml нет данных для текстовой оценки.")
        
        print("=== Текстовые метрики ===")
        bleu = compute_bleu(refs, cands)
        rouge = compute_rouge(refs, cands)
        print(f"BLEU: {bleu:.4f}")
        print(f"ROUGE: {rouge}")

    elif args.task == "image":
        real_path = config.get("real_path")
        fake_path = config.get("fake_path")
        if not real_path or not fake_path:
            sys.exit("[ОШИБКА] В config.yaml не заданы пути для изображений.")
        
        print("=== Изображения ===")
        fid_score = compute_fid(real_path, fake_path)
        print(f"FID: {fid_score:.4f}")

    elif args.task == "speech":
        ref_audio = config.get("ref_path")
        deg_audio = config.get("deg_path")
        if not ref_audio or not deg_audio:
            sys.exit("[ОШИБКА] В config.yaml не заданы пути для аудио.")

        print("=== Речь ===")
        stoi_score = compute_stoi(ref_audio, deg_audio)
        mos_score = mos_placeholder()
        print(f"STOI: {stoi_score:.4f}")
        print(f"MOS: {mos_score}")

if __name__ == "__main__":
    main()
