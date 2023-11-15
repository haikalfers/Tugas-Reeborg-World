"""
Kelas : 2023E
Prodi : D4 Manajemen Informatika
Kelompok 4
Anggota Kelompok
1. Zaidan Dhiya Ulhaq (23091397152)
2. Alya Faadhilah Putri (23091397153)
3. Haikal Ferdian Saputra (23091397154)
"""

#Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def mlampah():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()

def jalan_kaki():
    move()
    turn_left()
  
mlampah()
jalan_kaki()
mlampah()
jalan_kaki()
mlampah()
jalan_kaki()
mlampah()
jalan_kaki()
mlampah()
jalan_kaki()
mlampah()
jalan_kaki()

#Hurdle 2

def turn_right():
    for i in range(3):
        turn_left()
    
def vertical_pass():
    turn_left()
    for i in range(2):
        move()
        turn_right()
    move()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        vertical_pass()

#Hurdle 3
def turn_right():
    for i in range(3):
        turn_left()
        
def serong_kiri()
    move()
    turn_left()
    
def vertical_pass():
    turn_left()
    for i in range(2):
        move()
        turn_right()
    serong_kiri()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        vertical_pass()
