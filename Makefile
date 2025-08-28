PYTHON=python
MAIN=main.py
CONFIG=config.yaml

.PHONY: eval_text eval_image eval_speech clean

eval_text:
		$(PYTHON) $(MAIN) --config $(CONFIG) --task text

eval_image:
		$(PYTHON) $(MAIN) --config $(CONFIG) --task image

eval_speech:
		$(PYTHON) $(MAIN) --config $(CONFIG) --task speech

clean:
		@echo "Cleaning..."
		@if exist __pycache__ rmdir /s /q __pycache__
