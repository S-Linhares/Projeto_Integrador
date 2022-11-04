import numpy as np


print(25*'-', 'CIDADES', 25*'-')
print(f'1 - Valkaria{"33 - Montanhas Uivantes(leste)":>42}\n2 - Palthar{"34 - Montanhas Uivantes(oeste)":>43}'
      f'\n3 - Rhond{"35 - Montanhas Uivantes(sul)":>43}\n4 - Nova Malpetrim{"36 - Montanhas Uinvantes(norte)":>37}'
      f'\n5 - Barud{"37 - Montanhas Uivantes(centro)":>46}\n6 - Yuvalin{"38 - Grande Savana(oeste)":>38}\n7 - Zakharin'
      f'{"39 - Grande Savana(leste)":>37}\n8 - Villent{"40 - Grande Savana(centro)":>39}\n9 - Hippiontar'
      f'{"41 - Montanhas Sanguinarias(sul)":>42}\n10 - Altrim{"42 - Montanhas Sanguinarias(centro)":>48}'
      f'\n11 - Nimbarann{"43 - Montanhas Sanguinarias(norte)":>44}\n12 - Thartann'
      f'{"44 - Deserto da Perdição(leste)":>42}\n13 - Kannilar{"45 - Deserto da Perdição(centro)":>43}\n14 - Coridrian'
      f'{"46 - Deserto da Perdição(oeste)":>41}\n15 - Horeen{"47 - Ermos Púrpuras":>32}\n16 - Smokestone'
      f'{"48 - Floresta Tollon":>29}\n17 - Giluk{"49 - Floresta das Escamas Verdes":>46}\n18 - Fross'
      f'{"50 - A Cidade Normal dos Humanos":>46}\n19 - Yukadar{"51 - Khershandallas":>31}\n20 - Yuton'
      f'{"52 - Cidade no Deserto":>36}\n21 - Roschfallen{"53 - Ruinas de Tyrondir":>31}\n22 - Norm'
      f'{"54 - Imperio de Tauron(leste)":>44}\n23 - Milothiann{"55 - Imperio de Tauron(oeste)":>38}\n24 - Norba'
      f'{"56 - Imperio de Tauron(centro)":>44}\n25 - Coravandor{"57 - Imperio de Tauron(norte)":>38}\n26 - Adhurian'
      f'{"58 - Tiberus":>23}\n27 - Lannestul\n28 - Sternatchen\n29 - Khalifor\n30 - Lysianassa\n31 - Monte Palidor'
      f'\n32 - Ghallistryx')
print(59*'-')

cidade_destino = int(input('Informe qual cidade deseja que seja o destino: '))
cidade_origem = int(input('Informe qual cidade deseja que seja a origem: '))


class Vertice:

    def __init__(self, nome, distancia_objetivo):
        self.nome = nome
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.nome, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

        # Novo atributo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


