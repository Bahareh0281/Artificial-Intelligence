import numpy as np
import pandas as pd


train = pd.read_csv('Restaurant.csv')
# print (train.info())

# print(train.head(10))

# nptest = np.array(train["WillWait"])
# # nptest.sort()
# nptest

YesNo_Mapping = {
    "Yes": 1,
    "No": 0,
}
train["Alt"] = train["Alt"].replace(YesNo_Mapping)
train["Bar"] = train["Bar"].replace(YesNo_Mapping)
train["Fri"] = train["Fri"].replace(YesNo_Mapping)
train["Hun"] = train["Hun"].replace(YesNo_Mapping)
train["Rain"] = train["Rain"].replace(YesNo_Mapping)
train["Res"] = train["Res"].replace(YesNo_Mapping)
train["WillWait"] = train["WillWait"].replace(YesNo_Mapping)

Pat_Mapping = {
    "None": -1,
    "Some": 0,
    "Full": 1,
}
train["Pat"] = train["Pat"].replace(Pat_Mapping)

Price_Mapping = {
    "$": 1,
    "$$": 2,
    "$$$": 3,
}
train["Price"] = train["Price"].replace(Price_Mapping)

Type_Mapping = {
    "French": 1,
    "Thai": 2,
    "Burger": 3,
    "Italian": 4,
}
train["Type"] = train["Type"].replace(Type_Mapping)

Est_Mapping = {
    "0-10": 1,
    " 10-30": 2,
    "30-60": 3,
    ">60": 4,
}
train["Est"] = train["Est"].replace(Est_Mapping)

# # print(train[["Type", "WillWait"]].groupby(["Type"], as_index=False).mean())
# GroupedByType = train[["Type", "WillWait"]].groupby(["Type"], as_index=False).mean()
# print(GroupedByType)

# GroupedByPat = train[["Pat", "WillWait"]].groupby(["Pat"], as_index=False).mean()
# print(GroupedByPat)

print (train)

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
    min_entropy = np.inf
    for attribute in attributes:
        entropy = entropy_help(examples[:, find_attribute_index(attribute, attributes)])
        if entropy < min_entropy:
            best_attribute = attribute
            min_entropy = entropy

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
    
    elif np.all(examples[:, -1] == examples[0, -1]):
        return Node(label=examples[0, -1])
    
    elif len(attributes) == 0:
        return Node(label=PLURALITY_VALUE(examples))
    
    else:
        A = select_best_attribute_GiniIndex(attributes, examples)
        # A = select_best_attribute_entropy(attributes, examples)
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
    print("Node attribute is: ")
    print(node.attribute)
    print("Instance is: ")
    print(instance)
    if node.label is not None:
        return node.label
    attribute_value = instance[attributes.index(node.attribute)]
    print("Attribute value is: ")
    print(attribute_value)
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


# train_data = np.array(train.head(10))
# attributes = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est']
# DT = LEARN_DECISION_TREE(train_data, attributes, np.array([]))

train_data = np.array(train)
target = train_data[:, -1]
attributes = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est']
DT = LEARN_DECISION_TREE(train_data, attributes, target)

print("Decision Tree:")
print_tree(DT)

test_data = np.array(train.tail(12))[:, :-1]
predictions = test_decision_tree(DT, test_data)
print("Predictions:")
print(predictions)

