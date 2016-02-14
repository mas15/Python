"""
Created on 30 sty 2016

AVL tree - my second python program :)

I guess that it's not done quite properly because I've done it without knowing a python behaviour and it can be done much better

@author: Mateusz Stankiewicz
"""


class Sentinel(object):
    value = left = right = None
    height = -1


sentinel = Sentinel()  # singleton of sentinel node


class Node:
    def __init__(self, data, left=sentinel, right=sentinel, height=0):
        self.data = data
        self.left = left
        self.right = right
        self.height = height

    def addNode(self, data):
        if self.data == data:
            # return when node duplicated
            return
        isLeft = self.data > data
        child = self.left if isLeft else self.right
        if child is sentinel:
            setattr(self, 'left' if isLeft else 'right', Node(data))
        else:
            child.addNode(data)
            self.rebalance()
        self.setHeight()

    def rebalance(self):
        if self.balance() == 2:
            if self.right.balance() == -1:
                self.doubleRotateLeft()
            else:
                self.rotateLeft()
            self.right.setHeight()
            self.left.setHeight()
        elif self.balance() == -2:
            if self.left.balance() == 1:
                self.doubleRotateRight()
            else:
                self.rotateRight()
            self.right.setHeight()
            self.left.setHeight()

    def balance(self):
        return self.right.height - self.left.height

    def setHeight(self):
        self.height = max(self.left.height, self.right.height) + 1

    def printNodes(self):
        if self.left is not sentinel:
            self.left.printNodes()
        print(self)
        if self.right is not sentinel:
            self.right.printNodes()

    def printSpaces(self, number):
        for i in range(0, number):
            print(" ")

    def delete(self, key):
        if key == self.data:
            ''' when found and we know that has one or two children'''
            if self.left is sentinel:
                # if has got right child
                self.replaceWithChild(self.right)
            elif self.right is sentinel:
                # if has got left child
                self.replaceWithChild(self.left)
            else:
                if self.right.left is not sentinel:
                    self.data = self.right.pullMostLeftData()
                    print("data", self.data)
                else:
                    # put right child instead of self
                    self.data, self.right.data = self.right.data, self.data
                    self.right = self.right.right
        else:
            child = self.left if key < self.data else self.right
            if child is sentinel:
                print("Not found")
            else:
                if not child.hasChildren() and child.data == key:
                    # delete node if it is a leaf
                    setattr(self, 'left' if key < self.data else 'right', sentinel)
                else:
                    child.delete(key)
        self.rebalance()
        self.setHeight()

    def replaceWithChild(self, child):
        self.data, child.data = child.data, self.data
        self.left, child.left = child.left, self.left
        self.right, child.right = child.right, self.right

    def hasChildren(self):
        return self.left is not sentinel or self.right is not sentinel

    def pullMostLeftData(self):
        if self.left.left is not sentinel:
            return self.left.pullMostLeftData()
        else:
            data = self.left.data
            self.left = self.left.right
            return data

    def rotateRight(self):
        self.data, self.left.data = self.left.data, self.data
        temp = self.left
        self.left = self.left.left
        temp.left = self.right
        self.right = temp
        self.right.right, self.right.left = self.right.left, self.right.right

    def rotateLeft(self):
        self.data, self.right.data = self.right.data, self.data
        temp = self.right
        self.right = self.right.right
        temp.right = self.left
        self.left = temp
        self.left.right, self.left.left = self.left.left, self.left.right

    def doubleRotateRight(self):
        self.data, self.left.right.data = self.left.right.data, self.data
        self.right, self.left.right = self.left.right, self.right
        self.left.right, self.right.left = self.right.left, self.left.right
        self.right.left, self.right.right = self.right.right, self.right.left

    def doubleRotateLeft(self):
        self.data, self.right.left.data = self.right.left.data, self.data
        self.left, self.right.left = self.right.left, self.left
        self.right.left, self.left.right = self.left.right, self.right.left
        self.left.right, self.left.left = self.left.left, self.left.right

    def __str__(self):
        return str(self.data)


class binaryTree:
    def __init__(self):
        self.root = sentinel

    def add(self, data):
        if self.root is sentinel:
            self.root = Node(data)
        else:
            self.root.addNode(data)

    def printAll(self):
        if self.root is sentinel:
            print("Empty tree")
        else:
            self.root.printNodes()

    def delete(self, key):
        self.root.delete(key)

    def printBFS(self):
        if self.root is not sentinel:
            print("Tree:")
            level = [self.root]
            while level:
                newLevel = list()
                for n in level:
                    print(str(n) + " ", end='')
                    if n.left is not sentinel:
                        newLevel.append(n.left)
                    if n.right is not sentinel:
                        newLevel.append(n.right)
                print()
                level = newLevel


if __name__ == '__main__':
    b = binaryTree()
    b.add(1)
    b.add(22)
    b.add(4)
    b.add(26)
    b.add(13)
    b.add(3)
    b.add(14)
    b.add(6)
    b.add(13)
    b.add(5)
    b.add(23)
    b.delete(22)
    b.add(36)
    b.add(43)
    b.add(5)
    for i in range(1, 20):
        b.add(i)
    b.delete(26)
    b.delete(13)
    b.delete(8)
    b.printBFS()
