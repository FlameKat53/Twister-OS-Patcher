#!/bin/bash
rm -f ${HOME}/patcher/src/latestui.txt
if [ "$1" == "--remove" ]; then
	cd ${HOME}
	./patcher/uninstall.sh
fi

if [ "$1" == "--update" ]; then
	cd ${HOME}
	./patcher/upgradepatcher.sh
fi

if [ "$1" == "--nogui" ]; then
	cd ${HOME}/patcher/src/
	python3 main.py ${HOME} 1 1
fi

if [ "$1" == "" ]; then
	cd ${HOME}/patcher/src/
	python3 main.py ${HOME} 0 0 > log.txt
fi
