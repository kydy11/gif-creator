import imageio

images =[]
filenames = ["tree-leaf.png", "tree-leaf2.png","tree-leaf3.png", "tree-leaf4.png","tree-leaf5.png", "tree-leaf6.png","tree-leaf7.png", "tree-leaf8.png","tree-leaf9.png", "tree-leaf10.png",]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('animate.gif', images, duration=0.5)