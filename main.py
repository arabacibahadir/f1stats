import fastf1 as ff1
from fastf1 import plotting
from fastf1.core import Laps
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
import pandas as pd
from timple.timedelta import strftimedelta


def main():
    plotting.setup_mpl()
    laps_driver1 = laps.pick_driver(driver1)
    laps_driver2 = laps.pick_driver(driver2)
    fastest_driver1 = laps_driver1.pick_fastest()
    fastest_driver2 = laps_driver2.pick_fastest()
    telemetry_driver1 = fastest_driver1.get_car_data().add_distance()
    telemetry_driver2 = fastest_driver2.get_car_data().add_distance()

    def track():
        lap = laps.pick_fastest()
        tel = lap.get_telemetry()
        x = np.array(tel['X'].values)
        y = np.array(tel['Y'].values)
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        gear = tel['nGear'].to_numpy().astype(float)
        cmap = plt.get_cmap('Paired')
        lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N + 1), cmap=cmap)
        lc_comp.set_array(gear)
        lc_comp.set_linewidth(5)
        plt.figure(figsize=(9, 9))
        plt.gca().add_collection(lc_comp)
        plt.axis('equal')
        plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
        cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
        cbar.set_ticks(np.arange(1.5, 9.5))
        cbar.set_ticklabels(np.arange(1, 9))
        plt.suptitle(f"Fastest Lap Gear Shift Visualization")

    def gas(*args):
        fig, ax = plt.subplots(3, figsize=(8, 8))
        fig.suptitle("Fastest Race Lap Telemetry Comparison")
        data = ['Speed', 'Throttle', 'Brake']
        for i in range(3):
            ax[i].plot(telemetry_driver1['Distance'], telemetry_driver1[data[i]], label=driver1)
            ax[i].plot(telemetry_driver2['Distance'], telemetry_driver2[data[i]], label=driver2)
            ax[i].set(ylabel=data[i])

        for a in ax.flat:
            a.label_outer()
        ax[0].legend()
        fig.subplots_adjust(left=0.08, bottom=0.04, right=1, top=1, wspace=None, hspace=None)

    def compare(*args):
        fig, ax = plt.subplots()
        ax.plot(laps_driver1['LapNumber'], laps_driver1['LapTime'], color='red')
        ax.plot(laps_driver2['LapNumber'], laps_driver2['LapTime'], color='cyan')
        ax.set_title(f"Red:{driver1} vs Cyan:{driver2}")
        ax.set_xlabel("Lap Number")
        ax.set_ylabel("Lap Time")
        plt.legend()
        fig.subplots_adjust(right=1, top=0.9)

    def qualifying():

        ff1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme=None, misc_mpl_mods=False)
        drivers = pd.unique(laps['Driver'])
        list_fastest_laps = list()
        for drv in drivers:
            drvs_fastest_lap = laps.pick_driver(drv).pick_fastest()
            list_fastest_laps.append(drvs_fastest_lap)
        fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)
        pole_lap = fastest_laps.pick_fastest()
        fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']
        team_colors = list()
        for index, lap in fastest_laps.iterlaps():
            color = ff1.plotting.team_color(lap['Team'])
            team_colors.append(color)
        fig, ax = plt.subplots()
        ax.barh(fastest_laps.index, fastest_laps['LapTimeDelta'],
                color=team_colors, edgecolor='grey')
        ax.set_yticks(fastest_laps.index)
        ax.set_yticklabels(fastest_laps['Driver'])
        ax.invert_yaxis()
        ax.set_axisbelow(True)
        ax.xaxis.grid(True, linestyle='--', color='black', zorder=-1000)
        lap_time_string = strftimedelta(pole_lap['LapTime'], '%m:%s.%ms')
        plt.suptitle(f"{race.weekend.name} {race.weekend.year} Qualifying\n"
                     f"Fastest Lap: {lap_time_string} ({pole_lap['Driver']})")

    track()
    gas()
    compare(laps_driver1, laps_driver2)
    qualifying()
    plt.show()
    # add weather
    # more stats
    # ..

if __name__ == '__main__':
    driver1 = 'BOT'
    driver2 = 'HAM'
    ff1.Cache.enable_cache(r'C:\Users\bahadir\PycharmProjects\f1stats\cache')
    race = ff1.get_session(2021, 'Zandvoort', 'R')
    laps = race.load_laps(with_telemetry=True)
    main()
