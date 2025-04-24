def VelocidadeMedia(distancia, tempo):
    h, m, s = map(int, tempo.split(":"))
    total_h = h + m/60 + s/3600
    return distancia / total_h