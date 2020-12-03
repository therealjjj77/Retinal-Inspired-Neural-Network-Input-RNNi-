# RNNi
Retina Inspired Neural Network Data Structure

It's suggested that you first read the paper titled "Motivation for RNN.pdf". Abstract is below:

Abstract:
Data processing requirements for image processing with neural networks presents a bottleneck. Traditional neural network methods attempt to process whole images resulting in a growth of 2^(2n) of data per doubling(n) of information in one dimension. When examining how image processing is handled in nature, there are some distinct features which overcome this bottleneck. This paper presents a method inspired by nature which may result in a growth as low as 4n per doubling(n) of information in one dimension. Applying only the Retinal inspired Neural Network(RNN-i) method with MNIST Fashion images of 28x28 found a processing time reduction of 244% over conventional whole image processing, while maintaining 81.4% accuracy(vs. 88.3% for conventional whole image processing via neural networks). Due to the linear nature of data requirements growth with n using an RNN-i, this method could yield significantly lower data processing times for higher resolution image processing.  This paper also proposes a structure for a RNN-Brn neural network used in conjunction with the RNN-i. The system of both RNN-i and RNN-Brn can then be optimized for both efficiency and accuracy. 


Source Code is based on Neural Networks from Scratch in Python, Chapter 19: https://nnfs.io/. 
