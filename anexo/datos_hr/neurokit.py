# pip install neurokit2
# https://dominiquemakowski.github.io/post/simulate_ecg/
# https://pypi.org/project/neurokit2/

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import neurokit2 as nk

data = []

fig = plt.figure()
line, = plt.plot(data)

sample_rate = 100

data = list(nk.ecg_simulate(duration=4, sampling_rate=sample_rate, heart_rate=60))

for i in range(6):
    last_heart_rate = 60+i*10
    data += list(nk.ecg_simulate(duration=4, sampling_rate=sample_rate, heart_rate=last_heart_rate))

for i in range(6):
    data += list(nk.ecg_simulate(duration=4, sampling_rate=sample_rate, heart_rate=(last_heart_rate-i*10)))


data += list(nk.ecg_simulate(duration=4, sampling_rate=sample_rate, heart_rate=60))
data += list(nk.ecg_simulate(duration=4, sampling_rate=sample_rate, heart_rate=60))


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

measure_window = 60
sample_rate = 100
start = 0
finish = measure_window*sample_rate + start

pulsos = np.asanyarray(data[start:finish]) * 1000
t = np.asanyarray([i/float(sample_rate) for i in range(len(data[start:finish]))])

peaks, _ = find_peaks(pulsos, distance=sample_rate/2)

peak_list = np.zeros(shape=(len(pulsos)), dtype=np.bool)
peak_list[peaks] = True


plt.plot(t, pulsos)
plt.plot(peaks/sample_rate, pulsos[peaks], "x")
plt.show()

delta_time_rate = np.diff(peaks)
delta_time = delta_time_rate / sample_rate
promedio = np.mean(delta_time)
pulsaciones_por_minuto = (1/promedio) * 60
print("Pulsaciones", pulsaciones_por_minuto)

window_size = 3

hr = []
for w in range(int(measure_window/window_size)):
    start = w*sample_rate*window_size
    finish = (w+1)*sample_rate*window_size + 1
    d = pulsos[start:finish]
    peaks, _ = find_peaks(d, distance=sample_rate/2)
    delta_time_rate = np.diff(peaks)
    delta_time = delta_time_rate / sample_rate
    promedio = np.mean(delta_time)
    pulsaciones_por_minuto = (1/promedio) * 60
    hr += [pulsaciones_por_minuto]*window_size*sample_rate
    print("Pulsaciones", pulsaciones_por_minuto)

data = list(zip(t.astype(np.int), pulsos, peak_list, hr))

print(len(t), len(pulsos), len(hr), len(peak_list))

import sqlite3

conn = sqlite3.connect('hr2.db')

# Crear el cursor para poder ejecutar las querys
c = conn.cursor()

# Ejecutar una query
c.execute("""
            DROP TABLE IF EXISTS heartrate;
        """)

# Ejecutar una query
c.execute("""
        CREATE TABLE heartrate(
            [id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [time] INTEGER NOT NULL,
            [signal] INTEGER NOT NULL,
            [peak] BOOL NOT NULL,
            [hr] FLOAT NOT NULL,
            [sample_rate] INTEGER NOT NULL
        );
        """)

conn.commit()

for d in data:
    values = [int(d[0]), int(d[1]), bool(d[2]), float(d[3]), sample_rate]
    c.execute('INSERT INTO heartrate (time, signal, peak, hr, sample_rate) VALUES (?,?,?,?,?);', values)

conn.commit()

c.execute('SELECT * FROM heartrate WHERE time =?', (1,))
#c.execute('SELECT * FROM heartrate')
data = c.fetchall()
print(len(data))

conn.close()


