#!/bin/bash
cd ${HOME}/patcher/src/
rm -f ${HOME}/patcher/src/latest.txt

if [ "$1" == "--remove" ]; then
	cd ${HOME}
	./patcher/uninstall.sh
fi

if [ "$1" == "--update" ]; then
	cd ${HOME}
	./patcher/upgradepatcher.sh
fi
if [ "$1" == "--nogui" ]; then
	python3 main.py ${HOME} 1 1
else
	python3 main.py ${HOME} 0 0 > log.txt
fi
