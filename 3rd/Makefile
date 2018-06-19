.PHONY:	all kitti_native_evaluation cityscapesScripts

all:	kitti_native_evaluation cityscapesScripts

kitti_native_evaluation:
	cd kitti_native_evaluation && cmake -DCMAKE_BUILD_TYPE=release . && make -j8

cityscapesScripts:
	cd cityscapesScripts && python3 setup.py build
