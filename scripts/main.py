from system import System
from planet import Planet
import time
import multiprocessing
from game_stats import game_stats as gs
from main_ui import Main_ui as mu
import multiprocessing.sharedctypes
import cProfile


def main():

    main_loop()




def main_loop():

    # cProfile.run("mu()", sort="cumulative")
    game = mu()



    
#     shared_value = multiprocessing.Manager().dict(gs)
#     #shared_value = multiprocessing.sharedctypes.Value(multiprocessing.sharedctypes.ctypes.py_object, gs)


#     process1 = multiprocessing.Process(target=mu, args=(shared_value,))
#     process2 = multiprocessing.Process(target=game_engine, args=(shared_value,))

#     process2.start()
#     process1.start()

#     process1.join()
#     process2.terminate()  # Afslutter spilmotoren
# def game_engine(shared_value):
#     while True:
#         time.sleep(6)
#         try:
#             value = shared_value["systems"]
#             for system in value:

#                 for planet in system.planets:
#                     planet.mine_planet()
#                     print(planet.planet_iron)
#             shared_value["systems"] = value
#         except Exception as es:
#             print(f"there is an error in the game engine {es}")

if __name__ == "__main__":
 #   multiprocessing.freeze_support()
    main()