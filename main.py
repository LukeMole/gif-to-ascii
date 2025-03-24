import cv2
import os
import time

def create_ascii_frame(img_array):
    #goes through every row in the grayscale image and assigns ASCII characters based on brightness
    ascii_frame = ''
    for row in img_array:
        ascii_row = ''
        for item in row:
            if item > 200:
                ascii_row += '#'
            elif item > 125:
                ascii_row += '?'
            elif item > 50:
                ascii_row += '/'
            else:
                ascii_row += '.'
        #creates a full text based ASCII image and returns it
        ascii_frame += ascii_row + '\n'
    
    return ascii_frame
            

def convert_gif_to_ascii(gif_name, img_size):
    all_frames = []
    gif = cv2.VideoCapture(gif_name)
    frames = []
    ret, frame = gif.read()
    #goes through every frame and changes its color, resizes it and appends it to the frames list
    while ret:
        ret, frame = gif.read()
        if not ret:
            break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (img_size['x'],img_size['y']))
        frames.append(frame)
    for frame in frames:
        all_frames.append(create_ascii_frame(frame))

    #returns a full animation list with complete text based frames
    return all_frames

def play_ascii_gif(frames, fps):
    #plays the ASCII gif indefinitely based on the user set FPS
    while True:
        for frame in frames:
            time.sleep(fps)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)



if __name__ == '__main__':
    #input area for gif parameters
    gif_name = input('gif name: ')
    while True:
        try:
            speed = input('fps: ')
            speed = 1/int(speed)
            break
        except ValueError:
            pass
    gif_size = {'x':64,'y':48}
    all_frames = convert_gif_to_ascii(gif_name, gif_size)
    play_ascii_gif(all_frames, speed)