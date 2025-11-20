from mindmap_leaf import MindMapLeaf
from minbndmap_composite import MindMapComposite

if __name__ == "__main__":
    mindmap = MindMapComposite("mindmap","circle")
    tools = MindMapComposite("Tools", "bang")
    tools.add(MindMapLeaf("Pen and paper" ,"rectangle"))
    tools.add(MindMapLeaf("Mermaid", "rectangle"))
    mindmap.add(tools)
    origins = (MindMapComposite("Origins", "square"))
    origins.add(MindMapLeaf("Long histry", "rectangle"))
    popularisation = (MindMapComposite("Popularity", "rectangle"))
    popularisation.add(MindMapLeaf("British popular psychologyauthor Tony Buzan", "rectangle"))
    origins.add(popularisation)
    mindmap.add(origins)
    mindmap.display()
