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
pixel_column = {}
for current_column,current_pixel in enumerate(step_width_vector):
    pixel_column[current_pixel] = current_column

for i in range(board_rows):
    for j in range(board_columns):
        centers.append((step_width_vector[j],step_width_vector[i],color['WHITE']))
##############

class Backend:

    def __init__(self):
        self.board=py.zeros((12,13))
        self.board[(0,1,2),:]=np.nan
        self.board[(11,10,9),:]=np.nan
        self.board[:,(0,1,2)]=np.nan
        self.board[:,(12,11,10)]=np.nan
        self.scoreboard=np.zeros((2,12,13))
        self.scoreboard[:,(0,1,2),:]=np.nan
        self.scoreboard[:,(11,10,9),:]=np.nan
        self.scoreboard[:,:,(0,1,2)]=np.nan
        self.scoreboard[:,:,(12,11,10)]=np.nan

    def update_board(self,rad,drag):
        if py.isnan(self.board[rad+1,drag]):
            self.board[rad,drag]=py.nan
            return rad
        else:
            return game.update_board(rad+1,drag)



#Frontend functions#
def event_in_circle(list_of_tuples,position,rad):

    for cen in list_of_tuples:
        if math.pow(position[0] - cen[0],2) + math.pow(position[1] - cen[1],2) <= math.pow(rad,2):
            return True,pixel_column[cen[0]]
    return False
            #return False
            #new_centers.append((cen[0],cen[1],cen[2]))
    #return new_centers

#Main#
backend = Backend()
pygame.init()
window = pygame.display.set_mode(resolution)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event_in_circle(centers,event.pos,radius)[0]:
                current_column_frontend = event_in_circle(centers,event.pos,radius)[1]

        pygame.display.update()
    pygame.draw.rect(window, color['BLUE'], [0, 0, resolution[0],resolution[1]], 0)
    #draw new circles using centers list. this list should update accordingly after each correct event

    for center in centers:
        pygame.draw.circle(window,color['WHITE'],(center[0],center[1]),radius)

    #for center in centers:
    #    pygame.draw.circle(window,center[2],(center[0],center[1]),radius)
    pygame.display.flip()