def switch_dist_zero(selecao):
    if selecao == 1:
        lista_zero = (750, 1800, 1250, 1500, 1300, 2900, 2250, 2750, 3690, 4190, 5000, 3750, 3250, 3750, 1995, 3250,
                      2540, 2985, 2200, 1700, 1650, 800, 2600, 1950, 1650, 1525, 825, 855, 675, 550, 0, 510, 480, 1205,
                      950, 2135, 1625, 2525, 2045, 1640, 1090, 1490, 1490, 1765, 2200, 2120, 2690, 3120, 3450, 4190,
                      3790, 3300, 4750, 340, 700, 1050, 1325, 2750)
    if selecao == 2:
        lista_zero = (1327, 2274, 2167, 1464, 1833, 1782, 755, 1009, 2590, 2792, 3092, 1916, 1605, 2332, 1246, 3421,
                      2455, 2438, 2653, 0, 300, 999, 3144, 2906, 2628, 2535, 2276, 1180, 1073, 1183, 1700, 1794, 1241,
                      2370, 2432, 2864, 2180, 905, 735, 785, 1353, 1543, 1238, 1577, 1477, 997, 1422, 1650, 2687, 2586,
                      2194, 1979, 3791, 1962, 2345, 2576, 2792, 3692)
    if selecao == 3:
        lista_zero = (372, 1597, 1289, 927, 1107, 2007, 1463, 2010, 3223, 3626, 4034, 2906, 2411, 2775, 1273, 2961,
                      2094, 2291, 1983, 999, 1015, 0, 2400, 2014, 1733, 1609, 1281, 326, 448, 205, 800, 1083, 468, 1400,
                      1429, 2069, 1418, 1826, 1488, 1229, 1142, 1360, 1329, 1728, 1954, 1661, 2217, 2546, 3242, 3541,
                      3136, 2451, 3942, 1046, 1450, 1790, 2052, 2835)
    if selecao == 4:
        lista_zero = (1636, 900, 730, 1554, 1119, 2724, 2984, 3876, 5203, 5634, 5995, 3886, 2984, 2719, 2240, 1857,
                      1707, 2261, 850, 2906, 3006, 2014, 740, 0, 300, 435, 1169, 1763, 2309, 1963, 1950, 2373, 2171,
                      730, 1134, 430, 814, 3780, 3490, 3234, 2933, 3100, 3225, 3588, 3911, 3659, 4214, 4531, 5199, 5488,
                      5084, 3352, 3938, 2007, 1993, 2439, 2747, 850)
    if selecao == 5:
        lista_zero = (1230, 846, 350, 1288, 862, 2573, 2693, 3534, 4779, 5239, 5614, 3525, 2698, 2571, 2011, 2091, 870,
                      2235, 980, 2535, 2612, 1609, 1071, 435, 215, 0, 769, 1366, 1883, 1538, 1525, 1949, 1745, 335, 764,
                      710, 647, 3398, 3100, 2817, 2499, 2667, 2802, 3159, 3497, 3260, 3810, 4138, 4769, 5110, 4709,
                      3191, 3979, 1591, 1603, 2071, 2384, 1271)
    if selecao == 6:
        lista_zero = (140, 1332, 1022, 715, 844, 1916, 1537, 2192, 3485, 3882, 4251, 3045, 2465, 2717, 1166, 2705, 1860,
                      2096, 1707, 1180, 1246, 326, 2132, 1763, 1475, 1366, 1131, 0, 684, 350, 855, 1215, 653, 1180,
                      1287, 1805, 1151, 2038, 1730, 1494, 1388, 1602, 1597, 1992, 2217, 1916, 2464, 2779, 3506, 3759,
                      3358, 2416, 3839, 1084, 1453, 1845, 2119, 2577)
    if selecao == 7:
        lista_zero = (375, 1647, 1256, 1066, 1167, 2210, 1677, 2166, 3249, 3719, 4143, 3091, 2623, 3005, 1477, 3049,
                      2212, 2447, 2028, 1183, 1139, 205, 2410, 1963, 1689, 1538, 1117, 350, 356, 0, 550, 887, 300, 1306,
                      1271, 2069, 1444, 1963, 1597, 1282, 1059, 1263, 1292, 1676, 1965, 1730, 2286, 2652, 3249, 3655,
                      3254, 2681, 4165, 842, 1227, 1573, 1836, 2788)
    if selecao == 8:
        lista_zero = (680, 1934, 1509, 1363, 1455, 2462, 1842, 2181, 3059, 3589, 4072, 3149, 2784, 3228, 1741, 3339,
                      2515, 2741, 2310, 1241, 1125, 468, 2674, 2171, 1914, 1745, 1204, 653, 200, 300, 480, 620, 0, 1480,
                      1354, 2329, 1732, 1940, 1515, 1142, 778, 974, 1058, 1424, 1763, 1609, 2184, 2578, 3022, 3581,
                      3186, 2909, 4408, 668, 1093, 1371, 1622, 3013)
    if selecao == 9:
        lista_zero = (1380, 2450, 2269, 1647, 1986, 2089, 1054, 1056, 2355, 2647, 3007, 2037, 1871, 2629, 1518, 3649,
                      2704, 2706, 2833, 300, 0, 1015, 3312, 3006, 2723, 2612, 2259, 1246, 995, 1139, 1650, 1617, 1125,
                      2410, 2402, 3007, 2326, 821, 503, 495, 1078, 1261, 920, 1271, 1194, 742, 1225, 1537, 2423, 2519,
                      2117, 2290, 4093, 1783, 2209, 2403, 2579, 3814)
    if selecao == 10:
        lista_zero = (2040, 862, 1176, 1683, 1322, 1492, 3053, 4072, 5614, 5932, 6192, 4641, 3719, 3248, 2215, 1160,
                      1306, 1823, 525, 3144, 3312, 2400, 0, 740, 865, 1071, 1832, 2132, 2771, 2410, 2600, 2980, 2674,
                      1371, 1832, 360, 986, 4019, 3812, 3608, 3450, 3641, 3705, 4086, 4356, 4024, 4543, 4791, 5626,
                      5690, 5307, 3120, 3408, 2629, 2683, 3146, 3461, 739)
    if selecao == 11:
        lista_zero = (1364, 734, 460, 1309, 867, 2522, 2736, 3619, 4936, 5365, 5714, 4349, 3553, 3368, 2005, 1886, 1597,
                      2122, 800, 2628, 2723, 1733, 865, 300, 0, 215, 972, 1475, 2045, 1689, 1650, 2143, 1914, 517, 968,
                      550, 600, 3514, 3213, 2955, 2676, 2855, 2968, 3335, 3664, 3395, 3938, 4266, 4929, 5217, 4814,
                      3164, 3908, 1786, 1819, 2285, 2594, 1093)
    if selecao == 12:
        lista_zero = (985, 1428, 810, 1458, 1171, 2835, 2657, 3272, 4234, 4797, 5253, 4162, 3566, 2842, 2152, 2790,
                      2265, 2697, 1668, 2276, 2259, 1281, 1832, 1169, 972, 769, 0, 1131, 1377, 1117, 825, 1229, 1204,
                      460, 190, 1481, 1166, 3074, 2699, 2342, 1884, 2016, 2218, 2536, 2951, 2814, 3384, 3759, 4181,
                      4773, 4370, 3414, 4543, 861, 845, 1312, 1641, 1953)
    if selecao == 13:
        lista_zero = (739, 2005, 1611, 1352, 1514, 2386, 1685, 1986, 2909, 3408, 3880, 2954, 2612, 3123, 1657, 3374,
                      2522, 2706, 2377, 1073, 995, 448, 2771, 2309, 2045, 1883, 1377, 684, 0, 356, 675, 729, 200, 1642,
                      1525, 2425, 1800, 1745, 1323, 963, 700, 925, 926, 1321, 1622, 1434, 2003, 2390, 2895, 3415, 3011,
                      2807, 4384, 837, 1273, 1510, 1751, 3141)
    if selecao == 14:
        lista_zero = (1173, 2336, 1811, 1903, 1899, 3074, 2441, 2638, 3106, 3773, 4356, 3649, 3364, 3075, 2338, 3758,
                      3016, 3308, 2677, 1794, 1617, 1083, 2980, 2373, 2143, 1949, 1229, 1215, 729, 887, 510, 0, 620,
                      1641, 1318, 2608, 2100, 2363, 1893, 1459, 767, 835, 1125, 1372, 1863, 1897, 2439, 2878, 3010,
                      3903, 3521, 3514, 5039, 371, 679, 789, 1010, 3187)
    if selecao == 15:
        lista_zero = (1137, 1487, 878, 1587, 1283, 2971, 2811, 3431, 4358, 4931, 5404, 4316, 3718, 3829, 2303, 2827,
                      2352, 2804, 1715, 2432, 2402, 1429, 1832, 1134, 968, 764, 190, 1287, 1525, 1271, 950, 1318, 1354,
                      472, 0, 1481, 1236, 3226, 2841, 2487, 2005, 2117, 2342, 2653, 3078, 2947, 3523, 3902, 4292, 4915,
                      4514, 3547, 4597, 931, 862, 1308, 1627, 1895)
    if selecao == 16:
        lista_zero = (1702, 641, 820, 1420, 1022, 2411, 2826, 3800, 5288, 5639, 5929, 4438, 3551, 3209, 2010, 1394,
                      1301, 1839, 437, 2864, 3007, 2069, 360, 430, 550, 710, 1481, 1805, 2425, 2069, 2135, 2608, 2329,
                      1007, 1481, 0, 680, 3742, 3503, 3296, 3104, 3286, 3358, 3744, 4011, 3709, 4233, 4511, 5297, 5434,
                      5037, 3040, 3548, 2263, 2314, 2791, 3098, 837)
    if selecao == 17:
        lista_zero = (1055, 290, 390, 758, 300, 1928, 2203, 3128, 4620, 4960, 5257, 3800, 2971, 2774, 1423, 1671, 1115,
                      1589, 590, 2180, 2326, 1418, 986, 814, 600, 647, 1166, 1151, 1800, 1444, 1625, 2100, 1732, 781,
                      1236, 680, 0, 3052, 2838, 2626, 2500, 2693, 2734, 3129, 3360, 3034, 3555, 3843, 4659, 4776, 4372,
                      2575, 3426, 1792, 1961, 2433, 2756, 1515)
    if selecao == 18:
        lista_zero = (2182, 3141, 3031, 2326, 2718, 2348, 1213, 340, 1899, 1946, 2226, 1368, 1593, 2644, 1979, 4202,
                      3228, 3114, 3515, 905, 821, 1826, 4019, 3780, 3514, 3398, 3074, 2038, 1745, 1963, 2525, 2363,
                      1940, 3217, 3236, 3742, 3052, 0, 500, 920, 1708, 1826, 1408, 1564, 1162, 631, 675, 779, 2060,
                      1724, 1313, 2318, 4330, 2577, 2990, 3140, 3293, 4568)
    if selecao == 19:
        lista_zero = (1852, 2952, 2749, 2152, 2482, 2445, 1322, 816, 1872, 2147, 2552, 1848, 1939, 2885, 1943, 4118,
                      3168, 3120, 3325, 735, 503, 1488, 3812, 3490, 3213, 3100, 2699, 1730, 1323, 1597, 2045, 1893,
                      1515, 2876, 2841, 3503, 2838, 500, 0, 435, 1222, 1333, 933, 1115, 826, 300, 720, 1050, 1957, 2096,
                      1668, 2530, 4351, 2138, 2524, 2659, 2812, 4305)
    if selecao == 20:
        lista_zero = (1597, 2780, 2505, 2007, 2295, 2553, 1505, 1240, 2001, 2453, 2921, 2266, 2259, 3089, 1961, 4038,
                      3104, 3120, 3164, 785, 495, 1229, 3608, 3234, 2955, 2817, 2342, 1494, 963, 1282, 1640, 1459, 1142,
                      2553, 2487, 3296, 2626, 920, 435, 0, 779, 909, 550, 805, 770, 468, 1023, 1428, 2029, 2463, 2062,
                      2759, 4578, 1716, 2107, 2215, 2344, 4058)
    if selecao == 21:
        lista_zero = (1432, 2696, 2276, 2051, 2198, 2958, 2088, 2011, 2375, 3023, 3612, 3034, 2943, 3629, 2060, 4077,
                      3213, 3394, 3070, 1353, 1078, 1142, 3450, 2933, 2676, 2499, 1884, 1388, 700, 1059, 1090, 767, 778,
                      2217, 2005, 3104, 2500, 1708, 1222, 779, 0, 235, 400, 664, 1104, 1173, 1696, 2138, 2298, 3153,
                      2772, 3284, 5009, 1100, 1433, 1460, 1573, 3779)
    if selecao == 22:
        lista_zero = (1641, 2903, 2406, 2280, 2412, 2138, 2284, 3179, 2280, 2993, 3638, 3176, 3106, 3827, 2496, 4289,
                      3426, 3605, 3279, 1543, 1261, 1360, 3641, 3100, 2855, 2667, 2016, 1602, 925, 1263, 1490, 835, 974,
                      2374, 2117, 3286, 2693, 1826, 1333, 909, 235, 0, 409, 534, 1066, 1240, 1723, 2191, 2196, 3192,
                      2818, 3501, 5231, 1189, 1489, 1437, 1513, 3934)
    if selecao == 23:
        lista_zero = (2050, 3316, 2910, 2627, 2819, 3334, 2310, 1909, 1736, 2488, 3143, 2917, 3050, 3905, 2706, 4674,
                      3753, 3872, 3689, 1577, 1271, 1728, 4086, 3588, 3335, 3159, 2536, 1992, 1321, 1676, 1765, 1372,
                      1424, 2868, 2653, 3744, 3129, 1564, 1115, 805, 664, 534, 385, 0, 600, 933, 1319, 1777, 1655, 2724,
                      2384, 3560, 5330, 1735, 2017, 1931, 1977, 4429)
    if selecao == 24:
        lista_zero = (2022, 3174, 2932, 2382, 2686, 2727, 1610, 979, 1626, 1990, 2479, 1993, 2180, 3155, 2202, 4373,
                      3421, 3396, 3548, 997, 742, 1661, 4024, 3659, 3395, 3260, 2814, 1916, 1434, 1730, 2120, 1897,
                      1609, 3029, 2947, 3709, 3034, 631, 300, 468, 1173, 1240, 815, 933, 590, 0, 580, 980, 1701, 2014,
                      1618, 2817, 4694, 2154, 2547, 2620, 2730, 4478)
    if selecao == 25:
        lista_zero = (2911, 3928, 3784, 3114, 3481, 862, 1955, 3079, 1284, 1100, 1496, 1408, 2107, 3237, 2745, 4972,
                      4011, 3872, 4283, 1650, 1537, 2546, 4791, 4531, 4266, 4138, 3759, 2779, 2390, 2652, 3120, 2878,
                      2578, 3928, 3902, 4511, 3843, 779, 1055, 1428, 2138, 2191, 1782, 1777, 1206, 980, 475, 0, 1524,
                      1019, 638, 2952, 4891, 3154, 3533, 3600, 3691, 5329)
    if selecao == 26:
        lista_zero = (3592, 4794, 4504, 4044, 4301, 4370, 3239, 2279, 330, 1292, 2125, 2918, 3586, 4684, 3920, 6064,
                      5114, 5092, 5197, 2687, 2423, 3242, 5626, 5199, 4929, 4769, 4181, 3506, 2895, 3249, 3450, 3010,
                      3022, 4493, 4292, 5297, 4659, 2060, 1957, 2029, 2298, 2196, 1951, 1655, 1290, 1701, 1365, 1524, 0,
                      1914, 1784, 4372, 6310, 3385, 3640, 3516, 3463, 6017)
    if selecao == 27:
        lista_zero = (3862, 3184, 3753, 3161, 3379, 2001, 3023, 3938, 6028, 5777, 5551, 3673, 2677, 1300, 2700, 2473,
                      2343, 1845, 3197, 3791, 4093, 3942, 3408, 3938, 3908, 3979, 4543, 3839, 4384, 4165, 4750, 5039,
                      4408, 4234, 4597, 3548, 3426, 4330, 4351, 4578, 5009, 5231, 4953, 5330, 5190, 4694, 4820, 4891,
                      6310, 5188, 4899, 1823, 0, 4879, 5206, 5648, 5950, 4218)
    if selecao == 28:
        lista_zero = (1753, 2693, 2071, 2452, 2320, 3744, 3211, 3422, 3661, 4425, 5059, 4432, 4123, 4556, 3015, 4079,
                      3481, 3835, 2979, 2576, 2403, 1790, 3146, 2439, 2285, 3979, 1312, 1845, 1510, 1573, 1050, 789,
                      1371, 1761, 1308, 2791, 2433, 3140, 2659, 2215, 1460, 1437, 1830, 1931, 2493, 2620, 3147, 3600,
                      3516, 4619, 4250, 4238, 5648, 754, 500, 0, 800, 3184)
    if selecao == 29:
        lista_zero = (2049, 2999, 2387, 2754, 2646, 4024, 3435, 3582, 3637, 4453, 5119, 4602, 4357, 4825, 3288, 4406,
                      3784, 4130, 3277, 2792, 2579, 2052, 3461, 2747, 2594, 2384, 1641, 2119, 1751, 1836, 1325, 1010,
                      1622, 2056, 1627, 3098, 2756, 3293, 2812, 2344, 1573, 1513, 1918, 1977, 2554, 2730, 3242, 3691,
                      3463, 4692, 4316, 4503, 5950, 1033, 780, 800, 0, 3452)
    if selecao == 30:
        lista_zero = (2461, 1490, 1550, 2274, 1865, 3223, 3700, 4655, 6049, 6445, 6774, 5279, 4393, 3982, 2888, 1725,
                      2018, 2567, 1229, 3692, 3814, 2835, 739, 850, 1093, 1271, 1953, 2577, 3141, 2788, 2750, 3187,
                      3013, 1551, 1895, 837, 1515, 4568, 4305, 4058, 3779, 3934, 4062, 4429, 4776, 4478, 5020, 5329,
                      6017, 6274, 5870, 5014, 4218, 2817, 2774, 3184, 3452, 0)
    if selecao == 31:
        lista_zero = (980, 2032, 1480, 1718, 1622, 2980, 2482, 2827, 3460, 4094, 4635, 3807, 3417, 3784, 2231, 3461,
                      2761, 3099, 2370, 1962, 1783, 1046, 2629, 2007, 1789, 1591, 861, 1084, 937, 842, 349, 371, 668,
                      1267, 931, 2263, 1792, 2577, 2138, 1716, 1100, 1189, 1450, 1735, 4776, 2154, 2720, 3154, 3385,
                      4181, 3780, 3487, 4879, 0, 325, 754, 1033, 2817)
    if selecao == 32:
        lista_zero = (3900, 4830, 4753, 4018, 4409, 3710, 2704, 1633, 1616, 738, 450, 1495, 2530, 3711, 3562, 5764,
                      4800, 4566, 5194, 2586, 2519, 3541, 5690, 5488, 5217, 5110, 4773, 3759, 3415, 3644, 4190, 3903,
                      3581, 4926, 4915, 5434, 4776, 1724, 2096, 2463, 3153, 3192, 2811, 2724, 4776, 2014, 1488, 1019,
                      1914, 0, 400, 3446, 5188, 4181, 4584, 4619, 4692, 6274)
    if selecao == 33:
        lista_zero = (0, 1251, 710, 717, 730, 1995, 1670, 2326, 3599, 4003, 4393, 3177, 2605, 2824, 1273, 2642, 1851,
                      2121, 1647, 1327, 1380, 372, 2040, 1636, 1364, 1230, 985, 140, 739, 375, 750, 1173, 680, 1027,
                      1137, 1702, 1055, 2182, 1852, 1597, 1432, 1641, 1653, 2050, 2314, 2022, 2572, 2911, 3592, 3900,
                      3476, 2530, 3862, 980, 1350, 1753, 2049, 2461)
    if selecao == 34:
        lista_zero = (1251, 0, 600, 801, 500, 1807, 2201, 3203, 4768, 5071, 5329, 3799, 2917, 2631, 1387, 1427, 850,
                      1370, 430, 2274, 2450, 1597, 862, 900, 734, 846, 1428, 1332, 2005, 1647, 1800, 2336, 1934, 1028,
                      1487, 641, 290, 3141, 2952, 2780, 2696, 2903, 2926, 3316, 3530, 3174, 3659, 3928, 4794, 4830,
                      4432, 2427, 3184, 2032, 2221, 2693, 2999, 1490)
    if selecao == 35:
        lista_zero = (710, 600, 0, 894, 485, 2200, 2304, 3152, 4495, 4903, 5244, 3893, 3144, 3053, 1629, 2005, 1471,
                      1941, 895, 2167, 2269, 1289, 1176, 730, 460, 350, 810, 1022, 1611, 1256, 1250, 1811, 1509, 441,
                      878, 820, 390, 3031, 2749, 2463, 2276, 2406, 2546, 2910, 3218, 2931, 3460, 3784, 4504, 4753, 4343,
                      2808, 3753, 1480, 1610, 2071, 2387, 1550)    

    return lista_zero


