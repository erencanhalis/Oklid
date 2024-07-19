import math

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafelerin Hesaplanması
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçların Yazdırılması
print("Noktalar arası mesafeler:", distances)
print("Minimum mesafe:", min_distance)
