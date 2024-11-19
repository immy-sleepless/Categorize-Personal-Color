Is it your personal color | AIB
ก่อนจะไปดูว่าโปรเจคนี้ทำอะไร อยากให้เห็นแนวคิดความเป็นมาเป็นไปของ โปรเจคก่อนค่ะ ไอเดียหลักของโปรเจคนี้คือการแก้ปัญหาเกี่ยวกับ ‘‘ personal color ’’ หรือเรื่องโทนสีที่เหมาะกับแต่ละบุคคล แม้ว่าเราจะรู้ว่าเราตรงกับ personal color ฤดูใบไม้ร่วง แต่การแยกว่าสิ่งของที่เรากำลังจะซื้ออยู่ในโทนตรงกับเรารึเปล่าก็ไม่ใช่เรื่องง่ายค่ะ โดยเฉพาะเครื่องสำอางที่มีสีสันใกล้เคียงกันวางเรียงรายบนแท่นแสดงสินค้า อีกทั้งมนุษย์เรายังมีอคติมองว่าสีที่ตนชอบตรงกับ personal color ของตน

อธิบายโปรเจค
-ชุดข้อมูล มีทั้งหมด 4 คลาส (4 ฤดู) แต่ละคลาสประกอบด้วยค่า RGB เครื่องสำอาง 100 สี และนำไปทำ Data augment ต่อ
-โมเดลที่ใช้คือที่ Support Vector Machine และ Grid Search
-Baseline เปรียบเทียบกับความสามารถในการแยกของมนุษย์โดยมีวัตถุประสงค์ให้โมเดลมีความสามารถ 120% ของมนุษย์

ปัญหาที่พบ
ระหว่างทำมีปัญหาเกี่ยวกับ Data set ที่มีจำนวนค่อนข้างน้อยเพราะไม่มีข้อมูลค่า rgb ของสีเครื่องสำอางในโทนต่างๆจึงต้องทำชุดข้อมูลเอง
