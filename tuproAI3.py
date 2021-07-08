# -*- coding: utf-8 -*-
"""TUPRO3 (10_IF4305_1301194xxx).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jI0C9NV61zZnMwNmJRhkMXrkD3yVwZCz

# Tugas Pemrograman 3
Kelompok : 10

Kelas : IF - 43 - 05
*   Arpriansah Yonathan (1301194112)
*   Igga Febrian Virgiani (1301194283)
*   Manuel Benedict (1301194182)

# *Library* yang dibutuhkan
"""

import pandas as pd
import math

"""# Membaca data"""

data = pd.read_excel('mobil.xls')
data.head()

data.info()

data.describe()

"""# Teknik Prapemrosesan Data"""

data.isna().sum()

df = data.drop(["Nama Mobil"], axis=1)

"""# Menghitung jarak"""

def euclidean_distance(point1, point2):  
    squared_distance = 0  
    for i in range(len(point1)):  
        squared_distance += math.pow(point1[i] - point2[i], 2)  
    return math.sqrt(squared_distance)

def manhattan_distance(point1, point2):
    sum_absolute_distance = 0 
    for i in range(len(point1)):
        sum_absolute_distance += abs(point1[i]-point2[i])
    return sum_absolute_distance

def minkowski_distance(point1, point2, r):
    distance_r = 0
    for i in range(len(point1)):
        distance_r = math.pow(abs(point1[i]-point2[i]), r)
    return math.pow(distance_r, 1/r)

def supremum_distance(point1, point2):
    return max(abs(point1[i]-point2[i]) for i in range(len(point1)))

"""# Klasifikasi kNN"""

training_data = [7, 7, 9, 6, 1.3]
def knn(k):
  manhattan_list = []
  euclidean_list = []
  minkowski_list = []
  supremum_list = []
  
  df_list = df.values

  for x in df_list:
    manhattan_list.append(manhattan_distance(x, training_data))
    euclidean_list.append(euclidean_distance(x, training_data))
    minkowski_list.append(minkowski_distance(x, training_data, 3))
    supremum_list.append(supremum_distance(x, training_data))
  data['manhattan'] = manhattan_list
  data['euclidean'] = euclidean_list
  data['minkowski'] = minkowski_list
  data['supremum']  = supremum_list

  manhattan_sorted = data.sort_values(by=['manhattan'])[:k]
  euclidean_sorted = data.sort_values(by=['euclidean'])[:k]
  minkowski_sorted = data.sort_values(by=['minkowski'])[:k]
  supremum_sorted = data.sort_values(by=['supremum'])[:k]

  return manhattan_sorted, euclidean_sorted, minkowski_sorted, supremum_sorted

man, euc, min, sup = knn(3)
print(man, euc, min, sup)

df_manhattan = pd.DataFrame(man)
df_manhattan = df_manhattan.drop(["euclidean", "minkowski", "supremum"], axis=1)
df_manhattan.to_excel('rekomendasi_manhattan.xls', index=False, header=["Nama Mobil", "Ukuran", "Kenyamanan", "Irit", "Kecepatan", "Harga(ratusan juta)", "Manhattan"])

df_euclidean = pd.DataFrame(euc)
df_euclidean = df_euclidean.drop(["manhattan", "minkowski", "supremum"], axis=1)
df_euclidean.to_excel('rekomendasi_euclidean.xls', index=False, header=["Nama Mobil", "Ukuran", "Kenyamanan", "Irit", "Kecepatan", "Harga(ratusan juta)", "Euclidean"])

df_minkowski = pd.DataFrame(min)
df_minkowski = df_minkowski.drop(["euclidean", "manhattan", "supremum"], axis=1)
df_minkowski.to_excel('rekomendasi_minkowski.xls', index=False, header=["Nama Mobil", "Ukuran", "Kenyamanan", "Irit", "Kecepatan", "Harga(ratusan juta)", "Minkowski"])

df_supremum = pd.DataFrame(sup)
df_supremum = df_supremum.drop(["euclidean", "manhattan", "minkowski"], axis=1)
df_supremum.to_excel('rekomendasi_supremum.xls', index=False, header=["Nama Mobil", "Ukuran", "Kenyamanan", "Irit", "Kecepatan", "Harga(ratusan juta)", "Supremum"])