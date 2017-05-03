import pygame,sys,math
import numpy as np
#Parameters#
color={'WHITE':(255, 255, 255),
        'BLACK':(0,0,0),
        'BLUE':(0,0,255),
        'GREEN':(0,255,0),
        'RED':(255,0,0)}
resolution = (700,600)
step_width = resolution[0]/7
step_height = resolution[1]/7
step_width_vector = [i - 50 for i in range(100,resolution[0]+100,step_width)]
board_rows = 6
board_columns = 7
radius = 50
centers = []
assign = {}

for i in range(board_rows):
    for j in range(board_columns):
        centers.append((step_width_vector[j],step_width_vector[i],color['WHITE']))



#Frontend functions#
def check_event_position(list_of_tuples,position,rad):
    new_centers = []
    for cen in list_of_tuples:
        if math.pow(position[0] - cen[0],2) + math.pow(position[1] - cen[1],2) <= math.pow(rad,2):
            #return True
            #print cen

            new_centers.append((cen[0],cen[1],color['GREEN']))
        else:
            #return False
            new_centers.append((cen[0],cen[1],cen[2]))
    return new_centers

#Main#
pygame.init()
window = pygame.display.set_mode(resolution)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check if event is in circle
            #should return True + the current column it is in.
            #the current column is the only thing needed for the whole backendstuff
            #the centers list should check the backend_board, draw white if element = 0
            #do the backend check, if occupied, update backend etc.
            #
            centers = check_event_position(centers,event.pos,radius)
        pygame.display.update()

    pygame.draw.rect(window, color['BLUE'], [0, 0, resolution[0],resolution[1]], 0)
    #draw new circles using centers list. this list should update accordingly after each correct event

    for center in centers:
        pygame.draw.circle(window,center[2],(center[0],center[1]),radius)
    pygame.display.flip()
