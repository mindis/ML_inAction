#主要思想是建立分类器，对数据集分类的过程中国，由于存在多个超平面，
#所以需要选择一个最好的超平面当作数据集的分类器，线形模型可以设置为f(x) = WX+b
#而在选择最优超平面的过程中，需要先获取最小间隔的样本，即支持向量
#通过支持向量，来计算最小间隔，即计算模型参数W和b，使得间隔最小
#而在计算最小间隔的过程中，因为涉及向量内积会导致维度极高或无穷
#所以需要一种最优计算方法，SMO（序列最小优化），另外还包含软间隔（loss function）和正则化
#而在针对于非线性，则需要使用核函数（kenerl funtion）来将非线形问题映射到更高维的特征空间，从而使得其在特种空间中线形可分
#另外，实际情况下，支持向量回归在loss function的基础上，还提供来一个容忍偏差

#具体实验，下载libsvm进行实际操作