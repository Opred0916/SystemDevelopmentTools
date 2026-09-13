.PHONY: check build clean

check:
	"D:/Git/bin/bash.exe" check.sh

build:
	python -m build --wheel

clean:
	python -c "import shutil; [shutil.rmtree(p, ignore_errors=True) for p in ['build', 'dist']]; shutil.rmtree('src/greetlab_25040031075.egg-info', ignore_errors=True)"