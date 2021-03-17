import json
# def main():
#     def vertical_calc():
#         framerate = input("Enter the frame rate of the video: ")
#         nframes = int(input("Enter the number of frames spent in the air: "))
#         sec = nframes / int(framerate)
#         vheightm = 0 + (1 / 2) * 9.81 * ((sec / 2) ** 2)
#         vheighti = vheightm * 39.37
#         print("You spent", sec, "seconds in the air")
#         print("Your vertical jump that lasted", round(nframes, ndigits=2), "frames is", round(vheightm, ndigits=3),
#               "meters or", round(vheighti, ndigits=8), "inches")

    # vertical_calc()


# main()

while True:
    try:
        video_fps = int(input("Enter video frame rate: "))
        air_frames = int(input("Enter number of frames spent in the air: "))

        flight_time = air_frames/video_fps
        height_m = 0 + (1 / 2) * 9.81 * ((flight_time / 2) ** 2)
        height_i = height_m + 39.37
        print("You spent", round(flight_time, 3), "seconds in the air")
        print("Your vertical jump that lasted", round(air_frames, ndigits=2), "frames is", round(height_m, ndigits=3),
              "meters or", round(height_i, ndigits=8), "inches\n\n")

    except ValueError:
        print("Value must be a number!")

# class VerticalJump:
#     def __init__(self, fr: int, ft: int):
#         # assert fr == int
#         self.frame_rate = fr
#         self.flight_time = ft
#
#     def calculate(self):
#         flight_time = self.flight_time / self.frame_rate
#         height_m = 0 + (1 / 2) * 9.81 * ((flight_time / 2) ** 2)
#         height_i = height_m + 39.37
#         print("You spent", flight_time, "seconds in the air")
#         print("Your vertical jump that lasted", round(self.flight_time, ndigits=2), "frames is",
#               round(height_m, ndigits=3),
#               "meters or", round(height_i, ndigits=8), "inches\n\n")
#
#
# vj = VerticalJump(240, 220)
# vj.calculate()

