@echo off
echo NoobNote Compiler
pyinstaller -w - i "icon.ico" -n "NoobNote" leaf.py
echo Done
echo NoobScience