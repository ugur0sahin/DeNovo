from ete3 import Tree, faces, AttrFace, TreeStyle, NodeStyle
import Toolbar.Build_Tree_Tools.converter_distancelst_to_ete3format as transform_tree
#import Toolbar.Build_Tree_Tools.Distance_Tree.U_and_W_PGMA.WPGMA_Tree as WPGMATree
#import Toolbar.Build_Tree_Tools.UPGMA_Tree as UPGMATree
import random as rnd
'''
input =[ ('fb', 'f', 0.5, 'b'),
('da', 'd', 4.0, 'a'),
('gfb', 'g', 6.25, 'fb'),
('dagfb', 'da', 8.25, 'gfb')]

input=[('ba', 'b', 8.5, 'a'),
       ('eba', 'e', 11.0, 'ba'),
       ('dc', 'd', 14.0, 'c'),
       ('ebadc', 'eba', 17.5, 'dc')]

'''

input=[('fb', 'f', 0.5, 'b'),
('da', 'd', 4.0, 'a'),
('gfb', 'g', 6.25, 'fb'),
('dagfb', 'da', 8.25, 'gfb'),
('cdagfb', 'c', 14.5, 'dagfb'),
('ecdagfb', 'e', 17.0, 'cdagfb')]



def layout(node):
    # If node is a leaf, add the nodes name and a its scientific name
    if node.is_leaf():
        faces.add_face_to_node(AttrFace("name"), node, column=0)

def get_tree(input):
    tree_prepared = transform_tree.prepare_tree(input)
    #tree_prepared = "(e:12.000,(c:14.500,((d:4.000,a:4.000):4.250,(g:6.250,(f:0.500,b:0.500):5.750):2.000):6.250):2.500)"
    #tree_prepared="((Sus.Scrofa:11.000,(P.Paniscus:8.500,H.Spiens:8.500):2.500):6.500,(G.Gallus:14.000,R.Rattus:11.000):1.500)"
    t = Tree("(" + str(tree_prepared) + ");", format=1)

    # Node style handling is no longer limited to layout functions. You
    # can now create fixed node styles and use them many times, save them
    # or even add them to nodes before drawing (this allows to save and
    # reproduce an tree image design)

    # Set bold red branch to the root node
    style = NodeStyle()
    style["fgcolor"] = "#0f0f0f"
    style["size"] = 0
    style["fgcolor"] = "black"
    style["vt_line_color"] = "#ff0000"
    style["hz_line_color"] = "#ff0000"
    style["vt_line_width"] = 1.5
    style["hz_line_width"] = 1.5
    style["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
    style["hz_line_type"] = 0
    t.set_style(style)


    #Set dotted red lines to the first two branches
    style1 = NodeStyle()
    style1["size"] = 0
    style1["fgcolor"] = "black"
    style1["vt_line_width"] = 1.5
    style1["hz_line_width"] = 1.5
    style1["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
    style1["hz_line_type"] = 0
    style1["bgcolor"]="white"

    style3= NodeStyle()
    style3["fgcolor"]="black"
    style3["vt_line_width"] = 1.5
    style3["hz_line_width"] = 1.5
    style3["vt_line_type"] = 0  # 0 solid, 1 dashed, 2 dotted
    style3["hz_line_type"] = 0

    for i in t.iter_search_nodes():
        i.img_style = style1
        i.img_style = style1
    for n in t.iter_leaves():
        n.img_style = style3

    # Set dashed blue lines in all leaves
    style2 = NodeStyle()

    style2["shape"] = "circle"
    style2["fgcolor"] = "black"
    style2["vt_line_width"] = 1.5
    style2["hz_line_width"] = 1.5
    style2["vt_line_type"] = 0# 0 solid, 1 dashed, 2 dotted
    style2["hz_line_type"] = 0
    for l in t.iter_leaves():
        l.img_style = style2

    ts = TreeStyle()
    ts.layout_fn = layout
    ts.show_leaf_name = False
    ts.show_scale=False
    ts.show_branch_length =True
    ts.mode="r"

    return t, ts
'''
def plot_tree(input):
    a=rnd.randint(0,1000)
    t, ts = get_tree(input)
    t.show(tree_style=ts)
    t.render("node_style_" +str(a)+ "_.png", w=400, tree_style=ts)
'''
def get_tree_NJ(tree_formed):
    tree_prepared=tree_formed
    t = Tree("(" + str(tree_prepared) + ");", format=1)

    # Node style handling is no longer limited to layout functions. You
    # can now create fixed node styles and use them many times, save them
    # or even add them to nodes before drawing (this allows to save and
    # reproduce an tree image design)

    # Set bold red branch to the root node
    style = NodeStyle()
    style["fgcolor"] = "#0f0f0f"
    style["size"] = 0
    style["fgcolor"] = "black"
    style["vt_line_color"] = "#ff0000"
    style["hz_line_color"] = "#ff0000"
    style["vt_line_width"] = 1.5
    style["hz_line_width"] = 1.5
    style["vt_line_type"] = 0  # 0 solid, 1 dashed, 2 dotted
    style["hz_line_type"] = 0
    t.set_style(style)

    # Set dotted red lines to the first two branches
    style1 = NodeStyle()
    style1["size"] = 0
    style1["fgcolor"] = "black"
    style1["vt_line_width"] = 1.5
    style1["hz_line_width"] = 1.5
    style1["vt_line_type"] = 0  # 0 solid, 1 dashed, 2 dotted
    style1["hz_line_type"] = 0
    style1["bgcolor"] = "white"

    style3 = NodeStyle()
    style3["fgcolor"] = "black"
    style3["vt_line_width"] = 1.5
    style3["hz_line_width"] = 1.5
    style3["vt_line_type"] = 0  # 0 solid, 1 dashed, 2 dotted
    style3["hz_line_type"] = 0

    for i in t.iter_search_nodes():
        i.img_style = style1
        i.img_style = style1
    for n in t.iter_leaves():
        n.img_style = style3

    # Set dashed blue lines in all leaves
    style2 = NodeStyle()

    style2["shape"] = "circle"
    style2["fgcolor"] = "black"
    style2["vt_line_width"] = 1.5
    style2["hz_line_width"] = 1.5
    style2["vt_line_type"] = 0  # 0 solid, 1 dashed, 2 dotted
    style2["hz_line_type"] = 0
    for l in t.iter_leaves():
        l.img_style = style2

    ts = TreeStyle()
    ts.layout_fn = layout
    ts.show_leaf_name = False
    ts.show_scale = False
    ts.show_branch_length = True
    ts.mode = "r"

    return t, ts

def plot_tree(input):
    a = rnd.randint(0, 1000)
    t, ts = get_tree(input)
    t.show(tree_style=ts)
    t.render("node_style_" + str(a) + "_.png", w=400, tree_style=ts)

def plot_tree_NJ(input):
    a = rnd.randint(0, 1000)
    t, ts = get_tree_NJ(input)
    t.show(tree_style=ts)
    t.render("node_style_" + str(a) + "_.png", w=400, tree_style=ts)

#print(input)
#print(get_tree(input))
#print(plot_tree(input))
#print(plot_tree_NJ("(((((c:5.0625,d:8.9375):2.041666666666667,(a:9.9,b:7.1):3.708333333333333):2.0,f:9.125):1.375,e:9.625):3.1875,g:3.1875):1"))