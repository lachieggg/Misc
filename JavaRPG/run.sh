#!/bin/bash

javac -classpath ".:lib/slick.jar:lib/jinput.jar" src/*.java -d bin/

java -classpath ".:lib/slick.jar:lib/lwjgl.jar:lib/jinput.jar:bin" -Djava.library.path="./lib/natives" RPG

