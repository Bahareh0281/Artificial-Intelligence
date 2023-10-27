import numpy as np
import pandas as pd


train = pd.read_csv('Airplane.csv')
# print (train.info())

# print(train.head(10))

# nptest = np.array(train["WillWait"])
# # nptest.sort()
# nptest

def map_column_to_index(data_frame, column_name):
    column_values = data_frame[column_name]
    unique_values = column_values.unique()
    value_to_index = {value: index for index, value in enumerate(unique_values)}
    return value_to_index

attributes = train.columns
for attribute in attributes:
    train[attribute] = train[attribute].replace(map_column_to_index(train, attribute))  

# # print(train[["Type", "WillWait"]].groupby(["Type"], as_index=False).mean())
# GroupedByType = train[["Type", "WillWait"]].groupby(["Type"], as_index=False).mean()
# print(GroupedByType)

# GroupedByPat = train[["Pat", "WillWait"]].groupby(["Pat"], as_index=False).mean()
# print(GroupedByPat)

# print (train)

class Node:
    def __init__(self, attribute=None, value=None, label=None):
        self.attribute = attribute  # Attribute at this node
        self.value = value  # Value of the attribute (for non-leaf nodes)
        self.label = label  # Class label (for leaf nodes)
        self.children = {}  # Dictionary to store child nodes

    def add_child(self, value, child_node):
        self.children[value] = child_node

def PLURALITY_VALUE(examples):
    return np.argmax(np.bincount(examples[:, -1]))


def find_attribute_index(attribute, attributes):
    index = attributes.index(attribute)
    return index


def select_best_attribute_entropy(attributes, examples):
    best_attribute = None
    best_gain = -1
    for attribute in attributes:
        entropy = entropy_help(examples[attribute])
        if best_attribute is None or entropy < best_gain:
            best_attribute = attribute
            best_gain = entropy
    return best_attribute


def entropy_help(examples):
    unique_values, counts = np.unique(examples, return_counts=True)
    probabilities = counts / len(examples)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy


def select_best_attribute_GiniIndex(attributes, examples):
    best_attribute = None
    best_gini_index = float('inf')

    for attribute in attributes:
        attribute_values = np.unique(examples[:, find_attribute_index(attribute, attributes)])
        attribute_gini_index = 0

        for value in attribute_values:
            value_examples = examples[examples[:, find_attribute_index(attribute, attributes)] == value]
            value_prob = len(value_examples) / len(examples)
            value_gini_index = GiniIndex_help(value_examples[:, -1])

            attribute_gini_index += value_prob * value_gini_index

        if attribute_gini_index < best_gini_index:
            best_gini_index = attribute_gini_index
            best_attribute = attribute

    return best_attribute

def GiniIndex_help(labels):
    labels = labels.astype(int)
    label_counts = np.bincount(labels)
    label_probs = label_counts / len(labels)
    gini_index = 1 - np.sum(label_probs ** 2)
    return gini_index


def LEARN_DECISION_TREE(examples, attributes, parent_examples):
    if len(examples) == 0:
        return Node(label=PLURALITY_VALUE(parent_examples))
    
    elif np.all(examples.iloc[:, -1] == examples.iloc[0, -1]):
        return Node(label=examples[0, -1])
    
    elif len(attributes) == 0:
        return Node(label=PLURALITY_VALUE(examples))
    
    else:
        # A = select_best_attribute_GiniIndex(attributes, examples)
        A = select_best_attribute_entropy(attributes, examples)
        A_index = find_attribute_index(A, attributes)
        tree = Node(attribute=A)
        
        for value in np.unique(examples[:, A_index]):
            exs = examples[examples[:, A_index] == value]
            subtree = LEARN_DECISION_TREE(exs, attributes[:A_index] + attributes[A_index+1:], examples)
            tree.add_child(value, subtree)
        
        return tree
    

def print_tree(node, indent=''):
    if node.label is not None:
        print(indent + "Label:", node.label)
    else:
        print(indent + "Attribute:", node.attribute)
        for value, child_node in node.children.items():
            print(indent + "Value:", value)
            print_tree(child_node, indent + "  ")


def predict(node, instance):
    # print("Node attribute is: ")
    # print(node.attribute)
    # print("Instance is: ")
    # print(instance)
    if node.label is not None:
        return node.label
    attribute_value = instance[attributes.index(node.attribute)]
    # print("Attribute value is: ")
    # print(attribute_value)
    if attribute_value in node.children:
        child_node = node.children[attribute_value]
        return predict(child_node, instance)
    else:
        # Handle missing or unseen attribute values
        return None

def test_decision_tree(tree, test_data):
    predictions = []
    for instance in test_data:
        prediction = predict(tree, instance)
        predictions.append(prediction)
    return predictions

def calculate_accuracy(predictions, actual_labels):
    correct_predictions = 0
    total_predictions = len(predictions)

    for i in range(total_predictions):
        if predictions[i] == actual_labels[i]:
            correct_predictions += 1

    accuracy = correct_predictions / total_predictions
    return accuracy


import random

def random_rows_after_2000(data_frame, num_rows):
    total_rows = data_frame.shape[0]
    eligible_indices = list(range(2001, total_rows))
    
    # if len(eligible_indices) < num_rows:
    #     raise ValueError("Not enough eligible rows available.")
    
    selected_indices = random.sample(eligible_indices, num_rows)
    selected_rows = data_frame.iloc[selected_indices]
    
    return selected_rows


# train_data = np.array(train)
train_data = random_rows_after_2000(train, 500)
target = train_data.iloc[:, -1]
# attributes = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est']
attributes = list(attributes)
DT = LEARN_DECISION_TREE(train_data, attributes, target)

# print("Decision Tree:")
# print_tree(DT)

NumberOfTestData = 200

test_data = np.array(train.head(NumberOfTestData))[:, :-1]
predictions = test_decision_tree(DT, test_data)
# print("Predictions:")
# print(predictions)

accuracy = calculate_accuracy(predictions, target[-NumberOfTestData:])
print("Accuracy:", accuracy * 100)