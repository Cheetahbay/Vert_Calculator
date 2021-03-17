while True:
    try:
        video_fps = int(input("Enter video frame rate: "))
        if video_fps == 0:
            break
        air_frames = int(input("Enter number of frames spent in the air: "))
        if air_frames == 0:
            break
        flight_time = air_frames/video_fps
        height_m = (1 / 2) * 9.81 * (flight_time / 2) ** 2
        height_i = height_m * 39.37
        print("You spent", round(flight_time, 3), "seconds in the air")
        print("Your vertical jump that lasted", round(air_frames, ndigits=2), "frames is", round(height_m, ndigits=3),
              "meters or", round(height_i, ndigits=3), "inches\n\n")

    except ValueError:
        print("Value must be a number!")


