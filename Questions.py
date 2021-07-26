def turtle_movement(activities, turtle):
    order = ["F", "R", "F", "F", "L", "L", "R", "L", "F", "R"] # All the movements for each question answered correctly
    movements = { 
        0: 100,
        1: 170,
        2: 170,
        3: 170,
        4: 100,
        5: 100,
        6: 100,
        7: 155,
        8: 155,
        9: 100,
    }

    index = 0
    for x, y in activities.items(): # Tracks the movement of the turtle when each question is answered correct/incorrectly
        print("")
        print(x)
        answer = input("Answer: ")
        if answer.upper() == y:
            print("Correct.")
            print("")
            direction = order[index]
            if direction == "R":
                turtle.right(90)

            elif direction == "L":
                turtle.left(90)

            turtle.forward(movements[index])
            index += 1
            continue

        print("Incorrect.")

    print("")
    if index == 10:
        print("Congratulations! You successfully completed the maze and got all questions right!")
    else:
        print("You sadly didn't complete the maze, getting a ", index, " out of 10 correct.")
    print("")

# All the questions and answers for the AP Physics 1 units.
def practice(topic, turtle):
    topic = topic.upper()
    print("Treat g as 9.8 m/s^2. | Treat i after a variable as initial and f after a variable as final such as vi and vf for velocity. | Delta # means change in # | If there are multiple objects, velocity, and initial/final, the order for variables is velocity then object number than initial/final i.e. v1f | Unless otherwise stated, all these situations take place on Earth.")
    print("")
    print("")
    if (topic == "A"):
        activities = {
            "1. Which variable represents the position of an object?  A. x | B. a | C. vf | D. t": "A",
            "2. What is the center of mass, and what do you need to find it?  A. The middle distance of a mass | B. Where the least mass is located using distance | C. Where most of the mass is located using mass | D. Where most of the mass is located using mass and distance.": "D", 
            "3. What is the rate of change in position over a certain amount of time with a specific direction?  A. Velocity | B. Speed | C. None of the above | D. They are the same thing": "A", 
            "4. What measures how much an object has moved over its entire path?  A. Displacement | B. Distance | C. None of the above | D. They are the same thing": "B", 
            "5. What is the area under the curve of a velocity vs time graph?  A. Acceleration | B. Distance| C. Position| D. Displacement": "D", 
            "6. If a football is kicked upwards with an initial velocity of 5 m/s at 60 degrees above the horizontal, how long will it take until it reaches its peak height?  A. 0.52 s | B. 0.44 s | C. 0.26 s | D. 0.88 s": "B", 
            "7. A man runs westward from his house for 30 minutes at 10 meters per hour. He then takes a 2-minute break and runs back to his house at 7 meters per hour. How long is his trip?  A. 74.86 hours | B. 62 minutes | C. 74.86 minutes | D. Cannot determine without the distance the man ran from his house.": "C", 
            "8. When is the velocity increasing?  A. Either the velocity or acceleration is increasing| B. Either the velocity or acceleration is decreasing.| C. If both the acceleration and velocity are increasing/decreasing| D. Cannot be determined without more information": "C",
            "9. What is the acceleration due to gravity at the top of a curve in projectile motion?  A. 0 m/s^2 | B. 9.8 m/s^2 | C. -9.8 m/s^2 | D. There is no acceleration.": "C",
            "10. What is the area under an velocity vs time graph?  A. Final Velocity | B. Change in Position | C. Change in Velocity | D. Change in Acceleration ": "B"
        }

    elif (topic == "B"):
        activities = {
            "1. What is the relationship between acceleration and force, and which causes the other?  A. a = F/m; acceleration causes force. | B. F = a/m; acceleration causes force. | C. a = F/m; force causes acceleration. | D. F = a/m; force causes acceleration": "C", 
            "2. During translational equilibrium, an object is...  A. At rest or moving at a constant velocity | B. Only at rest. | C. Only moving at a constant velocity. | D. Depends on the state of the object": "A", 
            "3. Between kinetic and static friction, which will always be greater than the other?  A. Kinetic Friction | B. Kinetic Friction | C. They will always be the same | D. More information must be known": "B", 
            "4. Which is FALSE about inertial and gravitational mass?  A. Inertial mass measures an object's resistance to acceleration. | B. Gravitational mass determines the weight of an object | C. Inertial mass and gravitational mass are experimentally unidentical.| D. Gravitational mass can be calculated with mg.": "C", 
            "5. A 100 kg box, initially at rest, is pushed with 300 N horizontally for 2 seconds with negligable friction. What will be the box's speed after 2 seconds?  A. 6 m/s | B. 9 m/s | C. 3 m/s | D. 12 m/s ": "A", 
            "6. What is the spring constant of a spring compressing from 30 cm to 20 cm with a force of 5 N?  A. 25 N/m | B. 12.5 N/m | C. 0.5 N/m | D. 50 N/m": "D", 
            "7. When moving up in an elevator, what is the normal force?  A. mg - ma | B. ma - mg | C. mg + ma | D. Depends on the mass/acceleration due to gravity": "C", 
            "8. In a basic table-pulley system with blocks A (5 kg) and B (10 kg), each of which is connected by a string (negligable friction) and dangling over the air on one end of the table. What will the acceleration of the system be?  A. a = 1.64 m/s^2 | B. a = 9.8 m/s^2 | C. a = 6.53 m/s^2 | D. a = 3.27 m/s^2": "D", 
            "9. A block with mass 10 kg is on an incline with an angle of 30 degrees above the horizontal. What is the normal force on the block?  A. 49 N | B. 84.87 N | C. 98 N | D. 56.55 N": "B", 
            "10. Compare the normal force (FN) and weight (FG) of an object on the ground and whether they are a third-law pair.  A. FN = FG; not a third-law pair. | B. FN = FG; a third-law pair. | C. FN > FG; not a third-law pair. | D. FN < FG; a third-law pair.": "A"
        }
    elif (topic == "C"):
        activities = {
            "1. Which is NOT a type of energy?   A. Kinetic | B. Potential | C. Thermal | D.  Spring": "D", 
            "2. Express the Conversation of Energy with PE (Potential Energy) and KE (Kinetic Energy), using i (Initial) and f (Final):  A. PEi + KEf = PEf + KEi | B. PE = KE | C. PEi + KEi = PEf + KEf| D. PEf + KEi = PEi + KEf": "C", 
            "3. What is the potential energy for a spring with k = 25 N/m and change in x = 0.5?   A. 6.25 J | B. 12.5 J | C. 25 J | D. 3.125 J": "D", 
            "4. What is the area under a force vs displacement graph?   A. Work | B. Final Energy | C. Initial Energy | D. None of the Above": "A", 
            "5. What is the gravitational potential energy if g is NOT constant?  A. mgh | B. G m1 m2 / r^2 | C. -G m1 m2 / r^2 | D. -mgh": "C", 
            "6. All of these equations are for work that can be used in ANY situation (given the variables are known) except...  A. W = FdcosTheta | B. W = MEf - MEi | C. W = 1/2m vf^2 - 1/2m vi^2 | D. W = KEf - KEi": "B", 
            "7. Friction causes what type of decrease in kinetic energy?  A. Linear | B. Exponential | C. No change | D. Depends on the type of friction and situation": "A", 
            "8. Which is false about Hooke's Law?  A. It states that Fs = k * x | B. Fs represents the spring's restoring force | C. Robert Hooke discovered this law in 1660 | D. All of the statements are true.": "D", 
            "9. What is true about a nonconservative force?  A. It's a force that exists in ideal situations | B. It's when the force of gravity acts between the Earth and another mass | C. A force that does not depend on the path taken. | D. It's a force that does not exist in ideal situations": "D", 
            "10. Which is NOT an expression for Power?   A. Acceleration/Position | B. Work/Time | C. Force * Velocity | D. All of the expressions equal Power": "A" 
        }
    elif (topic == "D"):
        activities = {
            "1. Which of these is NOT an equation for Impulse?  A. mvf - mvi | B. F * Delta t | C. pf - pi | D. m1v1 - m2v2": "D", 
            "2. Impulse are typically calculated through the area under what graph?  A. Force vs Displacement Graph | B. Mass vs Time Graph | C. Momentum vs Displacement Graph | D. Force vs Time Graph": "D", 
            "3. Describe the kinetic energy (KE) and momentum (P) during an elastic collision.  A. KE is not conserved, but P is | B. Neither KE nor P are conserved | C. KE and P are both conserved before and after collision. | D. KE is conserved, but P is not": "C", 
            "4. Express the equation for a perfectly inelastic collision using mass (m) and velocity (v) with objects 1 and 2.  A. m1v1 - m2v2 = (m1 + m2)vf | B. m1v1 - m2v2 = (m1 - m2)vf | C. 1/2m v1i^2 + 1/2m v2i^2 = 1/2m v1f^2 + 1/2m v2f^2| D. ": "A", 
            "5. When is momentum conserved?  A. As long as the velocity and mass are constant | B. As long as there are no forces at all | C. As long as there is no net external force | D. Momentum is always conserved": "C", 
            "6. Find the momentum of a 10 gram object moving at 2.5 km/s.  A. 25 kg*m/s | B. 25 kg*m/s | C. 0.25 kg*m/s | D. 0.025 kg*m/s": "B", 
            "7. A 600-gram bird rests on a 1.2-kg object. It later pushes off the object at 2 m/s. What's the speed of the object when it recoils backward by the bird?  A. 1.2 m/s | B. 7.2 m/s | C. 0.36 m/s | D. 1 m/s": "D", 
            "8. Object 1 weighs 120 kg at 4 m/s and horizontally collides with Object 2, which is at rest and weighs 200 kg, resulting in the objects going in different directions, with Object 1's post-collision velocity at 2.4 m/s. What's the post-collision speed of Object 2 if no kinetic energy is lost?  A. 2.48 m/s | B. 4.96 m/s | C. 0.96 m/s | D. 1.92 m/s": "A", 
            "9. Object 1 (50 kg), moving north at 4.7 m/s, collides with and sticks to Object 2 (70 kg), which was moving east at 3.5 m/s. If momentum is conserved, what is the speed and direction of the objects post-collision?  A. 4.0 m/s, 46.19 degrees North of East | B. 2.83 m/s, 43.81 degrees North of East | C. 4.0 m/s, 43.81 degrees North of East | D. 2.83 m/s, 46.19 degrees North of East": "B", 
            "10. When the Earth is orbiting the sun, is momentum conserved?  A. Velocity is conserved, so momentum is conserved | B. Mass and time are conserved, so momentum is conserved | C. Velocity changes, so momentum is not conserved | D. Time changes, so momentum is not conserved": "C" 
        }
    elif (topic == "E"): # Rotational Kinematics
        activities = { 
            "1. Given rotational kinematic values, how do you convert them to translational values?  A. Divide the rotational value by the radius of the object | B. Divide the rotational value by time. | C. Multiply the rotational value by the radius of the object | D. You cannot convert from rotational to translational.": "C", 
            "2. Which is NOT an expression for centripetal force (ac is centripetal acceleration, and w is angular speed)?  A. m * ac | B. mv^2/r | C. w * mr/v | D. r * w^2 ": "C", 
            "3. When a car is speeding on a roundabout, which of the following is true?  A. The centripetal acceleration is not equal to the static friction force. | B. The static friction force is towards the circle. | C. The acceleration points perpendicular to the velocity of the car. | D. All of the above": "B", 
            "4. A ruler is spun in a circle around its end; A and B are two distinct points on the ruler, where point A is farther from the end than point B; what is true about their accelerations?  A. Point A has a greater angular acceleration than Point B. | B. Both points have the same translational acceleration. | C. Both points have the same angular and translational acceleration. | D. Both points have the same angular acceleration and different translational acceleration.": "D",
            "5. Calculate the angular velocity of a sphere rotating with mass 5 kg, radius of 40 centimeters, and a period of 2 seconds.  A. 3.14 rad/s | B. 1.27 rad/s | C. 1.88 rad/s | D. 1 rad/s": "A", 
            "6. A ball with mass 10 kg and diameter of 7 meters rolls down an incline at 8 m/s. What is its normal force?  A. 182.86 N | B. 98 N | C. 84.86 N | D. 280.86 N": "C", 
            "7. A sphere of mass 22 kg and a radius of 12 meters rolls up a hill; at a certain moment, its normal force is 80 Newtons. What is the sphere's angular velocity at that point?  A. 0.717 rad/s | B. 8.60 rad/s | C. 12.7 rad/s | D. 1.06 rad/s": "A", 
            "8. A rod of 50 grams and 0.43 meters is held in place and is being spun about its axis at a frequency of 1.5 Hz. What is the centripetal force on the rod after those revolutions?  A. 202.6 N | B. 191.0 N | C. 0.202 N | D. 1.91 N": "D", 
            "9. When a rollercoaster reaches the top of a circular loop, which expression represents the forces acting on it?  A. mv^2/r + mg | B. mv^2/r | C. mv^2/r - mg | D. mg - mv^2/r": "A",
            "10. Which of the following is NOT one of Kepler's laws?  A. Planets all have elliptical orbits. | B. T = 4pi^2 r/GM | C. The radius cubed divided by the time taken to make one cycle cubed is the same for all planets. | D. Planets cover an equal area over an equal amount of time.": "B",
        }
    elif (topic == "F"):
        activities = {
            "1. What is torque?  A. The ability to cause angular velocity.| B. The ability to cause angular acceleration. | C. The ability to cause linear velocity.| D. The ability to cause angular velocity.": "B", 
            "2. When does an object have rotational kinetic energy?  A. When an object is dropped. | B. When an object is rolling with slipping down an incline. | C. When the surface the object goes down has static friction. | D. When an object is rolling without slipping down an incline.": "D", 
            "3. What is false about the moment of inertia?  A. It represents an object's resistance to angular acceleration. | B. Increasing mass or radius increases the moment of inertia. | C. A hollow sphere has a greater moment of inertia than a solid sphere. | D. The moment of inertia can be expressed as the angular velocity divided by the angular momentum.": "D", 
            "4. When is an object in rotational equilibrium?  A. If the net external force on the object is zero. | B. If the net external torque on the object is zero. | C. If there is no torque acting on the object at all. | D. If the object is at rest.": "B", 
            "5. Calculate the torque when 50 Newtons of downward (perpendicular) force is applied at an angle of 40 degrees to a wrench of length 20 centimeters held horizontally to unscrew a nut.  A. 64.28 N*m | B. 76.60 N*m | C. 6.428 N*m | D. 7.660 N*m": "C", 
            "6. How much rotational kinetic energy does a ball of mass 5 kg, final velocity of 30 m/s, and radius of 0.45 meters have when rolling down an incline 60 ft vertically high with slipping?   A. 690 J | B. 2250 J | C. 2940 J | D. 0 J": "D", 
            "7. A solid and hollow sphere are simultaneously released and roll down an incline. Which reaches the ground faster?  A. The solid sphere | B. The hollow sphere | C. Both reach the ground at the same time. | D. It's impossible to tell without more information.": "A",  
            "8. A 40 kg disk with a radius of 0.35 meters is rotating at 25 m/s; later, a 20 kg disk with a radius of 15 centimeters is placed on it. What's the new angular speed of the system? (Moment of Inertia constant for disk is 0.5)  A. 9.536 rad/s | B. 10.41 rad/s | C. 22.90 rad/s | D. 21.12 rad/s": "B", 
            "9. There are two ropes, one hanging on the ceiling and another on a horizontal wall, both connecting to the same object of mass 10 kg and holding it in place, where the one hanging on the ceiling is to the right of the object and connects to it at an angle of 50 degrees above the horizontal, but the one from the wall is perfectly horizontal to the object. Calculate the tension in rope B.  A. 152.46 N | B. 127.93 N | C. 62.99 N | D. 75.07 N": "A", 
            "10. What's the difference between rotational and circular motion?  A. Rotational motion is caused by a centripetal force, while circular motion is caused by torque| B. Rotational motion is around a fixed path, while circular motion is within the rotating body | C. Rotational motion is caused by torque, while circular motion is caused by a centripetal force | D. They are equivalent.": "C" 
        }
    elif (topic == "G"):
        print("G is gravitational constant, and M is mass.")
        activities = {
            "1. What is the speed of an aircraft orbiting the Earth (R = radius, t = time)?  A. G m1m2 / r^2 | B. 2pi R/t | C. mg | D. mv^2/r ": "B", 
            "2. What is considered the radius (R) between two objects in space like a spacecraft and Earth?  A. The distance between the center of the larger object to the surface of the smaller object. | B. The distance between the center of the smaller object to the surface of the larger object. | C. The distance between the center of masses of both objects. | D. The distance between the surfaces of both objects.": "C", 
            "3. What is the force of gravity anywhere in the universe between objects 1 and 2 with masses m1 and m2?  A. -G m1m2/r^2 | B. mg | C. -G m1m2/r | D. G m1m2/r^2 ": "D", 
            "4. Choose the correct expression for the universal gravitational potential energy if g is not conserved between objects 1 and 2 with masses m1 and m2.  A. mg | B. -G m1m2/r | C. G m1m2/r | D. G m1m2/r^2": "B", 
            "5. What is the value of G (not g, but G)?  A. 6.67 * 10^-11 N m^2/kg^2 | B. 9.8 m/s^2 | C. 6.67 * 10^-9 N m^2/kg^2 | D. None of the above.": "A",
            "6. Find the force of gravity on two spheres A (70 kg with radius of 50 meters) and B (50 kg and radius of 25 meters) separated by 5 kilometers.  A. 2.92 * 10^-3 N | B. 2.92 * 10^-9 | C. 4.6 * 10^-5 N | D. 4.67 * 10^-5 N": "C", 
            "7. What is the mass of Earth, which has a radius of about 6,378 kilometers?  A. 6.099 * 10^24 kg | B. 5.977 * 10^24 kg | C. 9.371 * 10^17 | D. Cannot be determined without knowing Earth's weight.": "B", 
            "8. What is the speed of an aircraft 10.5 kilometers above Earth's surface orbiting a planet with mass 8 * 10^25 kg and a radius of 7,000 kilometers?  A. 8.73 * 10^5 m/s | B. 1.14 * 10^22 m/s | C. 7.62 * 10^11 m/s | D. You cannot find the answer without knowing the period.": "A", 
            "9. Find the acceleration due to gravity between object A (3,000 kg and radius of 400 km) and planet B (6.23 * 10^16 kg and radius of 2,000 km), which have a 100 km distance between their surfaces.  A. 0.721 m/s^2 | B. 415.54 m/s^2 | C. 0.665 m/s^2 | D. This cannot be calculated without knowing the force of gravity on the objects.": "C", 
            "10. What is the Universal Gravitational Potential Energy (UGP) of a single object with mass m and radius r?  A. mg | B. -G m m / r | C. G m m / r^2 | D. You can't calculate UGP without another object": "D" 
        }
    elif (topic == "H"):
        activities = {
            "1. Can you use kinematic equations with simple harmonic motion (SHM)?  A. Yes, because kinematics deals with the motion of objects, and SHM is the motion of an object and spring. | B. Yes, because SHM is uniformly accelerated motion.| C. No, because SHM is linear motion. | D. No, because SHM is not uniformly accelerated motion.": "D", 
            "2. What is the equation of the period of a mass-spring system?  A. T = 2 pi sqrt(L/g) | B. T = 2 pi sqrt(m/k) | C. T = 2 pi sqrt(k/m) | D. T = 2 pi sqrt(g/L)": "B", 
            "3. What's the relationship between the acceleration and position of a mass-spring system?  A. When the acceleration is at its smallest, the position is at its peak. | B. They have the same absolute value but different signs. | C. They are equivalent. | D. There is no relationship between the two values.": "B", 
            "4. In a spring-block oscillator vertical motion system with spring constant k and amplitude d, what is the weight (mg)?  A. k * A | B. 1/2k d^2 | C. k * d | D. -kx": "C", 
            "5. Calculate the frequency of a pendulum with length 0.5 kilometers on a planet with g = 15 m/s.  A. 0.0276 Hz | B. 36.276 Hz | C. 1.147 Hz | D. 0.872 Hz": "A", 
            "6. Find the mass of a spring with a spring constant of 100 N/m that allows an object to be bouncing 1 meter above the ground when pulled in 20 centimeters on Earth.   A. 0.408 kg | B. 0.204 kg | C. 2.04 kg | D. Cannot calculate without knowing the kinetic energy.": "B", 
            "7. What is the maximum velocity of a block on a mass-spring system on Earth with amplitude of 30 centimeters, spring constant of 40 N/m, and weight of 44.1 N?  A. 2.98 m/s | B. 0.286 m/s | C. 0.101 m/s | D. 0.8944 m/s": "D", 
            "8. In a room, two springs, one extending down from the ceiling and another up from the ground connect to a block of mass 3 kg such that they don't touch each other and the block isn't moving. The spring from the top has a spring constant of 30 N/m, and the spring connected from the ground has one of 25 N/m, and the block is initially motionless. If the top spring is compressed 52 centimeters past equilibrium, how far is the bottom spring stretched?  A. 1.376 m | B. 1.200 m | C. 1.336 m | D. 1.233 m": "C", 
            "9. For a string pendulum that's at an angle theta measured from the vertical, what is the restoring force?  A. mg | B. mgcos(theta) | C. mgsin(theta) | D. Cannot determine without the length of the string.": "C", 
            "10. When a large mass (M) is moving on the mass-spring system with amplitude A and spring constant k and another smaller mass (m) is placed on top, under what condition will it NOT slide off?  A. The speed of the system < kA/(M + m) | B. The coefficient of friction < kA/(M + m) | C. The speed of the system > kA/(M + m) | D. The coefficient of friction > kA/(M + m)": "D" 
        }
        
    turtle_movement(activities, turtle) # Inputs the questions to turtle_movement, which uses them to track the turtle's movement depending on the user's answers.
