import numpy as np
# necessary for wordcloud
from PIL import Image, ImageOps
# pillow module necessary for wordcloud
import matplotlib.pyplot as plt
# to show and save image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # the real wordcloud module
from scipy.ndimage import gaussian_gradient_magnitude  # edge detection

file = open("Pathfinder.txt", 'r')
text = file.read()

canvas_width = 1920
# width of the output image
canvas_height = 1080  # height of the output image
wordcloud = WordCloud(width=canvas_width, height=canvas_height).generate(text)
# generate wordcloud
wordcloud.to_file("simple_wordcloud.png")  # save the output wordcloud in png format
plt.imshow(wordcloud, interpolation='bilinear')
# show the image output
plt.axis("off")
plt.show()
