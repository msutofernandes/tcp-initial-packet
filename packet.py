student_number = 7952153
seq_number = "00000000"
ack_number = "00000000"
data_offset = 51020000
print ( hex(int(str(student_number)[-4:])) + hex(int(str(student_number)[:4])).split('x')[1] ).upper() + str(seq_number) + str(ack_number) + str(data_offset);