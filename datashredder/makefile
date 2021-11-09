# By awesomelewis2007
# Github:https://github.com/awesomelewis2007/Datashreddermake
compile:
	gcc installer.c -o install_linux
	x86_64-w64-mingw32-gcc -g -o install_win.exe installer.c
run:
	echo "Linux Build"
	./install_linux
	echo "Windows Build"
	./install_win
	python3 datashredder.py