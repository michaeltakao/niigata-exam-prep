PANDOC      = pandoc
TEMPLATE    = templates/niigata-exam.latex
PDF_DIR     = pdf
MATH_SRC    = $(wildcard 08_math/textbook/M*.md)
PHYSICS_SRC = $(wildcard 09_physics/textbook/P*.md)

PANDOC_FLAGS = \
  --pdf-engine=xelatex \
  --template=$(TEMPLATE) \
  --toc \
  --number-sections \
  -V geometry:a4paper \
  -V date:"$(shell date +%Y年%m月%d日)" \

.PHONY: all math physics drills clean check status coach analyze

all: math physics

math: $(PDF_DIR)/math-guide.pdf

physics: $(PDF_DIR)/physics-guide.pdf

$(PDF_DIR)/math-guide.pdf: $(MATH_SRC) $(TEMPLATE) | $(PDF_DIR)
	$(PANDOC) $(PANDOC_FLAGS) \
	  -V title:"数学 対策ガイド" \
	  $(MATH_SRC) \
	  -o $@
	@echo "✓  $@ 生成完了"

$(PDF_DIR)/physics-guide.pdf: $(PHYSICS_SRC) $(TEMPLATE) | $(PDF_DIR)
	$(PANDOC) $(PANDOC_FLAGS) \
	  -V title:"物理 対策ガイド" \
	  $(PHYSICS_SRC) \
	  -o $@
	@echo "✓  $@ 生成完了"

$(PDF_DIR):
	mkdir -p $(PDF_DIR)

drills:
	@echo "ドリルPDFは個別ターゲットで生成してください: make math-drills / make physics-drills"

math-drills: $(PDF_DIR)/math-drills.pdf

$(PDF_DIR)/math-drills.pdf: $(wildcard 08_math/drills/M*.md) $(TEMPLATE) | $(PDF_DIR)
	$(PANDOC) $(PANDOC_FLAGS) \
	  -V title:"数学 類題ドリル" \
	  $^ \
	  -o $@

physics-drills: $(PDF_DIR)/physics-drills.pdf

$(PDF_DIR)/physics-drills.pdf: $(wildcard 09_physics/drills/P*.md) $(TEMPLATE) | $(PDF_DIR)
	$(PANDOC) $(PANDOC_FLAGS) \
	  -V title:"物理 類題ドリル" \
	  $^ \
	  -o $@

check:
	@pandoc --version | head -1
	@xelatex --version 2>/dev/null | head -1 || echo "xelatex: not found (要: brew install basictex)"
	@echo "MATH_SRC: $(MATH_SRC)"
	@echo "PHYSICS_SRC: $(PHYSICS_SRC)"

status:
	@python3 scripts/report.py

coach:
	@python3 scripts/coach.py

analyze:
	@python3 scripts/analyze_mock.py

clean:
	rm -f $(PDF_DIR)/*.pdf
