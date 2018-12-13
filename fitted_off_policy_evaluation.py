"""
Created on December 12, 2018

@author: clvoloshin, 
"""

from model import Model
import numpy as np

class FittedOffPolicyQEvaluation(object):
	def __init__(self, initial_states, num_inputs, dim_of_actions, max_epochs, gamma):
		'''
		An implementation of fitted Q iteration

		num_inputs: number of inputs
		dim_of_actions: dimension of action space
		max_epochs: positive int, specifies how many iterations to run the algorithm
		gamma: discount factor
		'''
		self.num_inputs = num_inputs
		self.dim_of_actions = dim_of_actions
		self.max_epochs = max_epochs
		self.gamma = gamma
		self.initial_states = initial_states

	def init_Q(self):
		return Model(num_inputs, 1, dim_of_actions)

	def fit(self, D_k):
		# D_k is the dataset of the kth iteration of Fitted Q
		D_k = np.array(D_k)
		try:
			self.Q_k.fit(D_k[:,:-1], D_k[:,-1])
		except NameError:
			print 'Q has not been initialized. Please call run before calling fit.'
			sys.exit()

	def run(dataset, policy):
		# dataset is the original dataset generated by pi_{old} to which we will find
		# an approximately optimal Q

		self.Q_k = self.init_Q(num_inputs, num_outputs, dim_of_actions)
		for k in range(self.max_epochs):
			D_k = [[np.hstack([x,a]), r + self.gamma*self.Q_k(x_prime, policy(x_prime))[0]] for (x,a,x_prime,r) in dataset]
			self.fit(D_k)

		return np.mean([self.Q_k(state, policy(state)) for state in initial_states])


