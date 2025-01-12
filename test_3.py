import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1550, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# VALUES NEEDED FOR SIMULATIONS
RED=(255,0,0)
YELLOW = (255, 255, 0)
GREEN=(0,128,0)
BLUE=(0,0,255)
FUCHSIA=(255,0,255)
WHITE = (255, 255, 255)
PURPLE=(128,0,128)
GRAY=(128,128,128)
SCALES={'SCALE_NEPTUNE':(5984000,11594000),'SCALE_URANUS':(4400000,9500000),'SCALE_SATURN':(2700000,5500000),'SCALE_JUPITER':(2000000,4000000),'SCALE_MARS':(800000,1500000),'SCALE_EARTH':(700000,1500000),'SCALE_M_M':(386065,748000),'SCALE_VENUS':(800000,1500000),'SCALE_MERCURY':(650000,1100000)}
COLORS=[RED,YELLOW,GREEN,BLUE,WHITE,PURPLE,FUCHSIA,GRAY]
RADIUS=[10,20,23,15,35,32,27,25]
CELESTIAL_OBJECTS=["mercury_bg.png","venus_bg.png","earth_bg.png","mars_bg.png","jupiter_bg.png","saturn_bg.png","uranus_bg.png","neptune_bg.png"]
SMALL_SCALE_X=2123345
SMALL_SCALE_Y=4114000
LARGE_SCALE_X=5984000
LARGE_SCALE_Y=11594000
a=[0.387e6*149.6,0.723e6*149.6,1.00e6*149.6,1.524e6*149.6,5.203e6*149.6,9.537e6*149.6,19.191e6*149.6,30.068e6*149.6]
e=[0.2056,0.0068,0.0167,0.0934,0.0489,0.0565,0.0463,0.0086]
orbit=[]


'''FUNVTIONS NEEDED FOR SIMULATION'''
def update_position(theta,index,start_looking_in_orbit):
            theta_radians=math.radians(theta) 
            r=(a[index]*(1-e[index]**2))/(1+e[index]*math.cos(theta_radians)) 
            
            if index==0:
                x=r*math.cos(theta_radians)  //SCALES['SCALE_MERCURY'][0]
                y=r*math.sin(theta_radians) //SCALES['SCALE_MERCURY'][1]
                
            if index==1:
                x=-r*math.cos(theta_radians)  //SCALES['SCALE_VENUS'][0]
                y=-r*math.sin(theta_radians) //SCALES['SCALE_VENUS'][1]
                
            if index==2:
                x=-r*math.cos(theta_radians)  //SCALES['SCALE_EARTH'][0]
                y=r*math.sin(theta_radians) //SCALES['SCALE_EARTH'][1]  
                
            if index==3:
                x=r*math.cos(theta_radians)  //SCALES['SCALE_MARS'][0]
                y=-r*math.sin(theta_radians) //SCALES['SCALE_MARS'][1] 
                
            if index==4:
                x=-r*math.cos(theta_radians)  //SCALES['SCALE_JUPITER'][0]
                y=r*math.sin(theta_radians) //SCALES['SCALE_JUPITER'][1]  
                
            if index==5:
                x=r*math.cos(theta_radians)  //SCALES['SCALE_SATURN'][0]
                y=-r*math.sin(theta_radians) //SCALES['SCALE_SATURN'][1] 
            
            if index==6:
                x=r*math.cos(theta_radians)  //SCALES['SCALE_URANUS'][0]
                y=r*math.sin(theta_radians) //SCALES['SCALE_URANUS'][1]
                      
            if index==7:
                x=-r*math.cos(theta_radians)  //SCALES['SCALE_NEPTUNE'][0]
                y=-r*math.sin(theta_radians) //SCALES['SCALE_NEPTUNE'][1]
            
                
            if start_looking_in_orbit == False:
                orbit.append((x,y))
                       
            for i in range(0,len(orbit)):
                pygame.draw.circle(WIN,BLUE,(775+orbit[i][0],400+orbit[i][1]),2)
                   
            print(len(orbit))
            return x,y
            #print(start_looking_in_orbit)
            
def display_celestial_object(x,y,index):
    if index=="NONE":
        image_path="sun_bg.png"
        size= 45
        final_x=x-size
        final_y=y-size
    else:
        image_path = CELESTIAL_OBJECTS[index] 
        size = RADIUS[index]*2# Replace with your image path
        final_x=775+x-size
        final_y=400+y-size
        
    original_image = pygame.image.load(image_path).convert_alpha()

    # Resize the image to a square for circular cropping
     # Diameter of the circle
    image = pygame.transform.smoothscale(original_image, (size*2, size*2))

    # Create a circular mask
    circle_surface = pygame.Surface((size*2, size*2), pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, (255, 255, 255, 255), (size, size), size)
    image.set_colorkey((0, 0, 0))  # Make the background of the image transparent
    circle_surface.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    WIN.blit(circle_surface, (final_x,final_y))       
            



def main():  
    # Main loop
    run = True
    clock = pygame.time.Clock()

    # Create a planet object for Earth
   
    count=0
    start_looking_in_orbit=False
    while run:
        
        clock.tick(60)
        WIN.fill((0, 0, 0))  # Clear the screen with black

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        display_celestial_object(765,400,"NONE")
    
        #pygame.draw.circle(WIN,YELLOW,(765,400),45)#THE SUN
        if count == 360:
            start_looking_in_orbit = True
        
        for index in range(0,len(a)):
            x,y=update_position(count,index,start_looking_in_orbit=start_looking_in_orbit)
            display_celestial_object(x,y,index)
            #pygame.draw.circle(WIN,COLORS[index],(775+x,400+y),RADIUS[index])
            
        # Update the display
        pygame.display.update()
        count+=1
    pygame.quit()

#RUN THE PROGRAM
main()
