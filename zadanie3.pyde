def setup():
    size(500, 400)
    textSize(70)
    background(0,0,255)
    
    
def draw():
    fill(255)
    
    if ((mouseX > 150) and (mouseX < 200) and
    (mouseY > 150) and (mouseY < 210)): 
        fill(255,0,0)
    text("A", width/2-100, height/2)
    
    fill(255)
   
    if keyPressed == (key == 's'):
        fill(0,255,0)
        
    text("S", width/2+100, height/2)
    

    s = createShape()
    s.beginShape()
    s.fill(255,0,0) 
    s.stroke(255,0,0)
    s.vertex(100, 70)
    s.vertex(60, 150)
    s.vertex(100, 220)
    s.vertex(200, 220)
    s.vertex(235, 150)
    s.vertex(200, 70)
    s.vertex(185, 70)
    s.vertex(220, 150)
    s.vertex(190, 205)
    s.vertex(110, 205)
    s.vertex(75, 150)
    s.vertex(115, 70)
    s.endShape(CLOSE) 
    shape(s, 25, 25)
    s = createShape()
    s.beginShape()
    s.fill(0,255,0)
    s.stroke(0,255,0)
    s.vertex(260, 205)
    s.vertex(260, 220)
    s.vertex(420, 220)
    s.vertex(420, 205)
    s.vertex(410, 185)
    s.vertex(400, 205)
    s.vertex(390, 185)
    s.vertex(380, 205)
    s.vertex(370, 185)
    s.vertex(360, 205)
    s.vertex(350, 185)
    s.vertex(340, 205)
    s.vertex(330, 185)
    s.vertex(320, 205)
    s.vertex(310, 185)
    s.vertex(300, 205)
    s.vertex(290, 185)
    s.vertex(280, 205)
    s.vertex(270, 185)
    s.endShape(CLOSE)
    shape(s, 25, 25)
