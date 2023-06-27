# By lewisevans2007
# Github:https://github.com/lewisevans2007/Datashreddermake
compile-all:
	gcc installer.c -o install_linux
	x86_64-w64-mingw32-gcc -g -o install_win.exe installer.c
	gcc help.c -o help_linux
	x86_64-w64-mingw32-gcc -g -o help_win.exe help.c
run:
	echo "Linux Build"
	./install_linux
	echo "Windows Build"
	./install_win
	python3 datashredder.py