class Grafo:

    lista = switch_dist_zero(cidade_destino)

    Montanhas_uivantes_leste = Vertice('Montanhas Uivantes(leste)', lista[0])
    Montanhas_uivantes_oeste = Vertice('Montanhas Uivantes(oeste)', lista[1])
    Montanhas_uivantes_sul = Vertice('Montanhas Uivantes(sul)', lista[2])
    Montanhas_uivantes_norte = Vertice('Montanhas Uivantes(norte)', lista[3])
    Montanhas_uivantes_centro = Vertice('Montanhas Uivantes(centro)', lista[4])
    Savana_oeste = Vertice('Grande Savana(oeste)', lista[5])
    Savana_centro = Vertice('Grande Savana(centro)', lista[6])
    Savana_leste = Vertice('Grande Savana(leste)', lista[7])
    Sanguinarias_sul = Vertice('Montanhas Sanguinarias(sul)', lista[8])
    Sanguinarias_centro = Vertice('Montanhas Sanguinarias(centro)', lista[9])
    Sanguinarias_norte = Vertice('Montanhas Sanguinarias(norte)', lista[10])
    Deserto_leste = Vertice('Deserto da Perdição(leste)', lista[11])
    Deserto_centro = Vertice('Deserto da Perdição(centro)', lista[12])
    Deserto_oeste = Vertice('Deserto da Perdição(oeste)', lista[13])
    Tauron_leste = Vertice('Imperio de Tauron(leste)', lista[14])
    Tauron_oeste = Vertice('Imperio de Tauron(oeste)', lista[15])
    Tauron_centro = Vertice('Imperio de Tauron(centro)', lista[16])
    Tauron_norte = Vertice('Impero de Tauron(norte)', lista[17])
    Tiberus = Vertice('Tiberus', lista[18])
    Palthar = Vertice('Palthar', lista[19])
    Hippiontar = Vertice('Hippiontar', lista[20])
    Rhond = Vertice('Rhond', lista[21]*10)
    Altrim = Vertice('Altrim', lista[22])
    Nova_malpetrim = Vertice('Nova Malpetrim', lista[23])
    Nimbarann = Vertice('Nimbarann', lista[24])
    Barud = Vertice('Barud', lista[25])
    Thartann = Vertice('Thartann', lista[26])
    Yuvalin = Vertice('Yuvalin', lista[27])
    Kannilar = Vertice('Kannilar', lista[28])
    Zakharin = Vertice('Zakharin', lista[29])
    Valkaria = Vertice('Valkaria', lista[30])
    Coridrian = Vertice('Coridrian', lista[31])
    Villent = Vertice('Villent', lista[32])
    Floresta_Tollon = Vertice('Floresta de Tollon', lista[33])
    Horeen = Vertice('Horeen', lista[34]*10)
    Smokestone = Vertice('Smokestone', lista[35])
    Giluk = Vertice('Giluk', lista[36])
    Fross = Vertice('Fross', lista[37])
    Yukadar = Vertice('Yukadar', lista[38])
    Yuton = Vertice('Yuton', lista[39])
    Roschfallen = Vertice('Roschfallen', lista[40])
    Norm = Vertice('Norm', lista[41]*10)
    Ermos = Vertice('Ermos Púrpuras', lista[42])
    Milothiann = Vertice('Milothiann', lista[43])
    Floresta_Verde = Vertice('Floresta das Escamas Verdes', lista[44])
    Norba = Vertice('Norba', lista[45])
    Cidade_humanos = Vertice('A Cidade Normal dos Humanos', lista[46])
    Coravandor = Vertice('Coravandor', lista[47])
    Adhurian = Vertice('Adhurian', lista[48])
    Ghallistryx = Vertice('Ghallistryx', lista[49])
    Khershandallas = Vertice('Khershandallas', lista[50])
    Cidade_deserto = Vertice('Cidade no Deserto', lista[51])
    Lannestul = Vertice('Lannestul', lista[52])
    Monte_palidor = Vertice('Monte Palidor', lista[53])
    Ruinas = Vertice('Ruinas de Tyrondir', lista[54])
    Sternatchen = Vertice('Sternatchen', lista[55])
    Khalifor = Vertice('Khalifor', lista[56])
    Lysianassa = Vertice('Lysianassa', lista[57])

    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Yuvalin, 140))
    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 710))
    Montanhas_uivantes_leste.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 730))

    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 500))
    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Giluk, 290))
    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Tiberus, 525))
    Montanhas_uivantes_oeste.adiciona_adjacente(Adjacente(Tauron_centro, 850))

    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 710))
    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 485))
    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Barud, 350))
    Montanhas_uivantes_sul.adiciona_adjacente(Adjacente(Giluk, 390))

    Montanhas_uivantes_norte.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 420))
    Montanhas_uivantes_norte.adiciona_adjacente(Adjacente(Tauron_leste, 755))

    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 730))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 485))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_norte, 420))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 500))
    Montanhas_uivantes_centro.adiciona_adjacente(Adjacente(Giluk, 300))

    Savana_oeste.adiciona_adjacente(Adjacente(Tauron_norte, 860))
    Savana_oeste.adiciona_adjacente(Adjacente(Savana_centro, 1250))
    Savana_oeste.adiciona_adjacente(Adjacente(Cidade_deserto, 760))

    Savana_centro.adiciona_adjacente(Adjacente(Savana_oeste, 1250))
    Savana_centro.adiciona_adjacente(Adjacente(Savana_leste, 1380))
    Savana_centro.adiciona_adjacente(Adjacente(Palthar, 755))
    Savana_centro.adiciona_adjacente(Adjacente(Deserto_centro, 810))

    Savana_leste.adiciona_adjacente(Adjacente(Savana_centro, 1380))
    Savana_leste.adiciona_adjacente(Adjacente(Fross, 340))
    Savana_leste.adiciona_adjacente(Adjacente(Deserto_leste, 1000))

    Sanguinarias_sul.adiciona_adjacente(Adjacente(Adhurian, 330))
    Sanguinarias_sul.adiciona_adjacente(Adjacente(Sanguinarias_centro, 1000))

    Sanguinarias_centro.adiciona_adjacente(Adjacente(Sanguinarias_sul, 1000))
    Sanguinarias_centro.adiciona_adjacente(Adjacente(Coravandor, 1100))
    Sanguinarias_centro.adiciona_adjacente(Adjacente(Sanguinarias_norte, 840))
    Sanguinarias_centro.adiciona_adjacente(Adjacente(Khershandallas, 750))

    Sanguinarias_norte.adiciona_adjacente(Adjacente(Sanguinarias_centro, 840))
    Sanguinarias_norte.adiciona_adjacente(Adjacente(Ghallistryx, 350))

    Deserto_leste.adiciona_adjacente(Adjacente(Khershandallas, 1350))
    Deserto_leste.adiciona_adjacente(Adjacente(Savana_leste, 1000))
    Deserto_leste.adiciona_adjacente(Adjacente(Deserto_centro, 1390))

    Deserto_centro.adiciona_adjacente(Adjacente(Deserto_leste, 1390))
    Deserto_centro.adiciona_adjacente(Adjacente(Savana_centro, 810))
    Deserto_centro.adiciona_adjacente(Adjacente(Deserto_oeste, 1325))

    Deserto_oeste.adiciona_adjacente(Adjacente(Deserto_centro, 1325))
    Deserto_oeste.adiciona_adjacente(Adjacente(Cidade_deserto, 200))
    Deserto_oeste.adiciona_adjacente(Adjacente(Lannestul, 1300))

    Tauron_leste.adiciona_adjacente(Adjacente(Montanhas_uivantes_norte, 755))
    Tauron_leste.adiciona_adjacente(Adjacente(Tauron_centro, 1300))

    Tauron_oeste.adiciona_adjacente(Adjacente(Tiberus, 1100))
    Tauron_oeste.adiciona_adjacente(Adjacente(Tauron_centro, 965))

    Tauron_centro.adiciona_adjacente(Adjacente(Tauron_leste, 1300))
    Tauron_centro.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 850))
    Tauron_centro.adiciona_adjacente(Adjacente(Tiberus, 850))
    Tauron_centro.adiciona_adjacente(Adjacente(Tauron_oeste, 965))
    Tauron_centro.adiciona_adjacente(Adjacente(Tauron_norte, 600))

    Tauron_norte.adiciona_adjacente(Adjacente(Tauron_centro, 600))
    Tauron_norte.adiciona_adjacente(Adjacente(Savana_oeste, 860))

    Tiberus.adiciona_adjacente(Adjacente(Altrim, 525))
    Tiberus.adiciona_adjacente(Adjacente(Tauron_oeste, 1100))
    Tiberus.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 430))
    Tiberus.adiciona_adjacente(Adjacente(Tauron_centro, 850))

    Palthar.adiciona_adjacente(Adjacente(Hippiontar, 300))
    Palthar.adiciona_adjacente(Adjacente(Savana_centro, 755))
    Palthar.adiciona_adjacente(Adjacente(Fross, 905))
    Palthar.adiciona_adjacente(Adjacente(Yukadar, 735))

    Hippiontar.adiciona_adjacente(Adjacente(Kannilar, 995))
    Hippiontar.adiciona_adjacente(Adjacente(Palthar, 300))
    Hippiontar.adiciona_adjacente(Adjacente(Yuton, 495))

    Rhond.adiciona_adjacente(Adjacente(Zakharin, 205))

    Altrim.adiciona_adjacente(Adjacente(Nimbarann, 865))
    Altrim.adiciona_adjacente(Adjacente(Nova_malpetrim, 740))
    Altrim.adiciona_adjacente(Adjacente(Smokestone, 360))
    Altrim.adiciona_adjacente(Adjacente(Tiberus, 525))

    Nova_malpetrim.adiciona_adjacente(Adjacente(Altrim, 740))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Nimbarann, 300))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Smokestone, 430))
    Nova_malpetrim.adiciona_adjacente(Adjacente(Lysianassa, 850))

    Nimbarann.adiciona_adjacente(Adjacente(Nova_malpetrim, 300))
    Nimbarann.adiciona_adjacente(Adjacente(Barud, 215))
    Nimbarann.adiciona_adjacente(Adjacente(Altrim, 865))
    Nimbarann.adiciona_adjacente(Adjacente(Smokestone, 550))
    Nimbarann.adiciona_adjacente(Adjacente(Giluk, 600))

    Barud.adiciona_adjacente(Adjacente(Nimbarann, 215))
    Barud.adiciona_adjacente(Adjacente(Floresta_Tollon, 335))
    Barud.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 350))

    Thartann.adiciona_adjacente(Adjacente(Valkaria, 825))
    Thartann.adiciona_adjacente(Adjacente(Floresta_Tollon, 460))
    Thartann.adiciona_adjacente(Adjacente(Ruinas, 845))
    Thartann.adiciona_adjacente(Adjacente(Horeen, 190))

    Yuvalin.adiciona_adjacente(Adjacente(Zakharin, 350))
    Yuvalin.adiciona_adjacente(Adjacente(Montanhas_uivantes_leste, 140))

    Kannilar.adiciona_adjacente(Adjacente(Hippiontar, 995))
    Kannilar.adiciona_adjacente(Adjacente(Villent, 200))
    Kannilar.adiciona_adjacente(Adjacente(Roschfallen, 700))

    Zakharin.adiciona_adjacente(Adjacente(Yuvalin, 350))
    Zakharin.adiciona_adjacente(Adjacente(Rhond, 205))
    Zakharin.adiciona_adjacente(Adjacente(Villent, 300))

    Valkaria.adiciona_adjacente(Adjacente(Coridrian, 510))
    Valkaria.adiciona_adjacente(Adjacente(Thartann, 825))
    Valkaria.adiciona_adjacente(Adjacente(Villent, 480))
    Valkaria.adiciona_adjacente(Adjacente(Monte_palidor, 340))

    Coridrian.adiciona_adjacente(Adjacente(Valkaria, 510))

    Villent.adiciona_adjacente(Adjacente(Valkaria, 480))
    Villent.adiciona_adjacente(Adjacente(Kannilar, 200))
    Villent.adiciona_adjacente(Adjacente(Zakharin, 300))

    Floresta_Tollon.adiciona_adjacente(Adjacente(Thartann, 460))
    Floresta_Tollon.adiciona_adjacente(Adjacente(Barud, 335))

    Horeen.adiciona_adjacente(Adjacente(Thartann, 190))

    Smokestone.adiciona_adjacente(Adjacente(Nimbarann, 550))
    Smokestone.adiciona_adjacente(Adjacente(Nova_malpetrim, 430))
    Smokestone.adiciona_adjacente(Adjacente(Altrim, 360))

    Giluk.adiciona_adjacente(Adjacente(Montanhas_uivantes_sul, 390))
    Giluk.adiciona_adjacente(Adjacente(Montanhas_uivantes_centro, 300))
    Giluk.adiciona_adjacente(Adjacente(Montanhas_uivantes_oeste, 290))
    Giluk.adiciona_adjacente(Adjacente(Nimbarann, 600))

    Fross.adiciona_adjacente(Adjacente(Savana_leste, 340))
    Fross.adiciona_adjacente(Adjacente(Palthar, 905))
    Fross.adiciona_adjacente(Adjacente(Yukadar, 500))

    Yukadar.adiciona_adjacente(Adjacente(Fross, 500))
    Yukadar.adiciona_adjacente(Adjacente(Palthar, 735))
    Yukadar.adiciona_adjacente(Adjacente(Norba, 300))

    Yuton.adiciona_adjacente(Adjacente(Hippiontar, 495))
    Yuton.adiciona_adjacente(Adjacente(Ermos, 550))

    Roschfallen.adiciona_adjacente(Adjacente(Kannilar, 700))
    Roschfallen.adiciona_adjacente(Adjacente(Norm, 235))
    Roschfallen.adiciona_adjacente(Adjacente(Ermos, 400))

    Norm.adiciona_adjacente(Adjacente(Roschfallen, 235))

    Ermos.adiciona_adjacente(Adjacente(Yuton, 550))
    Ermos.adiciona_adjacente(Adjacente(Roschfallen, 400))
    Ermos.adiciona_adjacente(Adjacente(Milothiann, 385))

    Milothiann.adiciona_adjacente(Adjacente(Ermos, 385))
    Milothiann.adiciona_adjacente(Adjacente(Floresta_Verde, 600))

    Floresta_Verde.adiciona_adjacente(Adjacente(Milothiann, 600))
    Floresta_Verde.adiciona_adjacente(Adjacente(Norba, 590))
    Floresta_Verde.adiciona_adjacente(Adjacente(Adhurian, 1290))

    Norba.adiciona_adjacente(Adjacente(Yukadar, 300))
    Norba.adiciona_adjacente(Adjacente(Floresta_Verde, 590))
    Norba.adiciona_adjacente(Adjacente(Cidade_humanos, 980))

    Cidade_humanos.adiciona_adjacente(Adjacente(Norba, 980))
    Cidade_humanos.adiciona_adjacente(Adjacente(Coravandor, 475))

    Coravandor.adiciona_adjacente(Adjacente(Cidade_humanos, 475))
    Coravandor.adiciona_adjacente(Adjacente(Sanguinarias_centro, 1100))

    Adhurian.adiciona_adjacente(Adjacente(Floresta_Verde, 1290))
    Adhurian.adiciona_adjacente(Adjacente(Sanguinarias_sul, 330))

    Ghallistryx.adiciona_adjacente(Adjacente(Sanguinarias_norte, 350))
    Ghallistryx.adiciona_adjacente(Adjacente(Khershandallas, 400))

    Khershandallas.adiciona_adjacente(Adjacente(Ghallistryx, 400))
    Khershandallas.adiciona_adjacente(Adjacente(Sanguinarias_centro, 750))
    Khershandallas.adiciona_adjacente(Adjacente(Deserto_leste, 1350))

    Cidade_deserto.adiciona_adjacente(Adjacente(Deserto_oeste, 200))
    Cidade_deserto.adiciona_adjacente(Adjacente(Savana_oeste, 760))

    Lannestul.adiciona_adjacente(Adjacente(Deserto_oeste, 1300))

    Monte_palidor.adiciona_adjacente(Adjacente(Valkaria, 340))
    Monte_palidor.adiciona_adjacente(Adjacente(Ruinas, 325))

    Ruinas.adiciona_adjacente(Adjacente(Monte_palidor, 325))
    Ruinas.adiciona_adjacente(Adjacente(Thartann, 845))
    Ruinas.adiciona_adjacente(Adjacente(Sternatchen, 500))

    Sternatchen.adiciona_adjacente(Adjacente(Ruinas, 500))
    Sternatchen.adiciona_adjacente(Adjacente(Khalifor, 800))

    Khalifor.adiciona_adjacente(Adjacente(Sternatchen, 800))

    Lysianassa.adiciona_adjacente(Adjacente(Nova_malpetrim, 850))


