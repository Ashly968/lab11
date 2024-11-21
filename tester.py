from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite
from jinja2 import Environment, FileSystemLoader

def get_mind_map_html(root):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/mindmap.j2')
    output = template.render(mindmap=root.get_mind_map())
    return output

def main():
    #part 1 test
#    leaf = MindMapLeaf("Jean-Luc Picard", "circle")
 #   print(str(leaf))  # Should display "((Jean-Luc Picard))"
  #  leaf.display(2)   # Should display "  ((Jean-Luc Picard))" with two spaces
   # print("MindMapLeaf tests completed!")

    #part 2 test
    tools = MindMapComposite('Tools', 'cloud')
    tools.add(MindMapLeaf('Mermaid', 'Square'))
    tools.add(MindMapLeaf('Pen & Paper', 'Square'))
    mmc = MindMapComposite('MindMap', 'circle')
    mmc.add(tools)
    mmc.add(MindMapLeaf('Origins', 'cloud'))
    mmc.add(MindMapLeaf('Research', 'cloud'))
    mmc.display()

    print(get_mind_map_html(mmc))

    with open('templates/mindmap.html', 'w') as file:
        file.write(get_mind_map_html(mmc))

if __name__=='__main__':
    main()