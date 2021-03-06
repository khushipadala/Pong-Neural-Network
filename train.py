import tensorflow as tf 
import cv2
import pong
import numpy as np 
import random 
from collection import deque


#defining hyperparaneters
ACTIONS = 3
#learning raye 
GAMMA = 0.99
#update our gradient or training time
INTIAL_EPISON = 1.0
FINAL EPSILON = 0.05
#how many frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000
#BATCH SIZE
BATCH = 100



#create TF graph
def createGraph():

	#first convolutional layer, bias vector
	W_conv1 = tf.Variable(tf.zeros([8,8 ,4, 32]))
	b_conv1 = tf.Varibale(tf.zeros[32])

	#second
	W_conv2 = tf.Varibale(tf.zeros[4,4,32,64])
	b_conv2= tf.Variable(tf.zeros[64])

	#third
	W_conv3 = tf.Varibale(tf.zeros[3,3,64,64])
	b_conv3 = tf.Variable(tf.zeros[64])

	#fourth
	W_fc4 = tf.Variable(tf.zeros[784, ACTIONS])
	b_fc4 = tf.Variable(tf.zeros[784])))

	#fifth/last layer 
	W_fc5 = tf.Variable(tf.zeros[784, ACTIONS]))
	b_fc5 = tf.Variable(tf.zeros[[ACTIONS]])

	#input for piezel data
	s = tf.placeholder("float". [None, 84, 84, 84])

	#compute RELU activation function 
	#on 2d convolution
	#given 4D inputs and filter tensors

	conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, stride [1,4,4,1] padding = "VALID") + b_conv1)
	conv2 = tf.nn.relu(tf.nn.conv2d(s, W_conv2, stride [1,4,4,1] padding = "VALID") + b_conv2)
	conv3 = tf.nn.relu(tf.nn.conv2d(s, W_conv3, stride [1,4,4,1] padding = "VALID") + b_conv1)

	conv3_flat = tf.reshape(conv3, [-1, 3136])
	fc4 = tf.nn.relu9tf.matmul(conv3_flat, W_fc4 + b_fc4)
	fc5 = tf.matmul(fc5, W_fc5) + bb_fc5

	return s, fc5 

def main():

	#create session
	sess = tf.InteractiveSession()
		#input player and our out layer
		inp, out = CreateGraph()
		trainGraph(inp, out, sess)

if  __name__ =  "__main__"
	main()
