import tkinter as tk
from random import randint
import math
from PIL import Image, ImageTk
import pygame

l=['🍒','🍌','🍇','🍉','🍏','⑦','😍','😀']
def play_sound_spinning():
    sound_path = r"path_to_your_sound_file\mixkit-slot-machine-win-siren-1929.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
class SpinWheel(tk.Canvas):
    def __init__(self, master, sections):
        super().__init__(master, width=600, height=600, bg='#FFDB58')
        self.sections = sections
        self.angle_per_section = 360 / sections
        self.spin_result = None
        self.create_wheel()

    def create_wheel(self):
        for i in range(self.sections):
            start_angle = i * self.angle_per_section
            end_angle = (i + 1) * self.angle_per_section
            color = 'red' if i % 2 == 0 else 'blue'
            mid_angle = (start_angle + end_angle) / 2
            self.create_arc(20, 20, 600, 600, start=start_angle, extent=self.angle_per_section, fill=color)
        self.create_text(500, 390, text=(l[0]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(390, 500, text=(l[1]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(220, 500, text=(l[2]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(125, 390, text=(l[3]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(125, 220, text=(l[4]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(240, 125, text=(l[5]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(390, 125, text=(l[6]), anchor = 'center', font=("Helvetica", 70, "bold"))
        self.create_text(500, 220, text=(l[7]), anchor = 'center', font=("Helvetica", 70, "bold"))

    def spin(self):
        self.spin_result = randint(0, self.sections - 1)
        target_angle = 360 * 3 + self.spin_result * self.angle_per_section
        play_sound_spinning()
        self.animate_spin(target_angle, 0)

    def animate_spin(self, target_angle, current_angle):
        if current_angle < target_angle:
            self.delete('pointer')
            self.create_line(310, 310, self.get_x_coordinate(current_angle), self.get_y_coordinate(current_angle),
                             width=10, tags='pointer', arrow=tk.LAST, arrowshape=(16, 20, 8), fill='yellow')
            self.after(40, self.animate_spin, target_angle, current_angle + 10)
        else:
            if (self.spin_result-1)%2==0:
                result_label.config(text=f"Result → {l[self.spin_result-1]}", foreground = 'blue',font = ("Arial",40,"bold"))
            else:
                result_label.config(text=f"Result → {l[self.spin_result-1]}", foreground = 'red',font = ("Arial",40,"bold"))
            
    def get_x_coordinate(self, angle):
        return 300 + 200 * math.cos(math.radians(angle))

    def get_y_coordinate(self, angle):
        return 300 + 200 * math.sin(math.radians(angle))

if __name__=="__main__":
    root = tk.Tk()
    root.title("WheeL'o'Fortune")
    icon_image = ImageTk.PhotoImage(file = r"path_to_your_icon_file\icon.png")
    root.iconphoto(True, icon_image)
    bg = ImageTk.PhotoImage(file=r"path_to_your_background_file\background1(edited1).png")
    label1 = tk.Label(root, image=bg)
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    spin_wheel = SpinWheel(root, sections=8)
    spin_button = tk.Button(root, text="<SPIN>", background = '#FFDB58',foreground = 'green',font = ("Arial",40,'bold'), command=spin_wheel.spin)
    result_label = tk.Label(root, text="Result → ",background = "#FFDB58",foreground = 'green',font = ("Arial",40,'bold'))
    spin_wheel.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
    spin_button.grid(row=1, column=1, pady=10)
    result_label.grid(row=2, column=0, pady=10, columnspan=3)

    root.mainloop()
