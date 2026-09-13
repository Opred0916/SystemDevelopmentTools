.PHONY: all clean

all: stats.txt report.txt

stats.txt: data.csv stats.py
	python stats.py

report.txt: report.md stats.txt build_report.py
	python build_report.py

clean:
	del /Q stats.txt report.txt 2>nul || exit 0