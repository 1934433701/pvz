import pygame, sys
from plants.peashooter import Peashooter
from plants.sunflower import SunFlower
from plants.wallnut import WallNut

# 这初始化

pygame.init()

# 窗体大小
screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
# 窗体名称
pygame.display.set_caption('pvz')
# 背景
bg_path = 'images/Background.jpg'
backgroup = pygame.image.load(bg_path).convert()
#卡槽
card_slot=pygame.image.load('images/cardSlot.png').convert()
#card
card=pygame.image.load('images/cards/card_peashooter.png').convert()
card1=pygame.image.load('images/cards/card_sunflower.png').convert()
card_rect=card.get_rect()
card1_rect=card1.get_rect()
scale=0.78
card=pygame.transform.scale(card,(int(card_rect.width*scale),int(card_rect.height*scale)))
card1=pygame.transform.scale(card1,(int(card1_rect.width*scale),int(card1_rect.height*scale)))
#阳光数
sunnum='0'
font=pygame.font.SysFont('arial',20)
fontImg=font.render(sunnum,True,(0,0,0))



# 主函数
def main():
    block = pygame.time.Clock()
    # peashooter = Peashooter()
    #点击存放卡片的图像
    clickimage=[]
    # 临时存放pea
    p1 = []
    peaList=[]
    # sunflower=SunFlower()
    wallnut=WallNut()
    index = 0
    #是否点击了卡片
    is_pick=False

    while 1:

        block.tick(30)
        # 绘制背景
        screen.blit(backgroup, (0, 0))
        #卡槽
        screen.blit(card_slot, (250, 0))
        #card
        screen.blit(card, (330, 10))
        screen.blit(card1, (400, 10))
        #sunnum
        screen.blit(fontImg, (280, 60))

        #鼠标点击（0，0，0）（1，0，0）
        press=pygame.mouse.get_pressed()
        #坐标
        x,y=pygame.mouse.get_pos()

        if index > 13:
            index = 0
        # screen.blit(peashooter.images[index % 13], peashooter.rect)
        # screen.blit(sunflower.images[index % 18], sunflower.rect)
        # screen.blit(wallnut.images[index % 16], wallnut.rect)

        for image in clickimage:
            screen.blit(image.images[0], (x,y))
        for p in p1:
            screen.blit(p.images[0], p.zone)
        for pea in peaList:
            screen.blit(pea.images[index % 13], pea.zone)



        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type==pygame.MOUSEMOTION:
                # print(x,y)
                if not is_pick:
                    if 330<=x<=330+card.get_rect().width and 10<=y<=10+card.get_rect().height:
                        if press[0]:
                            p = Peashooter()
                            clickimage.append(p)
                            is_pick=True

                    if 400<=x<=400+card1.get_rect().width and 10<=y<=10+card1.get_rect().height:
                        if press[0]:
                            sunflower=SunFlower()
                            clickimage.append(sunflower)
                            is_pick = True
                if is_pick:
                    #330 180  405 274
                    if 330 <= x <= 405 and 180 <= y <= 274:
                        p=Peashooter()
                        p.zone=(330,180)
                        p1.append(p)
                        if press[0]:
                            peaList.append(p)
                            clickimage.clear()
                            p1.clear()
                            is_pick=False

                    else:
                        p1.clear()


                    if press[2]:
                        clickimage.clear()
                        is_pick=False



        index += 1


if __name__ == '__main__':
    main()
