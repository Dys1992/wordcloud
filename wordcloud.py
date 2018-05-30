from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

d = path.dirname(__file__)

text = open('word.txt').read()

alice_coloring = np.array(Image.open("timg.jpg"))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)

wc.generate(text)


image_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
