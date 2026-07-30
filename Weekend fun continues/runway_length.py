# name: runway_length
# read speed  in m/s and acceleration in m/s2
# calculate length using length = (v * v) / 2 * a
# display length

speed = float( input("Enter speed: "))

acceleration = float( input("Enter acceleration: "))

length = (speed * speed) / (2 * acceleration)

print("The minimum runway length for this airplane is ", length)