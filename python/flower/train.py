import pandas as pd
import cv2 as cv
from matplotlib import pyplot as plt


data = pd.read_csv("train.csv")

print(data.head())

category = data['category'][4]

print(data['category'][4])
print(category)
image = cv.imread('train/4.jpg')
plt.imshow(image)
plt.show()


# #Alpine sea holly
# Anthurium
# Artichoke
# Azalea
# Ball Moss
# Balloon Flower
# Barbeton Daisy
# Bearded Iris
# Bee Balm
# Bird of paradise
# Bishop of llandaff
# Blackberry Lily
# Black-eyed Susan
# Blanket flower
# Bolero deep blue
# Bougainvillea
# Bromelia
# Buttercup
# Californian Poppy
# Camellia
# Canna Lily
# Canterbury Bells
# Cape Flower
# Carnation
# Cautleya Spicata
# Clematis
# Colt's Foot
# Columbine
# Common Dandelion
# Corn poppy
# Cyclamen
# Daffodil
# Desert-rose
# English Marigold
# Fire Lily
# Foxglove
# Frangipani
# Fritillary
# Garden Phlox
# Gaura
# Gazania
# Geranium
# Giant white arum lily
# Globe Thistle
# Globe-flower
# Grape Hyacinth
# Great Masterwort
# Hard-leaved pocket orchid
# Hibiscus
# Hippeastrum
# Japanese Anemone
# King Protea
# Lenten Rose
# Lotus
# Love in the mist
# Magnolia
# Mallow
# Marigold
# Mexican Aster
# Mexican Petunia
# Monkshood
# Moon Orchid
# Morning Glory
# Orange Dahlia
# Osteospermum
# Oxeye Daisy
# Passion Flower
# Pelargonium
# Peruvian Lily
# Petunia
# Pincushion flower
# Pink Primrose
# Pink-yellow Dahlia
# Poinsettia
# Primula
# Prince of wales feathers
# Purple Coneflower
# Red Ginger
# Rose
# Ruby-lipped Cattleya
# Siam Tulip
# Silverbush
# Snapdragon
# Spear Thistle
# Spring Crocus
# Stemless Gentian
# Sunflower
# Sweet pea
# Sweet William
# Sword Lily
# Thorn Apple
# Tiger Lily
# Toad Lily
# Tree Mallow
# Tree Poppy
# Trumpet Creeper
# Wallflower
# Water Lily
# Watercress
# Wild Pansy
# Windflower
# Yellow Iris