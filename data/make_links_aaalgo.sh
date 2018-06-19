#!/bin/bash

if [ ! -d /shared/s2 ]
then
    echo It seems you are not working in aaalgo
    echo You will have to create the links manually
    exit
fi

ln -si /shared/s2/data/benchmarks/bdd100k bdd100k
ln -si /shared/s2/data/benchmarks/cityscape cityscape
ln -si /shared/s2/data/benchmarks/coco coco
ln -si /shared/s2/data/benchmarks/kitti kitti
ln -si /shared/s2/data/benchmarks/kaggle_diabetic kaggle_diabetic
ln -si /shared/s2/data/physionet/2018 physionet18

