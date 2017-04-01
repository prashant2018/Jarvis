import sys
import nltk
import json
import ast
from nltk.tokenize import word_tokenize
import os

def getGraph(name):
	fileObj = open(name,"r")
	graph = fileObj.read()
	graph = "".join(graph.split())
	graph = graph.replace('\\\\','')
	fileObj.close()
	return ast.literal_eval(graph)


def getCommandId(words):
	words = processText(words)
	path = os.getcwd() + '/app/TextProcessing/graph.json'
	graph = getGraph(path)
	#print graph
	for root in graph:
		if root in words:
			for action in graph[root]:
				
				if action in words:
					return graph[root][action]
				
	return -1
		
def processText(words):
	words_ = word_tokenize(words)
	words_.append('.')
	return words_


def runCommand(activateMethodObj,words):
	id = getCommandId(words)
	if id == -1:
		soryyMessage()
	else:
		successMessage("Working on it")
		idJson = getGraph("id.json")
		methodName = idJson[id]
		getattr(activateMethodObj,methodName)()

def successMessage(message):
	print message

def soryyMessage():
	print "Sorry Unable to process"

	#NLP