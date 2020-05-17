# obrabMultimediaLab1
![""](https://i.ibb.co/MG0V4rs/Vj-XIMZqpj6-Q.jpg)
![""](https://i.ibb.co/3rNSCdt/De-Cpm-PGg-Se0.jpg)
![""](https://i.ibb.co/PrQp3db/Llnej-Lbsq-VA.jpg)
![""](https://i.ibb.co/cb6QwX0/3d-J4k6-RYDz-U.jpg)


В задаче использовался пример полносвязной нейронной сети из 6 слоев. 
1- Flatten
2- Dense (128 нейронов);
3- Dense (128 нейронов);
4- Dense (64 нейронов);
5- Dense (64 нейронов);
6- Dense (10 нейронов);
2, 3, 4, 5 слои используют активацию relu.
6 слой использует активацию softmax.
В обучении нейронной сети производится 10 эпох обучения.
В цикле обучения используются:
- оптимизатор adam
- функция потерь sparse_categorical_crossentropy
- метрика accuracy
###Точность на валидационной выборке: val_acc=0.46
