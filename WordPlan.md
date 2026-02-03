# Core Idea
Load into a world that has been untouched by people. 

You are able to pick up whatever you want and do whatever you want to anything. 
The key is realisim. When wanted.

Think of it as a way to do things in the world without doing them irl. 

# Crafting
Crafting items can be difficult as there can be many ways to create one thing. Some better than others in various ways. There needs to be a dynamic way of adding new crafting recipies.

There might need to be a system that limits how much items you can craft at a time in certain stages. This can be done in a few ways. From either taking a lot of energy to do something, taking a lot of time to do, or having a lot of steps to make an item.

# World Generation
This engine needs to be able to support 3D maps. There will be moutains, caves, and oceans. Along with biomes in the future. 

Along with just terrain there needs to be resource generation. From trees to stones and sticks to ores. This will also need to be altered once we add biomes as different biomes with different conditions will produce different resources.  

The base thing that is needed for a MVP is Trees and Stones. 

## Trees
Trees are able to drop leaves and sticks. Will this be auto generated and nothing else happens or will there be a dynamic system that will drop resources after a certain amount of time? 

# Camera
The user will experience a seemless world generation with the world generation around them without any loading. They will be moving smoothly with no blocky movement. Grids might be used to make buildings and other things but for movement it will be smooth. 

## Camera Following
The camera shouldn't move in the direction that the player is moving until the player reaches a certain part of the screen cords, like a limit. 

## World Cord vs Camera Cords
There needs to be a system to track world position. This position will not be based around the camera. Camera position will be calculated based on world position and the distance of the player. 

### Item Loading
The items won't load on the left side of the screen even if they should because the cords are based around the top right of the object in pygame.

### Plan
The camera will have a world cord that we can base off to allow calculation of items. The camera will only move in the world when the player moves far enough in either direction.

### Math
To calculate if the item is in the view of the camera we can use the camera position (center of the screen) along with the screen width and height to calculate the ranges of x and y the camera can see in the world. 
Ex. If the camera's position is 450, 250. And the screen's dimentions are 800, 450. Then performing the following calculations will give up the ranges the items have to be in to render. 
450 -+ 400(half of 800) = x range

# Inventory
The player will need to store items but there is a limited amount of items the player can hold by themselves. Thus there will be a realistic inventory system where they can have the following can have items stored: Hands (Active), Back(Inactive & If able), Teeth/Mouth (Inactive). Unless there is clothing and tools to help store more, this is the MVP.

# Key Components 
- Inventory System
    - Limited storing system
        - Hands, Back, Teeth/Mouth
- Crafting System
    - Needs to be dynamic in code.
    - Limits needed?
- World Generation
    - Support 3D generation
    - Tree & Stone generation
    - Ore Generation
    - Biomes (TBD)
- Camera
    - Smooth motion
        - No grid system
    - Item loading (Come back to)