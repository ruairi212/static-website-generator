class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        list = []
        for key, value in self.props.items():
            list.append(f'{key}="{value}"')
        
        str =  " ".join(list)
        return str
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
class LeafNode(HTMLNode):
    def __init__(self, value,tag=None,  props=None):
        super().__init__(tag, value ,props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag given")
        if self.children == None:
            raise ValueError("Children is None")
        list = []
        for child in self.children:
            list.append(child.to_html())
        list = "".join(list)
        str = f"<{self.tag}{self.props_to_html()}>{list}</{self.tag}>"
        return str
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