grafo = Grafo()


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            return
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.nome, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print(45*'-')
        print('Atual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)


def switch_cities(opcao):
    if opcao == 1:
        return grafo.Valkaria
    elif opcao == 2:
        return grafo.Palthar
    elif opcao == 3:
        return grafo.Rhond
    elif opcao == 4:
        return grafo.Nova_malpetrim
    elif opcao == 5:
        return grafo.Barud
    elif opcao == 6:
        return grafo.Yuvalin
    elif opcao == 7:
        return grafo.Zakharin
    elif opcao == 8:
        return grafo.Villent
    elif opcao == 9:
        return grafo.Hippiontar
    elif opcao == 10:
        return grafo.Altrim
    elif opcao == 11:
        return grafo.Nimbarann
    elif opcao == 12:
        return grafo.Thartann
    elif opcao == 13:
        return grafo.Kannilar
    elif opcao == 14:
        return grafo.Coridrian
    elif opcao == 15:
        return grafo.Horeen
    elif opcao == 16:
        return grafo.Smokestone
    elif opcao == 17:
        return grafo.Giluk
    elif opcao == 18:
        return grafo.Fross
    elif opcao == 19:
        return grafo.Yukadar
    elif opcao == 20:
        return grafo.Yuton
    elif opcao == 21:
        return grafo.Roschfallen
    elif opcao == 22:
        return grafo.Norm
    elif opcao == 23:
        return grafo.Milothiann
    elif opcao == 24:
        return grafo.Norba
    elif opcao == 25:
        return grafo.Coravandor
    elif opcao == 26:
        return grafo.Adhurian
    elif opcao == 27:
        return grafo.Lannestul
    elif opcao == 28:
        return grafo.Sternatchen
    elif opcao == 29:
        return grafo.Khalifor
    elif opcao == 30:
        return grafo.Lysianassa
    elif opcao == 31:
        return grafo.Monte_palidor
    elif opcao == 32:
        return grafo.Ghallistryx
    elif opcao == 33:
        return grafo.Montanhas_uivantes_leste
    elif opcao == 34:
        return grafo.Montanhas_uivantes_oeste
    elif opcao == 35:
        return grafo.Montanhas_uivantes_sul
    elif opcao == 36:
        return grafo.Montanhas_uivantes_norte
    elif opcao == 37:
        return grafo.Montanhas_uivantes_centro
    elif opcao == 38:
        return grafo.Savana_oeste
    elif opcao == 39:
        return grafo.Savana_leste
    elif opcao == 40:
        return grafo.Savana_centro
    elif opcao == 41:
        return grafo.Sanguinarias_sul
    elif opcao == 42:
        return grafo.Sanguinarias_centro
    elif opcao == 43:
        return grafo.Sanguinarias_norte
    elif opcao == 44:
        return grafo.Deserto_leste
    elif opcao == 45:
        return grafo.Deserto_centro
    elif opcao == 46:
        return grafo.Deserto_oeste
    elif opcao == 47:
        return grafo.Ermos
    elif opcao == 48:
        return grafo.Floresta_Tollon
    elif opcao == 49:
        return grafo.Floresta_Verde
    elif opcao == 50:
        return grafo.Cidade_humanos
    elif opcao == 51:
        return grafo.Khershandallas
    elif opcao == 52:
        return grafo.Cidade_deserto
    elif opcao == 53:
        return grafo.Ruinas
    elif opcao == 54:
        return grafo.Tauron_leste
    elif opcao == 55:
        return grafo.Tauron_oeste
    elif opcao == 56:
        return grafo.Tauron_centro
    elif opcao == 57:
        return grafo.Tauron_norte
    elif opcao == 58:
        return grafo.Tiberus


busca_aestrela = AEstrela(switch_cities(cidade_destino))
busca_aestrela.buscar(switch_cities(cidade_origem))
print('\n')
