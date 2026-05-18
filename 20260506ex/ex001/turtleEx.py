import turtle

t=turtle.Turtle() #그림그리기준비완료
t.shape('turtle') #아이콘설정

angle=120

t.right(angle)    #오른쪽으로 120도 회전
t.forward(100)    #100픽셀 실선 그리기

t.left(angle)     #왼쪽 120도 회전
t.forward(100)

t.left(angle)     #왼쪽 120도 회전
t.forward(100)