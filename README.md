# RNNi
Retina Inspired Neural Network Data Structure

It's suggested that you first read the paper titled "Motivation for RNN.pdf". Abstract is below:

Abstract:
Data processing requirements for image processing with neural networks presents a bottleneck. Traditional neural network methods attempt to process whole images resulting in a growth of 2^(2n) of data per doubling(n) of information in one dimension. When examining how image processing is handled in nature, there are some distinct features which overcome this bottleneck. This paper presents a method inspired by nature which may result in a growth as low as 4n per doubling(n) of information in one dimension. Applying only the Retinal inspired Neural Network(RNN-i) method with MNIST Fashion images of 28x28 found a processing time reduction of 244% over conventional whole image processing, while maintaining 81.4% accuracy(vs. 88.3% for conventional whole image processing via neural networks). Due to the linear nature of data requirements growth with n using an RNN-i, this method could yield significantly lower data processing times for higher resolution image processing.  This paper also proposes a structure for a RNN-Brn neural network used in conjunction with the RNN-i. The system of both RNN-i and RNN-Brn can then be optimized for both efficiency and accuracy. 

File Summary:

nnfs-neural-network-test-RNNi.py - This is described in the paper.

nnfs-neural-network-test-default.py - This is described in the paper.

RNNi-module.py - This is exclusively the code which creates multiple "looks" per image. Parameters/ranges can be adjusted. These parameters will be randomized based on the ranges you specify: center of focus location, brightness, contrast, and rotation.  

RNNi+RNNBrn-v2.py - This is an updated working classification neural network training program based on the most recent RNNi-module. Instructions:
  1. You will need a folder in your python directory for storing images with subfolders as follows -> {names of subfolders:} test;train  -> {names of subfolders should be labeled 0 to n. for example, 0 1 2 3 for four unique classifiers}
  2. Go to line 1140 to change the name of the folder to match that of your main folder storing images from step 1.
  3. Go to line 1070 thru 1077. You may need to adjust the parameters in fs[] based on the instructions in the comments on lines 1070-1075. 
  4. Go to line 1156 to define the number of nodes per hidden layer. 
  5. Go to line 1165 to define the number of classifications. This should equal the number of folders in your "train" or "test" subfolders, which should be equal.
  6. You can also adjust epochs and steps per print on line 1180.

The code above was working using Python 3.6 and most updated packages specified in the top of the code files.

Source Code in the python files are based on Neural Networks from Scratch in Python, Chapter 19: https://nnfs.io/. 


