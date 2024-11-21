#!/bin/usr/env python3
import os
class MindMapLeaf:
    # step 1
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def __str__(self):
        return self.get_shape_representations().format(name = self.name)

    def get_mind_map(self, indent=0):
        result = ''
        if indent == 0:
            result += 'mindmap' + os.linesep + 'root'
        result += ' ' * indent + str(self)+ os.linesep
        return result

    def display(self, indent = 0):
        if indent == 0:
            print('mindmap' + os.linesep + 'root', end='')
        print(' ' *indent + str(self))

    def get_shape_representations(self):
        shapes = {"circle": "(({name}))",
                 "oval": "({name})",
                 "square": "[{name}]",
                 "cloud": "){name}(",
                 "hexagon": "{{{{{name}}}}}",
                 "bang": ")){name}(("}
        return shapes.get(self.shape, '{name}')

def main():
    nml = MindMapLeaf('ashly', 'circle')
    #print(nml)
    nml.display()
if __name__ == '__main__':
    main()